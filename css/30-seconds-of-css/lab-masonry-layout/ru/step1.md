# Макет кирпичного стиля

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания макета в стиле кирпичного кладки используйте `.masonry-container` в качестве основного контейнера, и добавьте `.masonry-columns` в качестве внутреннего контейнера, в который будут помещены элементы `.masonry-brick`. Макет состоит из "кирпичей", которые накладываются друг на друга, образуя идеальное сочетание. Ширина (`width`) для вертикального макета и высота (`height`) для горизонтального макета могут быть фиксированы.

Для обеспечения правильного отображения макета примените `display: block` к элементам `.masonry-brick`. Используйте селектор псевдо-элемента `:first-child`, чтобы применить другой `margin` для первого элемента, учитывая его позиционирование.

Для большей гибкости и адаптивности используйте CSS переменные и медиа-запросы. В `.masonry-container` есть CSS переменные для количества колонок и расстояния между ними. Количество колонок контролируется медиа-запросами, которые задают разные количества колонок и ширины для различных размеров экранов.

```html
<div class="masonry-container">
  <div class="masonry-columns">
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1016/384/256"
      alt="An image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1025/495/330"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1024/192/128"
      alt="Another image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1028/518/345"
      alt="One more image"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1035/585/390"
      alt="And another one"
    />
    <img
      class="masonry-brick"
      src="https://picsum.photos/id/1074/384/216"
      alt="Last one"
    />
  </div>
</div>
```

```css
.masonry-container {
  --column-count-small: 1;
  --column-count-medium: 2;
  --column-count-large: 3;
  --column-gap: 0.125rem;
  padding: var(--column-gap);
}

.masonry-columns {
  column-gap: var(--column-gap);
  column-count: var(--column-count-small);
  column-width: calc(1 / var(--column-count-small) * 100%);
}

@media only screen and (min-width: 640px) {
  .masonry-columns {
    column-count: var(--column-count-medium);
    column-width: calc(1 / var(--column-count-medium) * 100%);
  }
}

@media only screen and (min-width: 800px) {
  .masonry-columns {
    column-count: var(--column-count-large);
    column-width: calc(1 / var(--column-count-large) * 100%);
  }
}

.masonry-brick {
  width: 100%;
  height: auto;
  margin: var(--column-gap) 0;
  display: block;
}

.masonry-brick:first-child {
  margin: 0 0 var(--column-gap);
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
