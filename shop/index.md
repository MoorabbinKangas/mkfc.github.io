---
layout: default
title: Shop
permalink: /shop/
description: "Moorabbin Kangaroos FC merchandise — caps, scarves, beanies, apparel and more. Buy at the club or order online from our partners. Print or save as PDF."
---

<style>
.shop-page {
  max-width: 960px;
  margin: 0 auto;
  padding-bottom: 2rem;
  font-family: "DIN", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.shop-page h1,
.shop-page h2,
.shop-page h3 {
  font-family: "DIN Condensed", "Helvetica Neue Condensed", "HelveticaNeue-CondensedBold", "Arial Narrow", sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  font-weight: 700;
}

.shop-intro {
  text-align: center;
  margin-bottom: 1.25rem;
}

.shop-intro h1 {
  margin-bottom: 0.5rem;
}

.shop-intro p {
  color: #555;
  margin: 0 auto;
  max-width: 640px;
}

.shop-print-actions {
  text-align: center;
  margin: 1rem 0 2rem;
}

.shop-print-button {
  display: inline-block;
  background-color: #013087;
  color: #fff !important;
  padding: 0.6rem 1.4rem;
  border-radius: 4px;
  font-weight: 700;
  text-decoration: none !important;
  font-size: 0.95rem;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.shop-print-button:hover {
  background-color: #001a5e;
}

.shop-section {
  margin-bottom: 2.25rem;
}

.shop-section-heading {
  text-align: center;
  margin: 0 0 0.4rem;
  color: #013087;
  border-bottom: 2px solid #C8D6F0;
  padding-bottom: 0.5rem;
}

.shop-section-blurb {
  text-align: center;
  color: #666;
  font-size: 0.9rem;
  margin: 0 auto 1.25rem;
  max-width: 620px;
}

.shop-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 1.25rem;
}

.shop-item {
  border: 1px solid #C8D6F0;
  border-radius: 8px;
  background: #fff;
  overflow: hidden;
  break-inside: avoid;
  page-break-inside: avoid;
  display: flex;
  flex-direction: column;
}

.shop-item-photo {
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #eef1f8;
  overflow: hidden;
}

.shop-item-photo img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  display: block;
}

.shop-item-photo--placeholder {
  background: #C8D6F0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.shop-item-photo--placeholder img {
  width: 58%;
  opacity: 0.55;
}

.shop-item-body {
  padding: 0.85rem 0.9rem 1rem;
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
}

.shop-item-name {
  margin: 0 0 0.25rem;
  font-size: 1.1rem;
  color: #013087;
}

.shop-item-desc {
  color: #555;
  font-size: 0.85rem;
  margin: 0 0 0.75rem;
  line-height: 1.35;
}

.shop-item-price {
  margin-top: auto;
  font-weight: 700;
  font-size: 1.25rem;
  color: #013087;
  font-family: "DIN Condensed", "Helvetica Neue Condensed", "Arial Narrow", sans-serif;
  letter-spacing: 0.02em;
}

.shop-item-fulfilment {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  margin: 0.35rem 0 0;
  font-size: 0.78rem;
  font-weight: 600;
  color: #013087;
}

.shop-item-fulfilment svg {
  width: 13px;
  height: 13px;
  flex: 0 0 auto;
  fill: #013087;
}

