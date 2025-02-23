# Красивое подчёркивание текста

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы избежать обрезания подчёркивания опускающимися буквами, используйте `text-shadow` с четырьмя значениями, чтобы создать толстую тень, которая будет покрывать линию, где опускающиеся буквы касаются подчёркивания. Убедитесь, что цвет `text-shadow` совпадает с цветом `background`, и скорректируйте значения `px` для больших шрифтов. Создайте фактическое подчёркивание с использованием `background-image` с `linear-gradient()` и `currentColor`. Установите `background-position`, `background-repeat` и `background-size`, чтобы расположить градиент в правильном положении. Используйте псевдо-класс селектор `::selection`, чтобы убедиться, что текст-shadow не помешает выбрать текст. Обратите внимание, что этот эффект реализован встроенно как `text-decoration-skip-ink: auto`, но при этом есть меньший контроль над подчёркиванием.

Вот пример кода:

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
