---
layout: default
title: Events
permalink: /shop/events/
description: "Moorabbin Kangaroos FC events — social events, raffles and more for 2026. Pay securely online via Square or scan a QR code."
---

<style>
.events-page {
  font-family: "DIN", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.events-intro {
  text-align: center;
}

.events-intro img {
  max-width: 360px;
  width: 90%;
  height: auto;
  margin-bottom: 1rem;
}

.events-intro p {
  max-width: 620px;
  margin: 0.75rem auto 0;
  color: #444;
}

.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.25rem;
  max-width: 720px;
  margin: 0 auto;
}

.event-item {
  border: 1px solid #C8D6F0;
  border-radius: 8px;
  background: #fff;
  padding: 1.25rem 1.25rem 1.5rem;
  text-align: center;
}

.event-item h3 {
  margin: 0 0 0.35rem;
  color: #013087;
}

.event-item-meta {
  color: #555;
  font-size: 0.9rem;
  margin: 0 0 1rem;
}

.event-item-qr {
  width: 140px;
  height: 140px;
  margin: 0 auto 0.75rem;
  background: #fff;
  padding: 6px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
}

.event-item-qr svg {
  width: 100%;
  height: 100%;
  display: block;
}

.event-item-links a {
  display: inline-block;
  margin: 0.15rem 0.4rem;
}
</style>

<div class="events-page">

<div class="section section-light">
  <div class="section-inner events-intro">
    <img src="/assets/merchandise/moorabbin_kangas_blue_split_noborder-short.png" alt="Moorabbin Kangaroos">
    <h1>Events</h1>
    <p>Social events, raffles and more from the Moorabbin Kangaroos. Pay securely online via Square or scan a QR code.</p>
  </div>
</div>

<div class="section section-light" markdown="1">
<div class="section-inner" markdown="1">

<div class="events-grid">
  <div class="event-item">
    <h3>$5,000 Major Raffle</h3>
    <p class="event-item-meta">Tickets $50 each<br>Drawn Saturday 8 August, Widdop Reserve</p>
    <div class="event-item-qr" data-qr="https://square.link/u/VXXeLlbn"></div>
    <div class="event-item-links">
      <a href="https://square.link/u/VXXeLlbn" class="cta-button">Buy Tickets</a><br>
      <a href="/raffle/">Full raffle details</a>
    </div>
  </div>
</div>

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
