# Круг

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания круглой формы с использованием чистого CSS используйте свойство `border-radius: 50%`, чтобы закруглить границы элемента. Убедитесь, что установите оба `width` и `height` равными значениям, чтобы обеспечить идеальный круг. Если использовать разные значения, будет создан эллипс. Вот пример кода:

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
