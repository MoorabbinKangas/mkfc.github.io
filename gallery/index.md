---
layout: default
title: Gallery
description: "Match-day and club event photos from the Moorabbin Kangaroos Football Club."
---

# Photo Gallery

Match-day and club event photos from the Moorabbin Kangaroos. Click any photo to view it full size.

{% assign cdn_base = "https://cdn.jsdelivr.net/gh/MoorabbinKangas/media@main/gallery/" %}

{% if site.data.gallery.albums.size > 0 %}
  {% for album in site.data.gallery.albums %}
<h2>{{ album.name }}</h2>

<div class="photo-gallery">
  {% for photo in album.photos %}
  <figure class="gallery-item">
    <a href="{{ cdn_base }}{{ album.slug }}/{{ photo }}" target="_blank" rel="noopener">
      <img src="{{ cdn_base }}{{ album.slug }}/{{ photo }}" alt="{{ album.name }} photo" loading="lazy">
    </a>
  </figure>
  {% endfor %}
</div>
  {% endfor %}
{% else %}
<div class="photo-gallery">
  <p class="gallery-placeholder">Photos coming soon! Follow us on
  <a href="https://www.facebook.com/MoorabbinKangas">Facebook</a>
  and <a href="https://www.instagram.com/moorabbinkangas">Instagram</a>
  for the latest match-day photos.</p>
</div>
{% endif %}

More photos on [Facebook](https://www.facebook.com/MoorabbinKangas) and [Instagram](https://www.instagram.com/moorabbinkangas).
