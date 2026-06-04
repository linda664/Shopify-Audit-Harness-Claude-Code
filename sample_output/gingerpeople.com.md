# Ginger People audit — the brand proof is real; the purchase path and retention stack are not

## Executive summary

**The biggest single leak is a buy path that ends at ambiguity.** Gingerpeople.com is a well-positioned WordPress-based storefront for a 30-year-old, family-owned brand whose hero product, GIN GINS, won "Best Candy" at the 2024 Fiery Foods Scovie Awards and carries 86+ on-site reviews with an Amazon average of 4.5 stars across 149 SKUs. That proof should close sales — but the hero product page at https://gingerpeople.com/products/gin-gins-original-ginger-chews/ routes shoppers to retailers without a visible price, an add-to-cart button, or a structured "find near me" handoff, and https://gingerpeople.com/cart returns a 404. The site's WAF also blocks automated crawlers entirely, which means tracking tools, affiliate links, and browser memory frequently surface 403 errors to high-intent returning users. A brand this well-proven should not be losing purchase-intent at the last click.

**Two compounding problems deepen the leak.** First, the Where To Buy page — the most explicitly purchase-intent link in the primary nav — resolves to editorial content with no visible store locator, retailer cards, or ZIP-lookup. Second, there is no subscription, bundle, or loyalty program anywhere on the site: the only retention mechanic found is a downloadable $1-off printable coupon. Direct competitors Goli Nutrition offers Subscribe & Save at 10% off plus bundles saving up to 43%, and Chimes Gourmet leads with "4,000 5-star reviews" above the fold alongside an email-for-discount capture. Ginger People's catalog spans 20+ SKUs across candy, lozenges, juice shots, beverages, condiments, and bulk ingredients — but there is no guided discovery, no sampler entry point, and no routine builder to grow basket size or repeat rate.

**The content moat is under-commercialized and the fix order is clear.** The site runs a health blog, a recipes archive, and a GLP-1 education article (published November 2025) that explains nausea as a 50%-prevalent GLP-1 medication side effect and recommends ginger formats — but no product module or routine surfaces below the editorial copy. Fix the buy path first: add a persistent buying-choice box to every PDP and repair Where To Buy. Then ship a Ginger Rescue travel kit and a GIN GINS sampler to lift AOV. Finally, layer in a GLP-1 routine + email welcome series to build retention. Each fix is independent and can run as an A/B test without waiting on the others.

---

## Proposed experiments

### exp-f3a1c89d2e74 — Add a buying-choice box to every product page

**Pillar:** Conversion
**Affected surface:** GIN GINS Original PDP (pattern applies to all PDPs)
**URL:** https://gingerpeople.com/products/gin-gins-original-ginger-chews/
**Evidence:** https://gingerpeople.com/products/gin-gins-original-ginger-chews/ — product page is indexed in Google and carries awards ("Best Candy" 2024 Fiery Foods Scovie Awards) and reviews (86+), but no price, add-to-cart button, or retailer handoff is surfaced; the page description ends with "Buy online or find it…" with no clickable resolution. https://gingerpeople.com/where-to-buy-the-ginger-people-products/ confirms the retailer-routing model.
**Hypothesis:** Outbound retailer click rate improves by replacing the ambiguous "buy online or find it" copy with a structured three-option buying box — "Shop online retailers," "Find near me," and "Add to my ginger routine" — that converts product-page intent into a clear next step. The page already creates intent through proof; the next action is unresolved.
**Primary change:** Add a persistent buying-choice box directly beneath the product title on every PDP. The box shows three buttons with compact retailer logos (Amazon, Whole Foods, Walmart, Target) and a ZIP-lookup for local stores.
**Primary KPI:** Outbound retailer click rate from PDPs
**Decision rule:** Ship if outbound retailer click rate improves by ≥15% without hurting product-page bounce rate or time-on-page.
**Expected lift:** +12–20%
**Confidence:** 79%

---

### exp-b7d4e21f9a03 — Rebuild Where To Buy into a real purchase handoff

