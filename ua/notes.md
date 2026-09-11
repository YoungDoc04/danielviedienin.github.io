---
layout: page
lang: ua
nav: blog
permalink: /ua/notes/
title: "ДВ | Нотатки"
description: "Короткі польові нотатки про екстрену медицину, ШІ та HealthTech."
---

## Нотатки

Короткі пости (300–500 слів) — швидкі спостереження, ідеї, посилання. Те, що не потребує довгого тексту, але може бути корисним.

[← Усі пости](/ua/blog/)

---

{% assign lang_notes = site.notes | where: "lang", page.lang | sort: "date" | reverse %}
<ul class="post-list">
{% for item in lang_notes %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if lang_notes.size == 0 %}
  <li class="empty">Поки що немає нотаток.</li>
{% endif %}
</ul>
