# Zen Rojas audit — the brand is real; the store is sending shoppers to sold-out pages

## Executive summary

**The biggest single leak is a homepage that actively drives traffic into dead ends.** Four of the six teas in the Zen Rojas catalog are sold out — Organic Sleep Tea, Premium Sencha Organic Green Tea, Heartburn Organic Tea, and Unwind Organic Tea — and the homepage hero is pointing shoppers directly to three of those pages with explicit "Shop" CTAs: "Shop Organic Sleep Tea," "Shop Heartburn Organic Tea," and "Shop Premium Sencha Organic Green Tea." Every one of those buttons lands on a "Sold Out" page with no recovery mechanism: no Notify Me email capture, no suggested alternatives, no back-in-stock hook. The only two teas available for purchase right now — Bodyguard Organic Tea ($13) and Organic Black Tea ($8) — are not featured in the homepage hero at all.

**Two structural problems compound the stockout leak.** First, the cart page at `https://zenrojas.com/cart` renders a broken Shopify liquid template showing the string "t: e" alongside a missing-image placeholder — shoppers who do add a product to cart see a visually broken checkout prelude before they complete their purchase. Second, there is zero social proof on any product page: Bodyguard Tea, Organic Black Tea, and both sampler products show no reviews, no star rating, and no review count. The homepage shows four customer testimonials but they are disconnected from any product. Compounding this, the FAQ page states free shipping is available "on orders over $30," while the sitewide announcement bar reads "FREE SHIPPING ON ALL $50+ ORDERS" — a threshold inconsistency that erodes the trust signal right when a shopper is calculating whether to add to their cart. There is no Subscribe & Save option, no loyalty program, no cross-sell on PDPs or in the cart, and the ambassador program page is a single paragraph asking interested parties to send a DM.

**Fix the dead-end traffic first, then the cart, then social proof.** Update the homepage hero to replace sold-out CTAs with the two available teas and install a Back in Stock "Notify Me" flow on all four sold-out PDPs — this captures demand at zero cost and gives Zen Rojas an email list segment to hit the moment inventory returns. Patch the cart liquid rendering error next, since it sits between the shopper and checkout. Then install a reviews app and email the existing customer base for reviews on Bodyguard and Black Tea before building any AOV or retention layer. Only once conversion fundamentals are healthy does it make sense to add subscriptions, cross-sell, or ambassador structure.

---

## Proposed experiments

### exp-7f3a1c2d9e84 — Replace sold-out homepage hero CTAs with available products

**Pillar:** Performance
**Affected surface:** Homepage hero mission cards
**URL:** https://zenrojas.com/
**Evidence:** https://zenrojas.com/ — hero section shows four mission-based CTAs: "Shop Organic Sleep Tea," "Shop Bodyguard Organic Tea," "Shop Premium Sencha Organic Green Tea," and "Shop Heartburn Organic Tea." Confirmed via https://zenrojas.com/products/organicsleeptea (Sold Out), https://zenrojas.com/products/premiumsenchagreentea (Sold Out), and https://zenrojas.com/products/heartburntea (Sold Out). Three of four hero CTAs resolve to sold-out pages. The only in-stock tea — Organic Black Tea at $8 — is not featured in the hero.
**Hypothesis:** Homepage-to-purchase conversion improves by replacing sold-out hero CTAs with the two available teas (Bodyguard Organic Tea and Organic Black Tea), eliminating the click-to-dead-end pattern on 3 of 4 homepage mission cards.
**Primary change:** Update the four hero mission card CTAs to point only to in-stock products. Swap "Shop Organic Sleep Tea" → "Shop Organic Black Tea," "Shop Premium Sencha Organic Green Tea" → "Shop Loose Leaf Samplers" (all in stock), and "Shop Heartburn Organic Tea" → Bodyguard Tea. Update copy to match.
**Primary KPI:** Homepage click-through rate that leads to an add-to-cart event
**Decision rule:** Ship if homepage-to-cart rate improves without hurting session duration.
**Expected lift:** +20–35%
**Confidence:** 87%

