# Наложение изображения при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Для отображения эффекта наложения изображения при наведении курсора следуйте шагам:

1. Используйте псевдо-элементы `::before` и `::after` для верхней и нижней полос наложения соответственно. Задайте их `opacity`, `transform` и `transition`, чтобы получить желаемый эффект.
2. Используйте `<figcaption>` для текста наложения. Задайте `display: flex`, `flex-direction: column` и `justify-content: center`, чтобы выровнять текст по центру изображения.
3. Используйте псевдо-селектор `:hover`, чтобы обновить `opacity` и `transform` всех элементов и отобразить наложение.

Вот HTML-код для использования:

```html
<figure class="hover-img">
  <img src="https://picsum.photos/id/200/440/320.jpg" />
  <figcaption>
    <h3>Lorem <br />Ipsum</h3>
  </figcaption>
</figure>
```

Вот CSS-код для использования:

```css
.hover-img {
  display: inline-block;
  margin: 8px;
  width: 100%;
  max-width: 320px;
  min-width: 240px;
  overflow: hidden;
  position: relative;
  text-align: center;
  background-color: #000;
  color: #fff;
}

.hover-img * {
  box-sizing: border-box;
  transition: all 0.45s ease;
}

.hover-img::before,
.hover-img::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-top: 32px solid rgba(0, 0, 0, 0.5);
  border-bottom: 32px solid rgba(0, 0, 0, 0.5);
  z-index: 1;
  opacity: 0;
  transform: scaleY(2);
  transition: all 0.3s ease;
}

.hover-img::before {
  content: "";
  top: 0;
  bottom: auto;
}

.hover-img img {
  vertical-align: top;
  max-width: 100%;
  backface-visibility: hidden;
}

.hover-img figcaption {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.1em;
  opacity: 0;
  z-index: 2;
  transition-delay: 0.1s;
  font-size: 24px;
  font-family: sans-serif;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-img:hover::before,
.hover-img:hover::after {
  transform: scale(1);
  opacity: 1;
}

.hover-img:hover img {
  opacity: 0.7;
}

.hover-img:hover figcaption {
  opacity: 1;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
