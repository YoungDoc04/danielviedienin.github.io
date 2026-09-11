---
layout: page
lang: ru
nav: blog
permalink: /ru/articles/
title: "ДВ | Статьи"
description: "Глубокие разборы экстренной медицины, ИИ и HealthTech."
---

## Статьи

Длинные посты (1500–3000 слов) — глубокие разборы, анализ проблем, выводы. То, что требует времени и внимания.

[← Все посты](/ru/blog/)

---

{% assign lang_posts = site.posts | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_posts %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_posts.size == 0 %}
  <li class="empty">Статей пока нет.</li>
{% endif %}
</ul>
