import json,pathlib,subprocess,hashlib
root=pathlib.Path(__file__).parent
records=[]
for e in json.loads((root/'catalog.json').read_text()):
 p=root/'assets/exams'/e['id'];pdf=p.with_suffix('.pdf');audio=p.with_suffix('.mp3')
 assert pdf.read_bytes().startswith(b'%PDF-')
 info=subprocess.check_output(['pdfinfo',str(pdf)],stderr=subprocess.DEVNULL).decode()
 pages=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
 meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(audio)]))
 duration=float(meta['format']['duration']);assert duration>600
 subprocess.run(['ffmpeg','-v','error','-i',str(audio),'-f','null','-'],check=True)
 records.append({'id':e['id'],'pages':pages,'audioSeconds':duration,'pdfSha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'audioSha256':hashlib.sha256(audio.read_bytes()).hexdigest()})
 print(e['id'],pages,'pages',round(duration,2),'seconds: PASS')
(root/'assets/manifest.json').write_text(json.dumps(records,indent=2))