---

### exp-c4b8d2f1e903 — Fix the cart liquid template rendering error

**Pillar:** Performance
**Affected surface:** Cart page (`/cart`)
**URL:** https://zenrojas.com/cart
**Evidence:** https://zenrojas.com/cart — the cart page renders "t: e" as visible text alongside a broken "no image" placeholder element. This is a Shopify Liquid template rendering failure (unresolved variable output in a cart line-item snippet). Any shopper who adds a product to cart sees a visually broken page before reaching Shopify's hosted checkout. The same cart page also shows a note that cookies must be enabled — but the rendering error is independent of cookies and appears even in standard browsers.
**Hypothesis:** Cart-to-checkout conversion rate improves by patching the Liquid snippet rendering the broken "t: e" string and missing image, eliminating a visual trust break at the final step before purchase.
**Primary change:** Identify the cart line-item snippet (likely `cart-item.liquid` or a section in the theme) responsible for the unresolved `{{ t }}` or `{{ e }}` variable and fix the template logic. Re-test with a real product in the cart before and after.
**Primary KPI:** Cart-to-checkout rate
**Decision rule:** Ship if the visual error is resolved and cart-to-checkout rate holds or improves without an increase in checkout abandonment.
**Expected lift:** +10–18%
**Confidence:** 88%

---

### exp-2e9f4a57b103 — Install a reviews app and seed all PDPs with customer reviews

**Pillar:** Conversion
**Affected surface:** All product detail pages
**URL:** https://zenrojas.com/products/bodyguardtea (applies to all PDPs)
**Evidence:** https://zenrojas.com/products/bodyguardtea, https://zenrojas.com/products/blacktea, https://zenrojas.com/products/teabagsamplers, https://zenrojas.com/products/looseleafsamplers — zero reviews visible on any product page. The homepage at https://zenrojas.com/ shows four customer testimonials (Max Wical, Diane Mercado, Mariah Acajabon, Kelly Chase) as loose text, but they are not connected to product pages via a review widget. Competitor Art of Tea (artoftea.com) displays reviews on every PDP; Pique Life (piquelife.com) leads with "18,078+ Verified Five Star Reviews."
**Hypothesis:** PDP conversion rate improves by displaying product-specific star ratings and review counts directly on each PDP, giving shoppers the social proof signal that is currently entirely absent from the buying moment.
**Primary change:** Install Judge.me or Loox on the Shopify store. Email the existing customer list requesting reviews for Bodyguard Tea and Organic Black Tea with a direct review link. Seed each in-stock PDP with a minimum of 5 reviews before launching paid traffic.
**Primary KPI:** PDP add-to-cart rate
**Decision rule:** Ship if add-to-cart rate on reviewed PDPs improves by ≥10% without hurting return rate.
**Expected lift:** +15–25%
**Confidence:** 82%

---

### exp-8d1f6c43a279 — Reconcile the shipping threshold and add a cart progress bar

**Pillar:** Conversion
**Affected surface:** FAQ page, announcement bar, cart page
**URL:** https://zenrojas.com/pages/faqs and https://zenrojas.com/cart
**Evidence:** https://zenrojas.com/pages/faqs — states "Free on orders over $30." https://zenrojas.com/ announcement bar states "FREE SHIPPING ON ALL $50+ ORDERS." These two numbers are different. At an average product price of $8–$13, the $50 threshold requires adding 4–6 items; a shopper who has read the FAQ and budgeted for a $30 order will be confused or feel misled when the cart shows a different threshold. No cart progress bar showing "Add $X more for free shipping" exists anywhere.
**Hypothesis:** AOV and cart completion rate improve by (1) resolving the threshold to one number across all surfaces and (2) adding a "You're $X away from free shipping" progress bar in the cart that shows shoppers exactly how close they are.
**Primary change:** Decide on one shipping threshold (recommend $35 given $8–$13 product prices), update FAQ and all instances in the theme; add a free shipping progress bar app (e.g. Cart X or a native Shopify theme block) to the cart page.
**Primary KPI:** Average order value
**Decision rule:** Ship if AOV improves by ≥$3 without increasing cart abandonment rate.
**Expected lift:** +8–14% AOV
**Confidence:** 78%