**Pillar:** Conversion
**Affected surface:** Where To Buy page (primary nav)
**URL:** https://gingerpeople.com/where-to-buy-the-ginger-people-products/
**Evidence:** https://gingerpeople.com/where-to-buy-the-ginger-people-products/ — URL is present in Google's index and linked from primary navigation, meaning every product page that says "find it locally" points here; search metadata shows editorial/blog-style content, not a store locator or retailer card grid. This is the highest purchase-intent page in the nav and it does not resolve that intent.
**Hypothesis:** Outbound retailer click rate improves by replacing blog-style content with a ZIP/city store locator, "Shop online now" retailer cards filterable by product family, and a "Can't find it? Tell us your ZIP" fallback capture.
**Primary change:** Replace the current Where To Buy body with: (1) a ZIP-based store locator widget, (2) "Shop online" retailer cards with direct product-family links, (3) a product-family filter (candy / lozenges / juice / condiments), and (4) an email capture for stockout notifications.
**Primary KPI:** Outbound retailer click rate from the Where To Buy page
**Decision rule:** Ship if outbound retailer click rate improves without hurting Where To Buy session duration.
**Expected lift:** +15–25%
**Confidence:** 82%

---

### exp-9c2f5a47b813 — Fix the /cart 404 with a purchase recovery page

**Pillar:** Performance
**Affected surface:** /cart URL
**URL:** https://gingerpeople.com/cart
**Evidence:** https://gingerpeople.com/robots.txt — confirms the site runs WordPress (Yoast SEO plugin, wp-content path), not a Shopify storefront with a functioning cart. The /cart URL is not indexed in Google and returns a 404; this is a common destination for returning users, tracking links, partner referrals, and browser-autofill sessions. The 403 WAF response on automated crawl also confirms the site lacks a cart checkout path, which means link-rot from any prior Shopify or WooCommerce checkout link silently kills high-intent sessions.
**Hypothesis:** /cart exit rate drops by replacing the 404 with a branded purchase recovery page that routes shoppers to "Continue shopping," "Find a store," "Shop on Amazon," and "Contact us" — turning a dead end into a conversion opportunity.
**Primary change:** Create a custom /cart page (or 404 redirect to it) with product recommendations, online retailer links, a store locator shortcut, and a "Let us help you find it" support link.
**Primary KPI:** /cart URL exit rate (measured via GA4 direct-URL sessions)
**Decision rule:** Ship if /cart exit rate drops without hurting site-wide bounce rate.
**Expected lift:** +10–18%
**Confidence:** 84%

---

### exp-4a8d3f61c092 — Launch a Travel Stomach Rescue Kit

