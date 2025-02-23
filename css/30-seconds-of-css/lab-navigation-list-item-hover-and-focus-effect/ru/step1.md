# Эффект наведения курсора и фокуса на элементы списка навигации

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания настраиваемого эффекта наведения курсора и фокуса на элементы навигации используйте преобразования CSS следующим образом:

1. Используйте псевдо-элемент `::before` для якоря элемента списка, чтобы создать эффект наведения курсора. Скрыть его с помощью `transform: scale(0)`.
2. Используйте псевдо-класс селекторы `:hover` и `:focus`, чтобы переключить псевдо-элемент на `transform: scale(1)` и показать его цветной фон.
3. Предотвратите, чтобы псевдо-элемент не закрывал элемент якоря, используя `z-index`.

Вы можете использовать следующий HTML-код для вашего меню навигации:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

И примените следующие правила CSS:

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