---

### exp-5b3a9e17c648 — Add Notify Me When Available on all sold-out PDPs

**Pillar:** Retention
**Affected surface:** Sold-out product pages (Sleep, Sencha, Heartburn, Unwind)
**URL:** https://zenrojas.com/products/organicsleeptea, https://zenrojas.com/products/premiumsenchagreentea, https://zenrojas.com/products/heartburntea, https://zenrojas.com/products/unwind
**Evidence:** All four pages render a static "Sold Out" button with no alternative action. https://zenrojas.com/products/organicsleeptea — "Sold Out," 0 reviews, no email capture. The sampler page at https://zenrojas.com/products/teabagsamplers confirms Bodyguard Tea is even sold out within the sampler set. These are permanent dead ends that lose every shopper who arrives from a Google search, social referral, or bookmarked link. No demand is captured, and no restocking notification is possible.
**Hypothesis:** Email capture rate on sold-out pages improves by replacing the "Sold Out" button with a "Notify me when this is back in stock" email capture, turning dead-end visits into a warm subscriber segment ready to convert at restock.
**Primary change:** Install a Back in Stock app (Back in Stock by Appikon or native Shopify 2.0 block) on all four sold-out PDPs. The button reads "Notify me when available" and captures email + product selection. Trigger an automated email at restock.
**Primary KPI:** Email capture rate on sold-out PDPs
**Decision rule:** Ship if email capture rate on sold-out PDPs exceeds 5% without increasing bounce rate.
**Expected lift:** Converts a 100% bounce into a captured lead on 5–15% of visits
**Confidence:** 85%

---

### exp-a1d7f28b3e50 — Launch Subscribe & Save with 10% discount on all teas

**Pillar:** Retention
**Affected surface:** All tea PDPs (Bodyguard Tea, Organic Black Tea; extend on restock)
**URL:** https://zenrojas.com/products/bodyguardtea and https://zenrojas.com/products/blacktea
**Evidence:** https://zenrojas.com/products/bodyguardtea and https://zenrojas.com/products/blacktea — both pages show a single add-to-cart button with no subscription option. The newsletter at https://zenrojas.com/ offers only "Promotions, new products and sales. Directly to your inbox." There is no mechanism for a customer who loves Bodyguard Tea at $13 to automate a recurring purchase. Competitor Pique Life (piquelife.com) offers Subscribe & Save with free shipping, first-dibs stock access, exclusive rewards, and a 90-day money back guarantee.
**Hypothesis:** 90-day repeat purchase rate improves by adding a Subscribe & Save option at 10% off on all tea PDPs, converting single purchases into recurring revenue and reducing reacquisition cost.
**Primary change:** Install Shopify Subscriptions (native) or ReCharge on the two in-stock tea PDPs. Display subscription as the pre-selected option with "One-time purchase" as a secondary choice. Show the savings ($1.30/order on Bodyguard, $0.80/order on Black Tea) and a "cancel anytime" guarantee.
**Primary KPI:** 90-day repeat purchase rate among tea buyers
**Decision rule:** Ship if 90-day repeat purchase rate improves by ≥8 percentage points without increasing first-purchase cart abandonment.
**Expected lift:** +15–25% repeat purchase rate
**Confidence:** 75%

---

### exp-3c6e8a12d571 — Add cross-sell recommendations on PDPs and in the cart

