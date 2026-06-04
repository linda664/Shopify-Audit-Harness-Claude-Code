---
name: crawl
description: Phase 1 of the Qosmic audit. Crawl a Shopify storefront and capture artifacts.
---

# Crawl

## Goal
Visit the storefront and capture page contents from all key surfaces. These artifacts are your evidence base for Phase 2 reasoning.

## Pages to crawl (in order)

1. Homepage — `/`
2. Products/collections page — `/collections/all` or `/products`
3. 2-3 individual product pages — pick the hero product + one more
4. Cart — `/cart`
5. Where To Buy or Store Locator (if exists)
6. FAQ or About (if exists)
7. Blog (homepage only, not individual posts)

## For each page, capture

- Full page URL
- Page title and meta description (check `<title>` and `<meta name="description">`)
- Hero headline and CTA text
- Navigation items
- Any trust signals (reviews count, awards, certifications)
- Broken elements (404s, missing images, empty sections)
- Mobile-friendliness signals

## Technical checks to run

For each of these, record Pass / Warn / Fail + one-line detail:

- SSL certificate (does HTTPS load?)
- HTTPS redirect (does HTTP redirect to HTTPS?)
- Sitemap (does `/sitemap.xml` exist?)
- Robots.txt (does `/robots.txt` exist?)
- Critical pages loading (homepage, product, cart)
- Meta tags (title + description present?)
- Structured data (any JSON-LD on product pages?)
- Favicon (visible?)
- Mobile-friendly (viewport meta tag present?)
- Page speed mobile (estimate: fast / slow based on asset count)
- Page speed desktop (estimate)
- Broken links (any 404s encountered?)
- Image optimization (large uncompressed images?)
- Cookie/privacy (consent banner or privacy policy link?)
- Checkout reachable (can you reach `/checkout` or add to cart?)

## Output

Save all findings in a structured scratch note. You will use this in Phase 2.
When done, read `skills/reason.md` and proceed.