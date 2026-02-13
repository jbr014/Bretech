# Bretech — Static Website

This is a simple, modern static website scaffold for Bretech (IT infrastructure services). Files are in this folder.

What I created:
- `index.html` — Home page
- `services.html` — Services listing
- `about.html` — About / team
- `contact.html` — Contact form
- `assets/css/style.css` — Site styles
- `assets/js/main.js` — Minimal JS (nav toggle, demo form)

Images:
- The site currently uses direct image URLs from Pexels for hero, services and team photos. If you prefer local copies, download the referenced images from https://www.pexels.com and save them in `assets/images/`, then update the `img` `src` values to point to the local files.

Preview locally:
1. Open a terminal in this folder
2. Run a simple HTTP server (Python 3):

```bash
python -m http.server 8000
```

3. Open `http://localhost:8000` in your browser

Next steps I can help with:
- Replace the placeholder images with selected Pexels images
- Add a simple backend for the contact form (Node/Express or serverless endpoint)
- Deploy the site (Netlify, Vercel, GitHub Pages)