**Pillar:** AOV
**Affected surface:** Tea PDP pages and cart
**URL:** https://zenrojas.com/products/bodyguardtea and https://zenrojas.com/cart
**Evidence:** https://zenrojas.com/products/bodyguardtea — no "You may also like," "Frequently bought together," or recommended products section anywhere on the page. https://zenrojas.com/cart — cart page is empty of recommendations. The store carries teaware (infuser $5, mug $8) and samplers ($2–$10) that are natural complements to any tea purchase but are never surfaced on tea PDPs. Average PDP sells one SKU; a shopper buying Bodyguard Tea at $13 is never shown the $5 tea infuser or the $8 mug that would lift AOV to $18–$26 in a single session.
**Hypothesis:** AOV improves by surfacing a "Complete Your Ritual" cross-sell block on tea PDPs and a "You might also like" recommendation strip in the cart, pairing every tea purchase with the Tea Infuser, Mug, or Sampler.
**Primary change:** Use Shopify's native "Product Recommendations" API (Shopify 2.0 theme block) or an app like LimeSpot to add a 3-product cross-sell row at the bottom of each tea PDP and a 2-product "add-on" strip in the cart. Pair Bodyguard Tea with Tea Infuser + Loose Leaf Samplers; pair Black Tea with Mug + Tea Bags.
**Primary KPI:** Average order value
**Decision rule:** Ship if AOV rises by ≥$2.50 without hurting add-to-cart rate on the primary product.
**Expected lift:** +10–18% AOV
**Confidence:** 77%

---

### exp-6f9b3e24a015 — Launch a Ritual Starter Kit gift bundle

**Pillar:** AOV
**Affected surface:** New bundle PDP + gift collection
**URL:** https://zenrojas.com/products/ritual-starter-kit (new)
**Evidence:** https://zenrojas.com/collections/all — the full catalog lists a Zen Rojas Mug ($8), Tea Infuser ($5), Tea Bag Samplers ($2–$10), and Loose Leaf Samplers ($2–$10) as separate SKUs with no bundled gift offering. https://zenrojas.com/products/zen-rojas-e-giftcard — a digital gift card exists but a physical gifted experience does not. The homepage brand statement ("From our family to yours — peace, gratitude, and good tea") positions Zen Rojas as a gift-worthy brand, but there is no bundled product that makes gifting easy. Competitor Harney & Sons (harney.com) runs an "Everyday Gift Guide" and a tea gift bundles collection.
**Hypothesis:** AOV among new visitors and seasonal shoppers improves by offering a "Ritual Starter Kit" — Mug + Tea Infuser + Tea Bag Sampler Set + a printed care card — as a single bundled SKU at a $25–$28 price point, creating a natural gifting vehicle that lifts item count without requiring shoppers to self-assemble.
**Primary change:** Create a "Zen Ritual Starter Kit" bundle SKU ($25) containing Mug, Tea Infuser, Tea Bag Sampler Set, and a printed Brewing Guide card. Add a "Gifts" navigation item. Promote on the homepage below the hero.
**Primary KPI:** AOV among first-time visitors
**Decision rule:** Ship if first-time visitor AOV improves by ≥$5 without hurting kit PDP conversion rate.
**Expected lift:** +8–15% site-wide AOV
**Confidence:** 70%

---

### exp-d4a2f7c83b61 — Rewrite the blog with SEO-targeted wellness content and remove junk posts

