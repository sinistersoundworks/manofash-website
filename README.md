# Manofash Website

A minimalist Pelican-based website with a black grungy background, large logo display, and social media integration.

## Features

- **Minimalist Design**: Clean black background with subtle grungy texture
- **Large Logo Display**: Prominent branding with responsive sizing
- **Social Media Integration**: YouTube, Apple Music, Spotify, and Facebook links using Lineicons
- **Email Subscription**: Integrated subscription form via eocampaign1.com
- **Analytics**: Custom analytics tracking via Plausible
- **Responsive**: Mobile-friendly design
- **Favicons**: Complete favicon set for all devices

## Development Setup

### Prerequisites

- Python 3.8+
- Git

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd manofash-website-pelican
   ```

2. **Set up Python environment:**
   ```bash
   # Using direnv (recommended)
   direnv allow
   
   # Or manually create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the site:**
   ```bash
   make html
   ```

5. **Start development server:**
   ```bash
   make devserver
   ```
   
   The site will be available at `http://localhost:8000`

6. **Stop development server:**
   ```bash
   # Press Ctrl+C in the terminal running the server
   ```

### Development Commands

- `make html` - Generate static site
- `make clean` - Remove generated files
- `make devserver` - Start development server with auto-reload
- `make serve` - Start simple server without auto-reload
- `make publish` - Generate site with production settings

## Deployment to GitHub Pages

### Initial Setup

1. **Create GitHub repository:**
   - Create a new repository on GitHub
   - Name it `manofash-website` or your preferred name

2. **Initialize Git (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/manofash-website.git
   git push -u origin main
   ```

3. **Install ghp-import (if not already installed):**
   ```bash
   pip install ghp-import
   ```

### Deploy to GitHub Pages

1. **Generate production site:**
   ```bash
   make publish
   ```

2. **Deploy to GitHub Pages:**
   ```bash
   make github
   ```

   This command will:
   - Generate the site with production settings
   - Create/update the `gh-pages` branch
   - Push the generated site to GitHub Pages

3. **Configure GitHub Pages:**
   - Go to your repository on GitHub
   - Navigate to Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select branch: `gh-pages`
   - Select folder: `/ (root)`
   - Click Save

4. **Access your site:**
   - Your site will be available at: `https://yourusername.github.io/manofash-website`
   - It may take a few minutes for changes to appear

### Custom Domain (Optional)

1. **Add CNAME file:**
   ```bash
   echo "manofash.com" > content/extra/CNAME
   ```

2. **Update pelicanconf.py:**
   ```python
   EXTRA_PATH_METADATA = {
       # ... existing entries ...
       'extra/CNAME': {'path': 'CNAME'},
   }
   ```

3. **Configure DNS:**
   - Add CNAME record pointing to `yourusername.github.io`
   - Or add A records pointing to GitHub Pages IPs

4. **Update publishconf.py:**
   ```python
   SITEURL = 'https://manofash.com'
   ```

## Content Management

### Adding Content

- **Pages**: Add `.md` files to `content/pages/`
- **Articles**: Add `.md` files to `content/` (if you enable articles)
- **Images**: Add to `content/images/` and reference in Markdown

### Updating Social Media Links

Edit `theme/templates/index.html` and replace `href="#"` with actual URLs:

```html
<a href="https://youtube.com/yourchannel" class="social-link" aria-label="YouTube">
<a href="https://music.apple.com/yourprofile" class="social-link" aria-label="Apple Music">
<a href="https://open.spotify.com/artist/yourid" class="social-link" aria-label="Spotify">
<a href="https://facebook.com/yourpage" class="social-link" aria-label="Facebook">
```

### Customizing Design

- **Colors/Styling**: Edit `theme/static/css/style.css`
- **Layout**: Modify templates in `theme/templates/`
- **Logo**: Replace `content/extra/logo.png`

## Configuration Files

- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration
- `requirements.txt` - Python dependencies
- `Makefile` - Build and deployment commands

## Troubleshooting

### Common Issues

1. **Site not updating on GitHub Pages:**
   - Check the Actions tab for build errors
   - Ensure `gh-pages` branch exists and has content
   - Wait 5-10 minutes for changes to propagate

2. **Development server not starting:**
   - Check if port 8000 is already in use
   - Try `make serve` instead of `make devserver`

3. **Missing dependencies:**
   - Run `pip install -r requirements.txt`
   - Ensure you're in the correct virtual environment

4. **Images not loading:**
   - Check file paths in `EXTRA_PATH_METADATA`
   - Ensure images are in `content/extra/` or `content/images/`

### Getting Help

- Check Pelican documentation: https://docs.getpelican.com/
- GitHub Pages documentation: https://docs.github.com/pages
- Open an issue in this repository for project-specific problems

## Project Structure

```
manofash-website-pelican/
├── content/
│   ├── extra/
│   │   ├── favicons/
│   │   └── logo.png
│   └── pages/
│       └── home.md
├── theme/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       └── index.html
├── output/              # Generated site (ignored by git)
├── pelicanconf.py       # Development config
├── publishconf.py       # Production config
├── requirements.txt     # Dependencies
├── Makefile            # Build commands
└── README.md           # This file
```

## License

[Add your license information here]
