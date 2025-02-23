# Торсионный спиннер

В ВМ уже предоставлены `index.html` и `style.css`.

Для индикации загрузки контента создайте торсионный спиннер с полупрозрачной `рамкой` для всего элемента. Исключите одну сторону, чтобы она служила индикатором загрузки для тора. Затем определите и используйте соответствующую анимацию, используя `transform: rotate()` для вращения элемента. Вот пример кода на HTML и CSS:

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
