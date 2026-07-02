---
layout: default
title: Subscriptions
permalink: /subscriptions/
description: "Moorabbin Kangaroos FC season subscriptions — player and social memberships for 2026. Pay securely online via Square or scan a QR code."
---

<style>
.sub-page {
  font-family: "DIN", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.sub-intro {
  text-align: center;
}

.sub-intro img {
  max-width: 360px;
  width: 90%;
  height: auto;
  margin-bottom: 1rem;
}

.sub-intro p {
  max-width: 620px;
  margin: 0.75rem auto 0;
  color: #444;
}

.sub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
}

.sub-card {
  background: #fff;
  text-align: center;
}

.sub-card h3 {
  border-bottom: none;
  padding-bottom: 0;
  margin-bottom: 0.25rem;
}

.sub-price {
  font-size: 1.6rem;
  font-weight: 700;
  color: #013087;
  font-family: "DIN Condensed", "Helvetica Neue Condensed", "Arial Narrow", sans-serif;
  margin: 0 0 0.75rem;
}

.sub-desc {
  color: #555;
  font-size: 0.9rem;
  margin: 0 0 1rem;
  flex: 1 1 auto;
}

.sub-qr {
  width: 130px;
  height: 130px;
  margin: 0 auto 1rem;
  background: #fff;
  padding: 6px;
  border: 1px solid #C8D6F0;
  border-radius: 6px;
}

.sub-qr svg {
  width: 100%;
  height: 100%;
  display: block;
}

.sub-button {
  display: inline-block;
  background-color: #013087;
  color: #fff !important;
  padding: 0.6rem 1.4rem;
  border-radius: 4px;
  font-weight: 700;
  text-decoration: none !important;
  font-size: 0.95rem;
}

.sub-button:hover {
  background-color: #001a5e;
}
</style>

<div class="sub-page">

<div class="section section-light">
  <div class="section-inner sub-intro">
    <img src="/assets/merchandise/moorabbin_kangas_blue_split_noborder-short.png" alt="Moorabbin Kangaroos">
    <h1>Subscriptions</h1>
    <p>Join the Moorabbin Kangaroos for the 2026 season. Choose a membership below, then pay securely online via Square — either follow the link or scan the QR code with your phone camera.</p>
  </div>
</div>

<div class="section" id="memberships" markdown="1">
<div class="section-inner" markdown="1">

## Membership Options

<div class="sub-grid">

<div class="info-card sub-card">
  <h3>Season Player Subscription (Full/Working)</h3>
  <p class="sub-price">$400.00</p>
  <p class="sub-desc">Full season playing membership.</p>
  <div class="sub-qr" data-qr="https://square.link/u/qOgYiqsJ?src=webqr"></div>
  <a href="https://square.link/u/qOgYiqsJ?src=webqr" class="sub-button">Subscribe Now</a>
</div>

<div class="info-card sub-card">
  <h3>Season Player Subscription (Concession)</h3>
  <p class="sub-price">$200.00</p>
  <p class="sub-desc">Concession-rate season playing membership.</p>
  <div class="sub-qr" data-qr="https://square.link/u/HVK3vZgW?src=webqr"></div>
  <a href="https://square.link/u/HVK3vZgW?src=webqr" class="sub-button">Subscribe Now</a>
</div>

<div class="info-card sub-card">
  <h3>Season Player Subscription (Part-payment)</h3>
  <p class="sub-price">$30.00</p>
  <p class="sub-desc">Make a partial payment towards your season subscription. Use this link as many times as needed to pay off your total.</p>
  <div class="sub-qr" data-qr="https://square.link/u/yoSZcY2R?src=webqr"></div>
  <a href="https://square.link/u/yoSZcY2R?src=webqr" class="sub-button">Make a Payment</a>
</div>

<div class="info-card sub-card">
  <h3>Season Social Membership</h3>
  <p class="sub-price">$60.00</p>
  <p class="sub-desc">Non-playing social membership — support the club and enjoy member benefits.</p>
  <div class="sub-qr" data-qr="https://square.link/u/HzOHr3Mu?src=webqr"></div>
  <a href="https://square.link/u/HzOHr3Mu?src=webqr" class="sub-button">Subscribe Now</a>
</div>

</div>

</div>
</div>

<div class="section section-light" markdown="1">
<div class="section-inner" markdown="1">

## Questions?

If you'd rather subscribe in person, subscriptions can also be paid at the club. For any questions about memberships, get in touch via our [Contact page](/contact).

</div>
</div>

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
