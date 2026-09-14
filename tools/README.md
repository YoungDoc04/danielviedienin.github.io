# Генерация PDF резюме

Скрипты, которыми были собраны `assets/files/CV-Daniel-Viedienin-EN.pdf` и `-UA.pdf`. Нужны для
того, чтобы обновить резюме (поправить текст) или сделать версию на ещё одном языке (например RU),
не пересобирая PDF вручную в дизайнере.

## Запуск

```bash
pip install reportlab --break-system-packages   # если ещё не установлен
cd tools
python3 generate-cv-pdf-en.py   # пересоберёт assets/files/CV-Daniel-Viedienin-EN.pdf
python3 generate-cv-pdf-ua.py   # пересоберёт assets/files/CV-Daniel-Viedienin-UA.pdf
```

Запускать из папки `tools/` — пути к шрифтам (`fonts/`) и к выходному файлу (`../assets/files/`)
уже настроены относительно этой папки, ничего менять не нужно.

## Как сделать RU-версию (или обновить текст)

1. Скопируйте `generate-cv-pdf-ua.py` в `generate-cv-pdf-ru.py`.
2. Замените текст внутри `story.append(Paragraph(...))` — блок за блоком, ничего в структуре
   стилей (`name_style`, `section_style` и т.д.) трогать не нужно.
3. Поменяйте путь в `SimpleDocTemplate(...)` на `CV-Daniel-Viedienin-RU.pdf`.
4. Запустите — если получится больше 2 страниц, тесните отступы (`spaceBefore`/`spaceAfter`/
   `leading` в стилях наверху файла) или размер шрифта на 0.1–0.3pt, как это уже сделано в обоих
   текущих скриптах.
5. Добавьте третью кнопку в `.cv-header__buttons` и `.btn-stack` на всех трёх `cv.md`.

Шрифты (IBM Plex Serif, DejaVu Sans) уже лежат в `fonts/` — поддерживают кириллицу и украинские
буквы (і, ї, є, ґ) из коробки.
