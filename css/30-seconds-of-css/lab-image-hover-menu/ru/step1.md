# Меню при наведении на изображение

В ВМ уже предоставлены `index.html` и `style.css`.

Для отображения выпадающего меню при наведении курсора мыши на изображение используйте `<figure>` для оборачивания элемента `<img>` и элемент `<div>`, который будет содержать ссылки меню. Примените следующие свойства CSS для создания анимации изображения при наведении, создавая эффект скольжения:

- `opacity`
- `right`
  Установите атрибут `left` элемента `<div>` равным отрицательному значению ширины элемента. Сбросьте его до `0` при наведении на родительский элемент, чтобы вывести меню. Наконец, используйте `display: flex`, `flex-direction: column` и `justify-content: center` для элемента `<div>`, чтобы вертикально центрировать пункты меню.

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Home</a>
    <a href="#">Pricing</a>
    <a href="#">About</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
