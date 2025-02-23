# Наложение текста на изображение

В ВМ уже предоставлены `index.html` и `style.css`.

Для отображения текста поверх изображения с наложением используйте свойство `backdrop-filter` для применения эффектов `blur(14px)` и `brightness(80%)`. Это гарантирует, что текст читаемый независимо от фонового изображения и цвета. Вот пример HTML-кода:

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

И соответствующий CSS-код:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
