# HTTPS and Security Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Enables HSTS preloading.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are HTTPS-only.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF cookies are HTTPS-only.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection.

## Deployment
- SSL/TLS configured via Nginx/Apache
- Certificates installed and HTTPS enforced

## Review
- All forms tested for CSRF protection
- Headers verified using browser dev tools
- No mixed content warnings