.shop-item-vendor {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px dashed #C8D6F0;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.shop-item-qr {
  width: 78px;
  height: 78px;
  flex: 0 0 auto;
  background: #fff;
  padding: 4px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.shop-item-qr svg {
  width: 100%;
  height: 100%;
  display: block;
}

.shop-item-vendor-info {
  min-width: 0;
}

.shop-item-vendor-label {
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #888;
  margin: 0;
}

.shop-item-vendor-name {
  font-weight: 700;
  color: #013087;
  font-size: 0.9rem;
  margin: 0 0 0.15rem;
}

.shop-item-vendor-url {
  font-size: 0.72rem;
  word-break: break-all;
  line-height: 1.3;
}

.shop-item-vendor-url a,
.shop-item-vendor-url a:visited {
  color: #666;
  text-decoration: none;
}

.shop-item-vendor-url a:hover {
  text-decoration: underline;
}

.shop-item-vendor-soon {
  color: #999;
  font-size: 0.8rem;
  font-style: italic;
}

.shop-footer-note {
  text-align: center;
  color: #777;
  font-size: 0.85rem;
  margin-top: 2rem;
}

/* Print styles — clean colour output for PDF export / A4 display print */
@media print {
  .site-header,
  .site-footer,
  .site-nav,
  .shop-print-actions {
    display: none !important;
  }

  body {
    background: #fff !important;
    color: #000;
    font-size: 9pt;
  }

  .page-content {
    padding: 0 !important;
  }

  .wrapper {
    max-width: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .shop-page {
    max-width: none !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .shop-intro {
    margin-bottom: 0.5rem;
  }

  .shop-intro h1 {
    font-size: 18pt;
    margin: 0 0 0.2rem;
  }

  .shop-intro p {
    color: #333 !important;
    font-size: 9pt;
  }

  .shop-section {
    margin-bottom: 0.9rem;
  }

  .shop-section-heading {
    font-size: 12pt;
    margin: 0 0 0.3rem;
    padding-bottom: 0.25rem;
  }

  .shop-section-blurb {
    font-size: 8pt;
    margin-bottom: 0.6rem;
  }

  .shop-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 0.5rem;
  }

  .shop-item {
    page-break-inside: avoid;
    break-inside: avoid;
    border: 1px solid #888;
  }

  .shop-item-photo {
    aspect-ratio: 16 / 10;
  }

  .shop-item-body {
    padding: 0.45rem 0.5rem 0.55rem;
  }

  .shop-item-name {
    font-size: 10pt;
  }

  .shop-item-desc {
    font-size: 7.5pt;
    margin-bottom: 0.4rem;
    color: #333 !important;
  }

  .shop-item-price {
    font-size: 12pt;
  }

  .shop-item-fulfilment {
    font-size: 7pt;
    margin-top: 0.2rem;
  }

  .shop-item-fulfilment svg {
    width: 9px;
    height: 9px;
  }

  .shop-item-vendor {
    margin-top: 0.4rem;
    padding-top: 0.4rem;
    gap: 0.45rem;
  }

  .shop-item-qr {
    width: 60px;
    height: 60px;
    padding: 2px;
  }

  .shop-item-vendor-name {
    font-size: 8pt;
  }

  .shop-item-vendor-label,
  .shop-item-vendor-url {
    font-size: 6.5pt;
  }

  .shop-item-vendor-url a {
    color: #333 !important;
  }

  .shop-footer-note {
    font-size: 7.5pt;
    margin-top: 0.8rem;
  }

  @page {
    margin: 10mm;
    size: A4;
  }

  h1, h2, h3 {
    page-break-after: avoid;
  }
}
</style>

<div class="shop-page">

<div class="shop-intro">
<h1>Moorabbin Kangaroos Shop</h1>
<p>Show your colours! Buy club gear on game day, or scan an item's code to pay online securely with Square. Selected lines are also available from our partners. Print this page or save it as a PDF for the merchandise table.</p>
</div>

<div class="shop-print-actions">
  <button type="button" class="shop-print-button" onclick="window.print()">Print or Save as PDF</button>
</div>

{% for category in site.data.shop.categories %}
<div class="shop-section">

<h2 class="shop-section-heading">{{ category.name }}</h2>
{% if category.blurb %}<p class="shop-section-blurb">{{ category.blurb }}</p>{% endif %}

<div class="shop-grid">
{% for item in category.items %}
  <div class="shop-item">
    {% if item.image and item.image != "" %}
    <div class="shop-item-photo">
      <img src="{{ item.image }}" alt="{{ item.name | escape }}" loading="lazy">
    </div>
    {% else %}
    <div class="shop-item-photo shop-item-photo--placeholder">
      <img src="/mkfc-logo-large-no-text.png" alt="" loading="lazy">
    </div>
    {% endif %}
    <div class="shop-item-body">
      <h3 class="shop-item-name">{{ item.name }}</h3>
      {% if item.description %}<p class="shop-item-desc">{{ item.description }}</p>{% endif %}
      <div class="shop-item-price">{{ item.price }}</div>
      {% if item.fulfilment %}
      <p class="shop-item-fulfilment">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>
        {% case item.fulfilment %}{% when "pickup" %}Collect at the club{% when "post" %}Posted to you{% else %}{{ item.fulfilment }}{% endcase %}
      </p>
      {% endif %}
      {% if item.url and item.url != "" and item.url != "#" %}
      <div class="shop-item-vendor">
        <div class="shop-item-qr" data-qr="{{ item.url }}"></div>
        <div class="shop-item-vendor-info">
          {% if item.vendor %}<p class="shop-item-vendor-label">Order from</p><p class="shop-item-vendor-name">{{ item.vendor }}</p>{% else %}<p class="shop-item-vendor-label">Scan to buy</p><p class="shop-item-vendor-name">Secure payment by Square</p>{% endif %}
          <div class="shop-item-vendor-url"><a href="{{ item.url }}">{{ item.url | remove: "https://" | remove: "http://" | remove_first: "www." }}</a></div>
        </div>
      </div>
      {% elsif item.vendor %}
      <div class="shop-item-vendor">
        <div class="shop-item-vendor-info">
          <p class="shop-item-vendor-label">Available from</p>
          <p class="shop-item-vendor-name">{{ item.vendor }}</p>
          <div class="shop-item-vendor-soon">Online link coming soon</div>
        </div>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

</div>
{% endfor %}

<p class="shop-footer-note">{{ site.data.shop.note }}<br>Moorabbin Kangaroos Football Club &middot; Widdop Crescent Oval, Hampton East VIC 3188 &middot; <a href="https://www.mkfc.org.au">www.mkfc.org.au</a></p>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
<script>
(function() {
  function renderQRs() {
    if (typeof qrcode !== 'function') return;
    document.querySelectorAll('[data-qr]').forEach(function(el) {
      if (el.dataset.qrRendered === '1') return;
      var url = el.getAttribute('data-qr');
      if (!url) return;
      var qr = qrcode(0, 'M');
      qr.addData(url);
      qr.make();
      el.innerHTML = qr.createSvgTag({ cellSize: 4, margin: 0, scalable: true });
      var svg = el.querySelector('svg');
      if (svg) {
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.style.width = '100%';
        svg.style.height = '100%';
      }
      el.dataset.qrRendered = '1';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderQRs);
  } else {
    renderQRs();
  }
})();
</script>
