---
title: "Archive"
description: "A visual month-by-month archive of all MorDictionary posts."
---
/* Tumblr-like archive grid */
.tumblr-archive { max-width: 1100px; margin: 0 auto; }
.ta-month { margin: 2rem 0 1rem; font-size: 1.25rem; opacity: .9; }

.ta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 12px;
}

.ta-tile { display: block; border-radius: 12px; overflow: hidden; position: relative; }
.ta-tile img {
  width: 100%; height: 100%; aspect-ratio: 1 / 1;
  object-fit: cover; display: block;
  transition: transform .25s ease, filter .25s ease;
}
.ta-tile:hover img { transform: scale(1.03); filter: brightness(1.06); }
