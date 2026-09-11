---
layout: page
lang: en
nav: blog
permalink: /en/articles/
title: "DV | Articles"
description: "Deep dives on emergency medicine, AI, and HealthTech."
---

## Articles

Long posts (1500–3000 words) — deep dives, problem analysis, conclusions. Things that require time and attention.

[← All posts](/en/blog/)

---

{% assign lang_posts = site.posts | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_posts %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_posts.size == 0 %}
  <li class="empty">No articles published yet.</li>
{% endif %}
</ul>
