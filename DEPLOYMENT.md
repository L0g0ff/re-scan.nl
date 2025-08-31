# GitHub Pages Deployment Guide

## Quick Deployment Steps

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Re-Scan static website"
   ```

2. **Create GitHub Repository**:
   - Go to GitHub.com
   - Create a new repository named `re-scan.nl` (or any name you prefer)
   - Don't initialize with README (we already have one)

3. **Connect and Push**:
   ```bash
   git remote add origin https://github.com/YOURUSERNAME/re-scan.nl.git
   git branch -M main
   git push -u origin main
   ```

4. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Click "Settings" tab
   - Scroll to "Pages" in the left sidebar
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"

5. **Access Your Site**:
   - Your site will be available at: `https://YOURUSERNAME.github.io/re-scan.nl/`
   - GitHub will show you the exact URL in the Pages settings

## Custom Domain (Optional)

To use your own domain (www.re-scan.nl):

1. **Add CNAME file**:
   ```bash
   echo "www.re-scan.nl" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

2. **Update DNS Settings**:
   - Add a CNAME record pointing `www.re-scan.nl` to `YOURUSERNAME.github.io`
   - Or add A records pointing to GitHub Pages IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153

3. **Configure in GitHub**:
   - In Pages settings, add your custom domain
   - Enable "Enforce HTTPS"

## Before Going Live

### Add Your Images:
1. Replace `images/logo.png` with your actual logo
2. Add `images/favicon.ico` for the browser icon
3. Update any image references in the HTML

### Update Content:
1. Verify all contact information is correct
2. Update pricing if needed
3. Review all text content
4. Test the contact form functionality

### SEO Optimization:
1. Update meta descriptions in HTML
2. Add Google Analytics if needed
3. Submit to Google Search Console
4. Create sitemap.xml if desired

## File Structure Overview

```
re-scan.nl/
├── index.html          # Main website
├── css/style.css       # All styling
├── js/script.js        # Interactive features
├── images/             # Image assets
├── README.md           # Project documentation
├── DEPLOYMENT.md       # This file
├── _config.yml         # GitHub Pages config
└── .gitignore         # Git ignore rules
```

## Troubleshooting

- **Site not loading?** Check the Pages settings and ensure the correct branch is selected
- **Styles not working?** Verify all file paths are correct and case-sensitive
- **Contact form not working?** The form needs a backend service - consider Formspree or Netlify Forms
- **Images not showing?** Make sure image files are in the correct directory and paths match

## Performance Notes

The website is optimized for:
- Fast loading times
- Mobile responsiveness
- SEO best practices
- Modern browser compatibility

## Support

For GitHub Pages specific issues, refer to: https://docs.github.com/en/pages