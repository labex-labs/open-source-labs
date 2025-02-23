# Анимация подчеркивания при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать эффект анимированного подчеркивания при наведении курсора на текст, следуйте шагам:

1. Используйте `display: inline-block`, чтобы подчеркивание охватывало только ширину текстового контента.
2. Используйте псевдо-элемент `::after` с `width: 100%` и `position: absolute`, чтобы поместить его под содержимым.
3. Используйте `transform: scaleX(0)`, чтобы изначально скрыть псевдо-элемент.
4. Используйте селектор псевдо-класса `:hover`, чтобы применить `transform: scaleX(1)` и отобразить псевдо-элемент при наведении курсора.
5. Анимируйте `transform` с использованием `transform-origin: left` и соответствующего `transition`.
6. Удалите свойство `transform-origin`, чтобы трансформация начиналась из центра элемента.

Вот пример HTML-кода, чтобы применить эффект к текстовому элементу:

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

И вот соответствующий CSS-код:

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
