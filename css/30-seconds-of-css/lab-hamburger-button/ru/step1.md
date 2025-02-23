# Кнопка "бургер"

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Чтобы создать меню "бургер", которое при наведении курсора превращается в крестик, выполните следующие шаги:

1. Используйте контейнер `div` с классом `.hamburger-menu`, который содержит верхнюю, нижнюю и среднюю полосы.
2. Задайте для контейнера `display: flex` с `flex-flow: column wrap`.
3. Добавьте расстояние между полосами с помощью `justify-content: space-between`.
4. Используйте `transform: rotate()` для вращения верхней и нижней полос на 45 градусов и `opacity: 0` для затухания средней полосы при наведении курсора.
5. Используйте `transform-origin: left`, чтобы полосы вращались вокруг левой точки.

Вот соответствующий HTML-код:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

Вот CSS-код:

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
