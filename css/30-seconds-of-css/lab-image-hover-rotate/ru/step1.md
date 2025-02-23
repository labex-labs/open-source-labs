# Вращение изображения при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания эффекта вращения изображения при наведении курсора используйте свойства `scale()`, `rotate()` и `transition` при наведении на родительский элемент, который должен быть элементом `<figure>`. Чтобы убедиться, что трансформация изображения не вылезает за пределы родительского элемента, добавьте `overflow: hidden` в CSS родительского элемента. Вот пример кода HTML и CSS:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
