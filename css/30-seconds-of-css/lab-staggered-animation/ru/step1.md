# Анимация с задержкой

В ВМ уже предоставлены `index.html` и `style.css`.

Этот код создает анимацию с задержкой для элементов списка. Для этого необходимо:

1. Сделать элементы списка прозрачными и переместить их в самый правый край, установив `opacity: 0` и `transform: translateX(100%)`.
2. Указать одинаковые свойства `transition` для элементов списка, за исключением `transition-delay`.
3. Использовать встроенные стили, чтобы указать значение для `--i` для каждого элемента списка. Это будет использоваться для `transition-delay`, чтобы создать эффект задержки.
4. Использовать псевдо-класс селектор `:checked` для чекбокса, чтобы стилизовать элементы списка. Чтобы они появились и сдвинулись в вид, установите `opacity` в `1` и `transform` в `translateX(0)`.

Вот HTML и CSS код, чтобы достичь этого эффекта:

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
