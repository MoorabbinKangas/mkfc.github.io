# Auto-posting gallery photos to Facebook & Instagram

The website now publishes an RSS feed of new photo albums at:

```
https://www.mkfc.org.au/gallery/feed.xml
```

Every time a new album is added to the Gallery (e.g. a new home-game photo set), the feed gets one new entry containing:

- The album name and photo count
- A link to the full album on the site
- The album's cover photo (as both an `<enclosure>` and `<media:content>` image — the two formats most automation tools look for)

This lets a social media scheduling tool "watch" the feed and turn each new album into a draft (or auto-published) Facebook/Instagram post, instead of someone manually downloading and re-uploading photos.

**Important:** the feed publishes one post per *album*, not one per photo — it's meant to announce "new photos are up" and link back to the gallery, not to flood Facebook/Instagram with 100 individual images every time. If you want to post a handful of standout shots individually, do that manually as before.

## Recommended tool: Zapier or Make.com

Both have a free tier and support this exact pattern: RSS trigger → social post action.

1. **Trigger:** "New Item in Feed" (Zapier's built-in RSS app, or Make's RSS module). Point it at `https://www.mkfc.org.au/gallery/feed.xml`.
2. **Action — Facebook:** "Create Page Post" (Facebook Pages app). Map the post text to the feed item's title/description, and the image to the enclosure/`media:content` URL.
3. **Action — Instagram (optional):** "Upload Photo" (Instagram for Business app). Map the image URL and a caption.

Notes:
- Instagram posting requires the club's Instagram account to be a **Business or Creator account linked to the Facebook Page** — Meta doesn't allow automated posting to personal accounts. This is a one-time setup in the Instagram app (Settings → Account type) plus linking it to the Facebook Page in Meta Business Suite.
- The Facebook/Instagram integrations are usually "Premium" apps on Zapier's free plan, which caps you at a small number of tasks/month — fine for a few new albums a month, but check current Zapier pricing if the club posts more often.
- Both tools support **draft/review mode** if you'd rather approve each post before it goes live — recommended at first, so someone can tweak the caption before it's public.

## Simpler alternative: IFTTT

IFTTT's free tier has an "RSS Feed" trigger and a "Facebook Pages" action, with a similar but more limited applet model (one feed → one action, no per-post editing). Good enough if you only need Facebook and don't want to set up Zapier/Make.

## No automation, just a bookmark

If it's easier to just check in on the feed and post manually, any RSS reader app (Feedly, Inoreader, or even the browser) can subscribe to the feed URL above and notify you when a new album goes up — you still do the actual posting.

## Testing the feed

Paste `https://www.mkfc.org.au/gallery/feed.xml` into a feed validator like https://validator.w3.org/feed/ to confirm it's readable before wiring up an automation — this is also the quickest way to check a new album shows up correctly after it's published.
