---
layout: default
title: Gallery
description: "Match-day and club event photos from the Moorabbin Kangaroos Football Club."
---

# Photo Gallery

Match-day and club event photos from the Moorabbin Kangaroos. Select an album below to view the photos.

{% assign cdn_base = "https://cdn.jsdelivr.net/gh/MoorabbinKangas/media@main/gallery/" %}

{% if site.data.gallery.albums.size > 0 %}
<div class="photo-gallery">
  {% for album in site.data.gallery.albums %}
  <figure class="gallery-item">
    <a href="{{ '/gallery/' | append: album.slug | append: '/' | relative_url }}">
      <img src="{{ cdn_base }}{{ album.slug }}/{{ album.photos.first }}" alt="{{ album.name }} cover photo" loading="lazy">
      <figcaption>{{ album.name }} ({{ album.photos.size }} photos)</figcaption>
    </a>
  </figure>
  {% endfor %}
</div>
{% else %}
<div class="photo-gallery">
  <p class="gallery-placeholder">Photos coming soon! Follow us on
  <a href="https://www.facebook.com/MoorabbinKangas">Facebook</a>
  and <a href="https://www.instagram.com/moorabbinkangas">Instagram</a>
  for the latest match-day photos.</p>
</div>
{% endif %}

More photos on [Facebook](https://www.facebook.com/MoorabbinKangas) and [Instagram](https://www.instagram.com/moorabbinkangas).
