---
title: "Archive"
description: "A visual month-by-month archive of all MorDictionary posts."
---

<div class="tumblr-archive">
  <h2 class="ta-month">All Posts</h2>
  <div class="ta-grid">
    {{ range .Site.RegularPages }}
      <a href="{{ .Permalink }}" class="ta-tile">
        {{ with .Params.cover }}
          <img src="{{ . }}" alt="{{ $.Title }}">
        {{ end }}
      </a>
    {{ end }}
  </div>
</div>