---
layout: page
lang: ru
nav: blog
permalink: /ru/blog/
title: "ДВ | Блог"
description: "Экстренная медицина, ИИ в практике и HealthTech — заметки и статьи Данила Веденина."
---

## Блог

Здесь я пишу о том, что вижу каждый день: экстренная медицина, ИИ в практике, HealthTech и всё, что между ними. Короткие заметки с выездов, длинные разборы кейсов, мысли о том, как технологии меняют работу врача.

### Заметки

Короткие посты (300–500 слов) — быстрые наблюдения, идеи, ссылки. То, что не требует длинного текста, но может быть полезно.

[Смотреть заметки →](/ru/notes/)

### Статьи

Длинные посты (1500–3000 слов) — глубокие разборы, анализ проблем, выводы. То, что требует времени и внимания.

[Смотреть статьи →](/ru/articles/)

---

### Все посты

{% assign lang_posts = site.posts | where: "lang", page.lang %}
{% assign lang_notes = site.notes | where: "lang", page.lang %}
{% assign all_items = lang_posts | concat: lang_notes | sort: "date" | reverse %}
<ul class="post-list">
{% for item in all_items %}
  <li><a href="{{ item.url }}">{{ item.title }}</a><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%Y-%m-%d" }}</time></li>
{% endfor %}
{% if all_items.size == 0 %}
  <li class="empty">Пока ничего не опубликовано — загляните позже.</li>
{% endif %}
</ul>
