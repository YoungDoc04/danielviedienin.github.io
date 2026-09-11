---
layout: page
lang: ua
nav: blog
permalink: /ua/blog/
title: "ДВ | Блог"
description: "Екстрена медицина, ШІ в практиці та HealthTech — нотатки та статті Данила Вєдєніна."
---

## Блог

Тут я пишу про те, що бачу щодня: екстрена медицина, ШІ в практиці, HealthTech і все, що між ними. Короткі нотатки з виїздів, довгі розбори кейсів, думки про те, як технології змінюють роботу лікаря.

### Нотатки

Короткі пости (300–500 слів) — швидкі спостереження, ідеї, посилання. Те, що не потребує довгого тексту, але може бути корисним.

[Дивитися нотатки →](/ua/notes/)

### Статті

Довгі пости (1500–3000 слів) — глибокі розбори, аналіз проблем, висновки. Те, що потребує часу та уваги.

[Дивитися статті →](/ua/articles/)

---

### Усі пости

{% assign lang_posts = site.posts | where: "lang", page.lang %}
{% assign lang_notes = site.notes | where: "lang", page.lang %}
{% assign all_items = lang_posts | concat: lang_notes | sort: "date" | reverse %}
<ul class="post-list">
{% for item in all_items %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if all_items.size == 0 %}
  <li class="empty">Поки що нічого не опубліковано — зазирніть пізніше.</li>
{% endif %}
</ul>
