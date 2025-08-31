# Re-Scan Monitor Solutions Website

Modern static website for Re-Scan monitoring solutions, built with HTML, CSS, and JavaScript for GitHub Pages deployment.

## Features

- **Responsive Design**: Optimized for all devices (mobile, tablet, desktop)
- **Modern UI**: Clean, professional design with smooth animations
- **Fast Loading**: Optimized static files with efficient CSS and JavaScript
- **SEO Friendly**: Semantic HTML structure and meta tags
- **Contact Form**: Functional contact form with validation
- **FAQ Section**: Interactive accordion-style FAQ
- **Pricing Cards**: Clear pricing presentation
- **Smooth Scrolling**: Enhanced navigation experience

## Structure

```
├── index.html          # Main webpage
├── css/
│   └── style.css       # Stylesheet with modern design
├── js/
│   └── script.js       # Interactive functionality
├── images/             # Image assets directory
│   └── .gitkeep       # Images placeholder
└── README.md          # This file
```

## Setup for GitHub Pages

1. Push this repository to GitHub
2. Go to repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Save and wait for deployment

## Customization

### Adding Images
- Add your logo as `images/logo.png` (recommended: 200x80px)
- Add favicon as `images/favicon.ico` (16x16px)
- Replace image paths in HTML as needed

### Updating Content
- Edit `index.html` to modify text content
- Update contact information in the contact section
- Modify pricing plans and features as needed

### Styling
- Primary color: `#54B435` (green)
- Secondary color: `#379237` (dark green)  
- Navy: `#0F172A`
- All colors can be modified in CSS custom properties (`:root` section)

### Contact Form
The contact form includes client-side validation. For production use, you'll need to:
1. Set up a backend service to handle form submissions
2. Update the form action attribute
3. Or integrate with services like Formspree, Netlify Forms, etc.

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Progressive enhancement for older browsers

## Performance

- Optimized CSS with modern techniques
- Efficient JavaScript with event delegation
- Lazy loading for images
- Smooth animations with GPU acceleration
- Minimal external dependencies (only Google Fonts)

## License

© 2024 Re-Scan Monitor Solutions. All rights reserved.