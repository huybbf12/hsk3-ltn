# HSK Studio
Personal HSK 3 reading/writing practice. Original 40-question HSK 2.0 exercise; not a full exam or official HSK 3.0 simulator. No listening section yet.

Run locally: `python3 -m http.server 8080` from this directory, then open http://localhost:8080.

Deploy: upload index.html, app.js, style.css and questions.json to a GitHub repository. Import that repository in Vercel. Framework preset: Other. No build command. Root directory: repository root.

Features: timed 45-minute practice, untimed practice, autosave and resume in this browser, flags, answer comparison, local history. Timer persists across reloads. Written scoring uses reference answers; equivalent correct sentences may require manual review. Saved data is not synchronized across devices.

This version is static HTML/CSS/JS, without dependencies or API keys. Question data is intentionally client-visible for personal practice. No proctoring or high-stakes exam security.

Verification: JavaScript syntax, all 40 question IDs and choice mappings, answer normalization checks passed. Browser end-to-end testing and visual comparison with the official HSK client are not yet completed.
