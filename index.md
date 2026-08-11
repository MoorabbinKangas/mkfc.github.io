---
layout: default
title: Home
description: "Moorabbin Kangaroos Football Club — SFNL Division 4, Hampton East. Training, fixtures, and how to join."
---

<div class="hero">
  <video class="hero-bg-video hero-bg-video-desktop" autoplay muted loop playsinline preload="auto" poster="/assets/img/hero-poster-desktop.jpg">
    <source src="/videos/mkfc-clip2-2026-08-11.mp4" type="video/mp4">
  </video>
  <video class="hero-bg-video hero-bg-video-mobile" autoplay muted loop playsinline preload="auto" poster="/assets/img/hero-poster-mobile.jpg">
    <source src="/videos/mkfc-clip-2026-08-11.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay"></div>
  <div class="hero-inner">
    <img src="/logo-2025.jpg" alt="Moorabbin Kangaroos Logo" class="hero-logo">
    <h1>Moorabbin Kangaroos Football Club</h1>
    <p class="hero-tagline">Est. 1965 — SFNL Division 4 — Hampton East, Melbourne</p>
    <div class="hero-buttons">
      <a href="/welcome/" class="cta-button">New Players Welcome</a>
      <a href="/contact/" class="cta-button-outline">Contact Us</a>
    </div>
  </div>
</div>

{% assign today = "now" | date: "%Y-%m-%d" %}
{% assign next_match = nil %}
{% for game in site.data.fixtures.games %}
  {% assign game_date = game.date | date: "%Y-%m-%d" %}
  {% if game_date >= today and next_match == nil %}
    {% assign next_match = game %}
  {% endif %}
{% endfor %}

<section class="section section-light">
  <div class="section-inner">
    {% if next_match %}
    <div class="next-match-card">
      <span class="next-match-label">Next Match</span>
      <p class="next-match-meta">Round {{ next_match.round }} &middot; {{ next_match.date | date: "%a %-d %b" }}</p>
      <p class="next-match-teams">
        <span class="next-match-mkfc">MKFC</span>
        <span class="next-match-vs">vs</span>
        <span class="next-match-opponent">{{ next_match.opponent }}</span>
      </p>
      <p class="next-match-tag-row"><span class="next-match-tag next-match-tag-{{ next_match.home_away | downcase }}">{{ next_match.home_away | upcase }}</span></p>
      <p class="next-match-venue">{{ next_match.venue }}</p>
      <p class="next-match-times">Reserves 12:00pm &middot; Seniors 2:00pm</p>
      <p class="next-match-actions">
        <a class="next-match-btn" href="https://www.google.com/maps/search/?api=1&amp;query={{ next_match.venue | url_encode }}" target="_blank" rel="noopener">Directions</a>
        <a class="next-match-btn next-match-btn-outline" href="/calendar/">Full Fixtures</a>
      </p>
    </div>
    {% endif %}
    <div class="info-cards">
      <div class="info-card">
        <h3>Training</h3>
        <p><strong>Tuesday &amp; Thursday</strong><br>6:00pm - 8:00pm<br>Widdop Crescent Oval, Hampton East</p>
      </div>
      <div class="info-card">
        <h3>Find Us</h3>
        <p>Widdop Crescent Oval<br>41 Widdop Crescent<br>Hampton East 3188<br><a href="https://maps.app.goo.gl/EqwponkRzfhLmvSZ6">View on Google Maps</a></p>
      </div>
      <div class="info-card">
        <h3>Season 2026</h3>
        <p>Two teams competing in SFNL Division 4<br><a href="/calendar/">View Fixtures</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-navy" markdown="1">
<div class="section-inner" markdown="1">

## About Our Club

The Moorabbin Kangaroos Football Club has been part of the local community since 1965, providing opportunities for players to compete at a high level while fostering teamwork and sportsmanship.

We currently field two teams in the **Southern Football and Netball League**:

1. Senior Men's Team
2. Reserves Team

We welcome players of all experience levels — [find out more about joining](/welcome/).

</div>
</section>

<section class="section section-mid">
  <div class="section-inner">
    {% include mailchimp_signup.html
       variant="navy"
       heading="Stay Connected"
       intro="Get club news, fixtures, and event updates delivered straight to your inbox." %}
  </div>
</section>

<section class="section section-light" markdown="1">
<div class="section-inner" markdown="1">

## Quick Links

- [Our Sponsors](/sponsors)
- [Latest News](/news)
- [Club History](/about/#club-history)
- [Club Documents](/documents/)

</div>
</section>