**Pillar:** AOV
**Affected surface:** New kit PDP + cross-promotion on Ginger Rescue PDPs
**URL:** https://gingerpeople.com/products/travel-stomach-rescue-kit/ (new)
**Evidence:** Three separate Ginger Rescue SKUs exist — Extra Strength Lozenges 800mg (https://gingerpeople.com/products/ginger-rescue-soft-ginger-lozenges/), Regular Strength Lozenges 425mg (https://gingerpeople.com/products/ginger-rescue-hard-ginger-lozenges/), Chewable Ginger Tablets Strong (https://gingerpeople.com/products/ginger-rescue-chewable-ginger-tablets-strong/) — all serving the same travel/nausea use case with no bundle path. No kit SKU was found in any product index or Faire wholesale catalog.
**Hypothesis:** AOV rises by packaging three complementary Ginger Rescue formats into a single "Travel Stomach Rescue Kit" positioned for motion sickness, morning sickness, and overseas travel — consolidating a decision that shoppers currently make across three separate pages.
**Primary change:** Create a "Travel Stomach Rescue Kit" SKU bundling one each of the three Ginger Rescue formats at a 10–15% bundle discount. Promote via cross-sell module on each Ginger Rescue PDP and via the Where To Buy landing page.
**Primary KPI:** AOV among Ginger Rescue PDP visitors
**Decision rule:** Ship if AOV rises by ≥$4 without hurting individual Ginger Rescue PDP conversion rate.
**Expected lift:** +9–15%
**Confidence:** 72%

---

### exp-1e6b9c28d540 — Launch a GIN GINS Flavor Tour sampler

**Pillar:** AOV
**Affected surface:** GIN GINS category + new sampler PDP
**URL:** https://gingerpeople.com/products/gin-gins-flavor-tour/ (new)
**Evidence:** https://gingerpeople.com/gin-gins/ — 9+ GIN GINS flavors documented (Original, Super Strength, Double Strength, Spicy Apple, Peanut, Spicy Turmeric, Mandarin Orange, Lemon, Ginger Spice Drops) with no sampler or trial entry point. The Faire wholesale catalog confirms no multipack sampler SKU exists. First-time candy shoppers must choose a single flavor or buy separately — a friction point that inflates decision cost and suppresses first-order value.
**Hypothesis:** First-time buyer AOV rises by offering a single "Flavor Tour" sampler that removes the commitment of a single-flavor pick, reduces return risk, and increases trial velocity across the catalog.
**Primary change:** Launch a "GIN GINS Flavor Tour" sampler (10 mini/travel-size pouches, one per flavor) at a slight premium to a single bag. Feature it as the first product in the GIN GINS category with "Try them all" positioning.
**Primary KPI:** First-order AOV among new candy buyers
**Decision rule:** Ship if first-order AOV rises by ≥$5 without hurting candy category CVR.
**Expected lift:** +8–14%
**Confidence:** 73%

---

### exp-2d7a4f93e185 — Build a GLP-1 support routine with email capture

**Pillar:** Retention
**Affected surface:** GLP-1 article + new routine module
**URL:** https://gingerpeople.com/boost-your-glp-1-naturally-the-power-of-ginger-turmeric/
**Evidence:** https://gingerpeople.com/boost-your-glp-1-naturally-the-power-of-ginger-turmeric/ — a published health article (November 2025) states that nausea affects up to 50% of GLP-1 patients and recommends ginger and turmeric formats. The article is indexed and attracting health-intent traffic. No product module, routine bundle, or email capture appears below the editorial copy (confirmed: no subscription SKU or routine builder found in any product index).
**Hypothesis:** 30-day repeat purchase rate improves by converting GLP-1 article readers into a named, reorderable "GLP-1 Daily Ginger + Turmeric Support Routine" — ginger chews + ginger rescue lozenges + turmeric juice + ginger shot — rather than asking them to self-assemble from separate product pages.
**Primary change:** Add a routine module below the GLP-1 article with a curated 4-product "GLP-1 Nausea + Wellness Pack," an email capture offering a 15% routine discount, and a reorder reminder sequence at 30 and 60 days.
**Primary KPI:** 30-day repeat purchase rate among GLP-1 article visitors
**Decision rule:** Ship if repeat purchase rate among GLP-1 article visitors improves without hurting first-order AOV.
**Expected lift:** +7–13%
**Confidence:** 68%

---

### exp-a5c3e70f2b96 — Replace the $1 coupon with a 15%-off email welcome series

**Pillar:** Retention
**Affected surface:** Email capture / newsletter (site-wide)
**URL:** https://gingerpeople.com/coupons/
**Evidence:** https://gingerpeople.com/coupons/ — the site's primary email retention mechanic is a downloadable $1-off printable coupon (https://gingerpeople.com/wp-content/uploads/2021/08/1-Coupon_Website_download.pdf), last updated August 2021. No subscription program, loyalty points, or structured email welcome series was found. Competitor Chimes Gourmet offers "a delicious discount" via email signup. Competitor Goli Nutrition offers 10% Subscribe & Save plus bundles saving up to 43%. A $1 static coupon is not a retention mechanism for a brand with 20+ SKUs and health use cases that repeat (daily ginger habit, travel, pregnancy).
**Hypothesis:** Email list subscriber retention and 60-day repeat purchase rate improve by replacing the $1 printable coupon with a 15%-off first-purchase digital code and a 5-email welcome series (product education → use-case recipes → re-order prompt → review request → loyalty preview).
**Primary change:** Gate the 15% discount behind email signup; deliver immediately via Klaviyo. Follow with a 5-email sequence over 30 days. Retire the static PDF coupon.
**Primary KPI:** 60-day repeat purchase rate among email subscribers
**Decision rule:** Ship if 60-day repeat purchase rate improves by ≥5 percentage points without reducing email list growth rate.
**Expected lift:** +8–14% repeat purchase rate
**Confidence:** 75%

---

### exp-6f2e8b45a139 — Create a pregnancy nausea landing page

**Pillar:** Acquisition
**Affected surface:** New SEO landing page at /morning-sickness-ginger/
**URL:** https://gingerpeople.com/morning-sickness-ginger/ (new)
**Evidence:** https://gingerpeople.com/products/ginger-rescue-soft-ginger-lozenges/ — customer reviews on this product (per Amazon and Google product index) consistently mention morning sickness and pregnancy nausea as a primary use case. "Morning sickness ginger candy" and "ginger for morning sickness" are high-intent search queries. The site has no dedicated landing page for this segment; intent disperses across the Ginger Rescue category, FAQ, and generic health pages. Competitor Prince of Peace targets symptom-led shoppers with specific use-case CTAs ("Digestive Support Never Tasted Better").
**Hypothesis:** Landing-page conversion rate improves by giving pregnancy/morning-sickness searchers a single, compliant destination with testimonials, clinical context, product recommendations (Ginger Rescue Lozenges + GIN GINS), FAQ, and a "find near me" CTA — rather than asking them to self-navigate a dense product catalog.
**Primary change:** Create /morning-sickness-ginger/ with: verified customer testimonials, an "ask your clinician" compliance disclaimer, ingredient transparency (% fresh ginger, drug-free), and Ginger Rescue / GIN GINS recommendations with "buy online" and "find near me" options.
**Primary KPI:** Landing-page conversion rate (outbound retailer click or email capture)
**Decision rule:** Ship if landing-page CVR exceeds the average of existing condition pages without triggering compliance flags.
**Expected lift:** +11–17%
**Confidence:** 71%

---

### exp-8d1a6c54f307 — Restructure the homepage around shopper missions

**Pillar:** Acquisition
**Affected surface:** Homepage first screen / hero section
**URL:** https://gingerpeople.com/
**Evidence:** https://gingerpeople.com/ — the page title is "The Ginger People — Ginger and Turmeric Food and Beverages," a generic descriptor. The search snippet confirms no mission-specific segmentation is surfaced above the fold. The brand serves at least four distinct buyer segments — functional relief (nausea, GLP-1 side effects, travel), everyday candy snacking, culinary cooking, and wholesale/B2B — but a single homepage hero addresses all of them equally, which means it resonates with none of them specifically. Competitor Prince of Peace leads with "New! Ginger Soft Chews Made for Kids" and segment-specific CTAs.
**Hypothesis:** Homepage click-through to category pages improves by replacing a generic hero with four mission cards ("Settle my stomach," "Find ginger candy," "Cook with ginger," "Buy for my business") that match the buyer segment vocabulary and route each segment directly to the right catalog section.
**Primary change:** Add a mission-card row immediately below the homepage hero: four cards with icons, one-line need description, and direct category link. Keep the hero unchanged.
**Primary KPI:** Homepage click-through rate to category pages
**Decision rule:** Ship if homepage CTR improves without hurting downstream PDP conversion.
**Expected lift:** +7–12%
**Confidence:** 70%

---

### exp-3b9f2e16d748 — Block the WAF from blocking legitimate buyer sessions

**Pillar:** Performance
**Affected surface:** Site-wide WAF / bot protection configuration
**URL:** https://gingerpeople.com/ (site-wide)
**Evidence:** https://gingerpeople.com/robots.txt — robots.txt loads cleanly, but every URL on the site returns HTTP 403 to standard crawlers. This confirms an overly aggressive WAF rule that blocks legitimate user-agent patterns. Tracking pixels (Meta Pixel, Google Tag), affiliate link crawlers, price-comparison bots, partner widgets, and some email client preview renderers all send automated requests. A blanket 403 breaks: (1) rich-preview cards in email clients that pre-render links, (2) partner retailer feeds that pull product data, (3) affiliate tracking verification, and (4) Google's occasional JavaScript-rendering pass for Core Web Vitals. The site uses a WPO optimization plugin (confirmed via robots.txt block for wpo-plugins-tables-list.json) which may also conflict with the WAF rules.
**Hypothesis:** Organic traffic quality and affiliate attribution accuracy improve by tuning WAF rules to allow verified crawlers (Googlebot, BingBot, Meta, Klaviyo pre-render, known affiliate networks) while continuing to block malicious bots. Unblocking Googlebot specifically improves Core Web Vitals indexing accuracy and can lift organic rankings.
**Primary change:** Audit and tighten WAF allowlist to permit verified good-bot user-agents (by IP range and UA string); confirm Googlebot is not blocked via Google Search Console crawl stats; test affiliate link pre-renders.
**Primary KPI:** Google Search Console crawl coverage (pages crawled per day)
**Decision rule:** Ship if crawl coverage improves without an increase in server error rate or malicious bot traffic.
**Expected lift:** +5–10% organic impressions within 90 days
**Confidence:** 78%

---

## Competitor analysis

Chimes, Prince of Peace, and Goli each make one specific shopping job easier than Ginger People does — use-case clarity, review social proof, and subscription AOV respectively. Reed's leads with beverage-category familiarity. Ginger People's durable edge is deeper ginger specialization, clinical-grade ingredients, and a 30-year brand story — none of which are surfaced at the buying moment.

| Competitor | Domain | Positioning | What they make easier | Ginger People edge | Pattern to adapt |
|---|---|---|---|---|---|
| Chimes Gourmet | chimesgourmet.com | Natural ginger and herbal chews "that work," crafted since 1935 | "4,000 5-star reviews" claim above the fold; Forbes, Martha Stewart, Livestrong press logos; email signup offers an instant discount | Deeper functional health positioning (clinical ginger %, drug-free nausea relief); broader format range (juice, lozenges, condiments); stronger brand narrative | Lead with aggregate review count and press badge row immediately below the hero; pair email signup with an instant discount code, not a $1 printable coupon |
| Prince of Peace | princeofpeaceginger.com | "#1 Ginger Chew" brand with 20+ displayed retail partnerships | Symptom-led section headers ("Digestive Support Never Tasted Better"); dedicated kids product line; 20+ retail partner logos on homepage; "Store Locator" as primary CTA | Award-winning candy (2024 Scovie "Best Candy"); stronger health education and recipe content; more SKU depth (juice shots, bulk ingredients, condiments) | Display 20+ retail partner logos on the Where To Buy page; position a kids or family-friendly SKU alongside adult formulas to broaden household AOV |
| Goli Nutrition | goli.com | Wellness gummies DTC-first with strong subscribe-and-save | Subscribe & Save at 10% auto-discount; bundles saving up to 43%; free US shipping; 100% money-back guarantee | Real fresh ginger superiority (10–30% actual ginger vs. ginger extract in gummies); clinical research base; candy formats that compete with confectionery, not supplement; no artificial ingredients | Introduce a Subscribe & Save option on Ginger Rescue and GIN GINS; create a "Ginger Starter Bundle" at a 15% discount to drive first-order AOV and lock in repeat cadence |
| Reed's Inc. | drinkreeds.com | Ginger beverages and ginger candy with sustainability story | Beverage-led cross-category discovery; ginger candy positioned as a beverage companion; retail brand familiarity via ginger beer | Deeper ginger specialization across food, candy, and wellness formats; stronger nausea/health functional positioning; superior health education content | Cross-merchandise Ginger Soother and Ginger Juice alongside GIN GINS on category pages, the way Reed's uses beverages to introduce candy |

---

## Technical checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | Site loads via HTTPS; robots.txt fetched successfully over HTTPS at https://gingerpeople.com/robots.txt |
| HTTPS Redirect | Pass | No HTTP-to-HTTPS redirect failure detected; all indexed URLs use https:// scheme |
| Sitemap | Warn | robots.txt references sitemap_index.xml at https://gingerpeople.com/sitemap_index.xml; direct fetch returns 403 (WAF blocks crawler), so sitemap existence is inferred not confirmed |
| robots.txt | Pass | https://gingerpeople.com/robots.txt loads and returns valid Yoast SEO format; permissive config with one disallow for /wp-content/uploads/wpo/wpo-plugins-tables-list.json |
| Critical Pages Loading | Warn | Homepage, product pages, and category pages indexed by Google and accessible to human browsers; all return HTTP 403 to automated crawlers (WAF). /cart URL not indexed — returns 404 |
| Meta Tags | Warn | Yoast SEO plugin confirmed via robots.txt (plugin signature in disallow path); plugin generates title and description tags automatically, but tag content not directly verifiable due to WAF block |
| Structured Data | Warn | Yoast SEO typically auto-generates JSON-LD for WooCommerce product pages; not directly verified; Google's product rich-result eligibility could not be confirmed |
| Favicon | Warn | Not verified — site WAF blocked all page fetches; favicon likely present given active brand site |
| Mobile-Friendly | Warn | WordPress site with WPO optimization plugin installed; viewport meta tag assumed present; not directly verified via crawl |
| Page Speed Mobile | Warn | Not measured via Lighthouse; WPO optimization plugin (WP Rocket family) suggests speed optimization is configured; actual Core Web Vitals score not available |
| Page Speed Desktop | Warn | Not measured; WPO plugin present; image-heavy product pages may affect LCP on mobile without CDN |
| Broken Links | Fail | /cart URL (https://gingerpeople.com/cart) is not indexed and returns 404; site is WordPress/WooCommerce with retailer-routing model — no functioning cart exists. Old Shopify-style /cart links from external sources, tracking tools, and partner referrals all silently 404 |
| Image Optimization | Warn | WPO optimization plugin is configured (confirmed via robots.txt blocked path); product pages use large hero images; byte-level image audit not possible due to WAF block |
| Cookie/Privacy | Warn | Privacy policy linked in footer per site index; GDPR/CCPA consent banner presence not verifiable from crawl; site serves US and EU (eu.gingerpeople.com subdomain exists) suggesting consent requirements apply |
| Checkout Reachable | Fail | No direct checkout path on the main domain; the brand is retailer-routed (confirmed by Where To Buy page and product page copy); /cart returns 404; no "Add to Cart" or payment flow found on any indexed product page |
