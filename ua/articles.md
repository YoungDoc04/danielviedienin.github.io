---
layout: page
lang: ua
nav: blog
permalink: /ua/articles/
title: "ДВ | Статті"
description: "Глибокі розбори екстреної медицини, ШІ та HealthTech."
---

## Статті

Довгі пости (1500–3000 слів) — глибокі розбори, аналіз проблем, висновки. Те, що потребує часу та уваги.

[← Усі пости](/ua/blog/)

---

{% assign lang_posts = site.posts | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_posts %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_posts.size == 0 %}
  <li class="empty">Поки що немає статей.</li>
{% endif %}
</ul>
