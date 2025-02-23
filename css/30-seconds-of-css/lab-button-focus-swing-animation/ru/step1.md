# Анимация кнопки при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания анимации при наведении курсора на кнопку, вы должны использовать соответствующее свойство `transition`, чтобы анимировать изменения элемента. Затем, примените псевдо-класс `:focus` к элементу и используйте `animation` с `transform`, чтобы заставить кнопку "качать" (swing). Наконец, добавьте `animation-iteration-count`, чтобы анимация воспроизводилась только один раз. Вот пример, как это можно сделать с использованием HTML и CSS:

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
