---
layout: page
lang: ru
nav: blog
permalink: /ru/notes/
title: "ДВ | Заметки"
description: "Короткие полевые заметки об экстренной медицине, ИИ и HealthTech."
---

## Заметки

Короткие посты (300–500 слов) — быстрые наблюдения, идеи, ссылки. То, что не требует длинного текста, но может быть полезно.

[← Все посты](/ru/blog/)

---

{% assign lang_notes = site.notes | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_notes %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_notes.size == 0 %}
  <li class="empty">Заметок пока нет.</li>
{% endif %}
</ul>
