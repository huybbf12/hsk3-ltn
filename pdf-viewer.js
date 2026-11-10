import {getDocument,GlobalWorkerOptions} from './vendor/pdf.mjs';
GlobalWorkerOptions.workerSrc=new URL('./vendor/pdf.worker.mjs',import.meta.url).href;
let current=null;
window.openStudyPdf=async function(url){
 const host=document.querySelector('#pdfViewer');if(!host)return;
 if(current){current.cancelled=true;current.task?.destroy();}
 const state=current={cancelled:false,page:1,zoom:1,task:null,renderTask:null};
 host.innerHTML='<div class="pdf-tools"><button id="pdfPrev" aria-label="Trang trước">←</button><span id="pdfPage">Đang tải PDF…</span><button id="pdfNext" aria-label="Trang sau">→</button><button id="pdfZoomOut" aria-label="Thu nhỏ">−</button><button id="pdfZoomIn" aria-label="Phóng to">+</button></div><div class="pdf-canvas-wrap"><canvas id="pdfCanvas" aria-label="Trang đề thi PDF" role="img"></canvas></div><p id="pdfStatus" class="small" role="status">Đang mở tài liệu…</p>';
 const status=host.querySelector('#pdfStatus'),canvas=host.querySelector('canvas');
 try{
 state.task=getDocument({url,cMapUrl:'./vendor/cmaps/',cMapPacked:true,standardFontDataUrl:'./vendor/standard_fonts/'});const pdf=await state.task.promise;if(state.cancelled)return;
 let serial=Promise.resolve();
 const render=()=>{serial=serial.catch(()=>{}).then(async()=>{if(state.cancelled||!host.isConnected)return;const page=await pdf.getPage(state.page),v=page.getViewport({scale:1}),width=Math.max(250,host.clientWidth-24),viewport=page.getViewport({scale:width/v.width*state.zoom}),ratio=Math.min(devicePixelRatio||1,2);canvas.width=viewport.width*ratio;canvas.height=viewport.height*ratio;canvas.style.width=viewport.width+'px';canvas.style.height=viewport.height+'px';state.renderTask=page.render({canvasContext:canvas.getContext('2d'),viewport,transform:[ratio,0,0,ratio,0,0]});await state.renderTask.promise;if(state.cancelled)return;host.querySelector('#pdfPage').textContent=`Trang ${state.page} / ${pdf.numPages}`;host.querySelector('#pdfPrev').disabled=state.page===1;host.querySelector('#pdfNext').disabled=state.page===pdf.numPages;status.textContent='PDF đã tải · Dùng mũi tên để chuyển trang';});return serial;};
 host.querySelector('#pdfPrev').onclick=()=>{state.page=Math.max(1,state.page-1);render()};host.querySelector('#pdfNext').onclick=()=>{state.page=Math.min(pdf.numPages,state.page+1);render()};host.querySelector('#pdfZoomIn').onclick=()=>{state.zoom=Math.min(2,state.zoom+.2);render()};host.querySelector('#pdfZoomOut').onclick=()=>{state.zoom=Math.max(.6,state.zoom-.2);render()};await render();
 }catch(e){if(state.cancelled)return;status.textContent='Không tải được PDF. Kiểm tra mạng và thử lại.';const retry=document.createElement('button');retry.textContent='Tải lại PDF';retry.onclick=()=>window.openStudyPdf(url);status.append(' ',retry);console.error('PDF load failed',e);}
};
window.dispatchEvent(new Event('pdfviewerready'));
