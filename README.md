# danielviedienin.com — исходники сайта

Сайт-резюме и блог на Jekyll, готов к публикации через GitHub Pages.

## Структура

```
_config.yml         настройки сайта (title, email, LinkedIn и т.д.)
_layouts/           шаблоны страниц (default, home, page, post, blog)
_includes/           переиспользуемые куски разметки (head, header, footer)
_posts/              посты блога — по одному .md файлу на пост
assets/css/style.css вся вёрстка одним файлом
assets/js/main.js    открытие/закрытие мобильного меню
assets/img/          сюда положить свою фотографию (daniel-photo.jpg)
index.md             главная страница
about.md             страница "Обо мне"
contact.md           страница "Контакты"
blog/index.html      страница со списком всех постов блога
CNAME                домен для GitHub Pages
```

## Как запустить локально

Нужен установленный Ruby и Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Сайт откроется на http://localhost:4000.

## Как добавить новый пост

1. Создать файл в `_posts/` с именем вида `ГГГГ-ММ-ДД-название-поста.md`,
   например `_posts/2026-09-10-moy-vtoroy-post.md`.
2. В начале файла — front matter:

```markdown
---
title: "Заголовок поста"
excerpt: "Одно-два предложения — краткое описание для списка постов."
---

Текст поста в Markdown...
```

3. `git add`, `git commit`, `git push` — GitHub Pages соберёт сайт
   автоматически. Ничего больше делать не нужно: пост появится в блоге
   на дате из имени файла.

## Первая настройка

1. В `_config.yml` заменить `email` и `linkedin_url` на свои.
2. Положить фото в `assets/img/daniel-photo.jpg` (см. `assets/img/README.md`).
3. При необходимости — поправить текст в `about.md`, `contact.md`
   и на главной (`_layouts/home.html`) под себя.

## Публикация на GitHub Pages

1. Создать репозиторий на GitHub и запушить в него содержимое этой папки.
2. В настройках репозитория: Settings → Pages → Source → выбрать ветку
   `main` и папку `/ (root)`.
3. Файл `CNAME` уже содержит `danielviedienin.com` — когда домен будет
   готов, останется только прописать DNS-записи (A/ALIAS на GitHub Pages
   или CNAME на `<username>.github.io`) согласно инструкции GitHub:
   https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site
4. Пока домен не подключен, сайт будет доступен по адресу
   `https://<username>.github.io/<repo>/` — в `_config.yml` в этом случае
   стоит временно выставить `baseurl: "/<repo>"`.
