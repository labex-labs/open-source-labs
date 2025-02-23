# Анимация границы кнопки

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Для создания анимации границы при наведении курсора можно использовать псевдо-элементы `::before` и `::after`, чтобы сгенерировать два прямоугольника шириной `24px`, расположенных выше и ниже основной кнопки. Затем применить псевдо-класс `:hover`, чтобы при наведении курсора увеличить ширину этих элементов до `100%` и анимировать переход с помощью свойства `transition`.

Ниже представлен пример кода:

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
