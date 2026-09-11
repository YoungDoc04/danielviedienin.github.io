---
layout: page
lang: en
nav: blog
permalink: /en/notes/
title: "DV | Notes"
description: "Quick field notes on emergency medicine, AI, and HealthTech."
---

## Notes

Short posts (300–500 words) — quick observations, ideas, links. Things that don't need a long text but can be useful.

[← All posts](/en/blog/)

---

{% assign lang_notes = site.notes | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_notes %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_notes.size == 0 %}
  <li class="empty">No notes published yet.</li>
{% endif %}
</ul>
