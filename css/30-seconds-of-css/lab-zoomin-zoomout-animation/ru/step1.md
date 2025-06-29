# Понимание структуры HTML

Перед тем, как мы начнем создавать анимацию, нам нужно понять структуру HTML, с которой будем работать. На этом этапе мы рассмотрим предоставленный HTML - файл и внесем необходимые изменения.

1. Откройте файл `index.html` в редакторе.

2. Если файл пустой или отсутствует, создайте его со следующим содержимым:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Поймем, что делает этот HTML:
   - У нас есть стандартная структура HTML - документа с заголовком и настройками области просмотра (viewport)
   - Мы подключаем внешний CSS - файл с именем `style.css`
   - Мы включаем заголовок и абзац для объяснения нашей демонстрации
   - Самое главное, у нас есть элемент `<div>` с классом `zoom-in-out-box`, который будет анимирован

4. Сохраните файл `index.html`, если вы внесли какие - либо изменения.

Этот элемент `<div>` станет нашей "холстом" для создания анимации. На следующем этапе мы стилизуем этот элемент с помощью CSS.
