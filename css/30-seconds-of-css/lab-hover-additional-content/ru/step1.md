# Показывать дополнительный контент при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать карточку, которая отображает дополнительный контент при наведении курсора, следуйте шагам:

1. Используйте `overflow: hidden` для карточки, чтобы скрыть любые элементы, которые выходят за пределы по вертикали.
2. Используйте псевдо-классовые селекторы `:hover` и `:focus-within`, чтобы изменить стиль карточки, когда элемент находится под курсором, имеет фокус или любой из его потомков имеет фокус.
3. Задайте `transition: 0.3s ease all`, чтобы создать гладкий эффект перехода при наведении/фокусе.

Вот пример HTML-кода для карточки:

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

Вот CSS-код для стилизации карточки:

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