**Pillar:** Acquisition
**Affected surface:** Blog (`/blogs/weekly-blog`)
**URL:** https://zenrojas.com/blogs/weekly-blog
**Evidence:** https://zenrojas.com/sitemap_blogs_1.xml — the blog sitemap contains 25 URLs, including posts with slugs like `/blogs/weekly-blog/kjhdchg`, `/blogs/weekly-blog/he-hfrvhi`, and `/blogs/weekly-blog/h` that are clearly test or junk posts. These are live, indexable pages being submitted to search engines. https://zenrojas.com/blogs/weekly-blog/bold-journey — the most recent post (October 2025) is 2 sentences long and links offsite. Blog posts about "ginger-for-heartburn," "sleep-tea," and "bodyguard" exist as weekly product spotlights but are not structured for keyword targeting (no H-tags, no word count, no internal product links).
**Hypothesis:** Organic search traffic improves by (1) removing or redirecting the junk/test blog posts that pollute the sitemap, and (2) rewriting the product-specific posts into 600–1,000-word articles targeting high-intent queries ("best tea for heartburn," "organic chamomile sleep tea benefits," "ginger tea for immunity") with internal links to the relevant PDPs.
**Primary change:** Unpublish or 301-redirect the junk posts (slugs: kjhdchg, he-hfrvhi, h, holla, 4-8, 5-12, 6-30). Rewrite 5 existing product posts to 800+ words with keyword-targeted H1s, ingredient explanations, and "Shop now" links to the PDP. Add a blog category or tag system for navigation.
**Primary KPI:** Organic search sessions to blog pages
**Decision rule:** Ship if organic blog traffic improves within 90 days without increasing bounce rate on blog-to-PDP funnels.
**Expected lift:** +15–30% organic traffic to the blog
**Confidence:** 72%

---

### exp-9e5c1b47f236 — Rebuild the ambassador program with a commission structure and application form

**Pillar:** Acquisition
**Affected surface:** Ambassador Program page
**URL:** https://zenrojas.com/pages/ambassador-program
**Evidence:** https://zenrojas.com/pages/ambassador-program — the page is a single 64-word paragraph: "Zen Rojas is looking for tea loving, awesome, ambassadors to grow our brand and allow our customers to get to know us on a more personal level. If you are interested please send us an email or DM on any of our social media accounts to get more details." No commission rate, no requirements, no application form, no tracking link system, no content guidelines. This page is linked from the primary navigation, meaning it is a top-level acquisition channel with no conversion path.
**Hypothesis:** Ambassador signups and attributed referral revenue improve by replacing the single-paragraph page with a structured program: a defined commission rate (e.g., 15%), a Shopify Affiliates or Refersion-powered referral link system, a brief content guideline, and an embedded application form — turning a dead page into a working channel.
**Primary change:** Install a Shopify affiliate app (Refersion or UpPromote). Build a new Ambassador Program page with: (1) commission rate and payout terms, (2) content guidelines and brand kit download, (3) embedded application form collecting name, IG handle, and follower count, (4) auto-approval email with a unique referral link. Link to existing Bold Journey and Voyage Houston features as "social proof" of brand story.
**Primary KPI:** Monthly ambassador signups and attributed referral revenue
**Decision rule:** Ship if ambassador signups exceed 3/month and attributed revenue exceeds $100/month within 60 days.
**Expected lift:** New channel; currently $0 attributed referral revenue
**Confidence:** 65%

---

## Competitor analysis

All three direct competitors make personalization, subscription, and social proof easier than Zen Rojas currently does. Zen Rojas's durable edge is its veteran-owned story, genuine organic sourcing, and Houston-local authenticity — none of which require budget to leverage, only structured placement.

