# Прыгающий лоадер

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания анимации прыгающего лоадера:

1. Определите анимацию `@keyframes`, которая использует свойства `opacity` и `transform`, с трансляцией по одной оси в `transform: translate3d()` для лучшей производительности.
2. Создайте родительский контейнер с классом `.bouncing-loader`, который использует `display: flex` и `justify-content: center`, чтобы центрировать прыгающие круги.
3. Дайте трем `<div>` элементам для прыгающих кругов одинаковую `width`, `height` и `border-radius: 50%`, чтобы они были круговыми.
4. Примените анимацию `bouncing-loader` к каждому из трех прыгающих кругов.
5. Используйте разные `animation-delay` для каждого круга и `animation-direction: alternate`, чтобы создать соответствующий эффект.

Вот HTML-код:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

А вот CSS-код:

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
