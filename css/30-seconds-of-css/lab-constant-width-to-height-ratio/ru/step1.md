# Постоянное соотношение ширины к высоте

В ВМ уже предоставлены `index.html` и `style.css`.

Этот фрагмент кода обеспечивает то, что элемент с переменной `width` будет сохранять пропорциональное значение `height`. Для этого применяется `padding-top` на псевдо-элементе `::before`, делая `height` элемента равным проценту его `width`. Соотношение `height` к `width` можно изменить по необходимости. Например, `padding-top` равный `100%` создаст отзывчивый квадрат с соотношением сторон 1:1. Чтобы использовать этот код, просто добавьте следующий HTML-код:

```html
<div class="constant-width-to-height-ratio"></div>
```

Затем добавьте следующий CSS-код:

```css
.constant-width-to-height-ratio {
  background: #9c27b0;
  width: 50%;
}

.constant-width-to-height-ratio::before {
  content: "";
  padding-top: 100%;
  float: left;
}

.constant-width-to-height-ratio::after {
  content: "";
  display: block;
  clear: both;
}
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
