---
layout: page
lang: en
nav: blog
permalink: /en/blog/
title: "DV | Blog"
description: "Emergency medicine, AI in practice, and HealthTech — notes and articles from Daniel Viedienin."
---

## Blog

Here I write about what I see every day: emergency medicine, AI in practice, HealthTech, and everything in between. Short notes from shifts, long case analyses, thoughts on how technology changes the doctor's work.

### Notes

Short posts (300–500 words) — quick observations, ideas, links. Things that don't need a long text but can be useful.

[See notes →](/en/notes/)

### Articles

Long posts (1500–3000 words) — deep dives, problem analysis, conclusions. Things that require time and attention.

[See articles →](/en/articles/)

---

### All posts

{% assign lang_posts = site.posts | where: "lang", page.lang %}
{% assign lang_notes = site.notes | where: "lang", page.lang %}
{% assign all_items = lang_posts | concat: lang_notes | sort: "date" | reverse %}
<ul class="post-list">
{% for item in all_items %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if all_items.size == 0 %}
  <li class="empty">Nothing published yet — check back soon.</li>
{% endif %}
</ul>
