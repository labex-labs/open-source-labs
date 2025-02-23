# Анимация теневой рамки при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания теневой рамки вокруг текста при наведении курсора выполните следующие шаги:

1. Установите `transform: perspective(1px)`, чтобы дать элементу трехмерное пространство, изменив расстояние между плоскостью Z и пользователем, и `translateZ(0)`, чтобы переместить элемент `<p>` по оси z в трехмерном пространстве.
2. Используйте `box-shadow`, чтобы сделать рамку прозрачной.
3. Включите переходы для `box-shadow` и `transform` с помощью свойства `transition-property`.
4. Примените новое значение `box-shadow` и `transform: scale(1.2)`, чтобы изменить масштаб текста, используя псевдо-классы `:hover`, `:active` и `:focus`.
5. Добавьте класс `hover-shadow-box-animation` к элементу `<p>`.

Вот код HTML:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

Вот код CSS:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
