# HSK Studio v2
Static personal study app. Serve the root with an HTTP server, or import the repository into Vercel with Framework Preset Other, no build command, root output.

## Library
Six official published papers from Chinese Test: H10901, H20901, H31001, H41001, H51001, H61001. Each has a real source PDF link and official audio archive link, with an independent answer sheet. Source: https://old.chinesetest.cn/godownload.do
PDFs remain hosted by Chinese Test. Embedding depends on browser support/source response; use the open-in-new-tab or local PDF fallback. Audio archives are RAR: download, extract, then load the MP3 in the local player. Files are not uploaded. The HSK 3.0 experience/sample pack links open the official external resources.

## Features
Search, level filtering, favorites, per-paper resume, timed/free practice, flags, unanswered navigation, Chinese writing, local audio with speed controls, history, JSON and CSV export. H31001 objective questions 1–70 are checked against the official key; writing is shown for manual comparison. Other official papers use manual comparison with the answer key in the PDF. Practice scores are not certificate scores. The previous 40-question original exercise remains at practice.html.

## Limits
This is a PDF practice workspace, not an exact official computer exam clone. Whole-paper timers do not lock individual sections. External resources require network access. Progress is local to the browser. No account sync or anti-cheating. Browser file handles must be reselected after reload. Up to 50 completed official-paper attempts are stored.

## Verification
Run `node test.cjs`. Syntax and logic checks passed. Browser tested search/select, H31001 answer entry, reload persistence, Chinese text input, submission, objective scoring, writing review, history, and H10901 free-practice pause/resume. External PDF rendering did not complete in the test browser; fallback links and local selector are provided. Actual MP3 playback was not verified with an official audio file.

## Deployment status
Not deployed: earlier Vercel creation returned 403 (no project creation permission). Current team project listing remains empty. GitHub repository access is not yet available. No production URL is claimed.