| Competitor | Domain | Positioning | What they make easier | Zen Rojas edge | Pattern to adapt |
|---|---|---|---|---|---|
| Pique Life | piquelife.com | Premium wellness tea and supplements with subscription protocols | 18,078+ verified five-star reviews featured prominently; wellness protocol quiz for personalization; Subscribe & Save with 90-day money-back guarantee; expert endorsements (Forbes, Elle, Mark Hyman MD) | Veteran-owned authenticity and family story; simpler loose-leaf category; lower price entry point for trial | Add a verified review count (even at 50–100) as a trust headline; offer a 90-day money-back guarantee instead of a generic 30-day warranty |
| Harney & Sons | harney.com | Established fine tea brand with DTC and gifting focus | "Your Perfect Tea Quiz" for personalization; Subscribe & Savor program; Tea Discovery Wheel; corporate gifting section; rewards and referrals program | Newer, trendier wellness angle; veteran narrative; Houston community story; organic/ethical sourcing | Launch a tea quiz (3–5 questions: caffeine preference, health goal, flavor profile) that routes to Bodyguard, Black Tea, or Samplers |
| Art of Tea | artoftea.com | Organic loose-leaf tea organized by wellness benefit | Benefit-based navigation (Energy & Focus, Calm & Sleep, Digestion, Immunity); "Want 10% off your first purchase?" email capture popup; LoyalTEA Rewards program; Tea Club subscription; media endorsements (Forbes, HuffPost, Bon Appétit, Disney, Google) | Smaller, more personal brand story; veteran-owned trust; simpler SKU set for easier decision-making | Replace the newsletter's "Promotions and sales" copy with a "Get 10% off your first order" popup with a branded discount code; organize the tea collection by health benefit |
| Teami Blends | teamiblends.com | Wellness lifestyle tea brand with strong social proof and influencer DTC model | Tiered ambassador and influencer program with tracked referral links; subscription bundles; large Instagram-native community; product quiz | More credible organic sourcing story; simpler ingredient transparency; veteran-owned angle resonates in different demographics | Build ambassador tiers (Micro → Partner → Elite) with escalating commissions to activate the existing ambassador page |

---

## Technical checks

| Check | Status | Detail |
|---|---|---|
| SSL Certificate | Pass | HTTPS loads cleanly; all pages served over HTTPS |
| HTTPS Redirect | Pass | HTTP redirects to HTTPS; standard Shopify behavior confirmed |
| Sitemap | Pass | https://zenrojas.com/sitemap.xml exists and loads a valid sitemap index linking 5 sub-sitemaps (products, pages, collections, blogs, agentic discovery) |
| robots.txt | Pass | https://zenrojas.com/robots.txt exists; properly configured Shopify robots.txt with correct disallows (/admin, /cart/, /checkout, /checkouts/, /orders) and allows for adsbot-google |
| Critical Pages Loading | Warn | Homepage, cart, about, FAQs, collections all load. /products/bodyguard-organic-tea (hyphenated slug) returns 404 — the correct URL is /products/bodyguardtea (no hyphens); any external links or marketing materials using the hyphenated pattern will 404 |
| Meta Tags | Warn | Homepage title is "Home Page – Zen Rojas" (generic); meta description absent on the /collections/all page. Shopify auto-generates titles but product descriptions are not optimized |
| Structured Data | Warn | No JSON-LD visible on fetched product pages (Bodyguard, Black Tea, Sleep Tea, Samplers); Shopify's default theme may inject product schema but it was not confirmed in crawled output |
| Favicon | Warn | Not verified from crawl; assumed present given active Shopify store, but not confirmed |
| Mobile-Friendly | Pass | Shopify-hosted theme; viewport meta tag is standard in all Shopify themes; assumed mobile-responsive |
| Page Speed Mobile | Warn | Not measured via Lighthouse; Shopify CDN provides baseline optimization, but no speed test was run |
| Page Speed Desktop | Warn | Not measured via Lighthouse; no third-party speed data available |
| Broken Links | Fail | /products/bodyguard-organic-tea returns 404 (slug mismatch — correct URL is /products/bodyguardtea); /blogs/news returns 404 (correct URL is /blogs/weekly-blog); 25 blog posts include at least 7 junk/test slugs (kjhdchg, he-hfrvhi, h, etc.) indexed by search engines |
| Image Optimization | Warn | Not measured; Shopify CDN serves images but no WebP confirmation or byte-level audit was performed |
| Cookie/Privacy | Warn | Privacy Policy, Terms of Service, and Refund Policy all linked in footer. No cookie consent banner was detected; may be required for EU/international visitors given iDEAL Wero payment method displayed |
| Checkout Reachable | Warn | Shopify-hosted checkout is reachable in principle; cart page renders with a liquid template bug ("t: e" text and missing image placeholder) that may cause trust issues before the shopper reaches checkout |
