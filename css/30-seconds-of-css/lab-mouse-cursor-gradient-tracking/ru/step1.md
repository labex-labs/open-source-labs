# Отслеживание градиента курсора мыши

Файлы `index.html` и `style.css` уже предоставлены в виртуальной машине (VM).

Для создания эффекта наведения, при котором градиент следует за курсором мыши, выполните следующие шаги:

1. Объявите две переменные CSS, `--x` и `--y`, для отслеживания положения мыши на кнопке.
2. Объявите переменную CSS `--size` для изменения размеров градиента.
3. Используйте `background: radial-gradient(circle closest-side, pink, transparent)`, чтобы создать градиент в правильном положении.
4. Зарегистрируйте обработчик события `'mousemove'` с помощью `Document.querySelector()` и `EventTarget.addEventListener()`.
5. Обновите значения переменных CSS `--x` и `--y` с помощью `Element.getBoundingClientRect()` и `CSSStyleDeclaration.setProperty()`.

Вот HTML - код для кнопки:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

А вот CSS - код:

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Наконец, вот JavaScript - код:

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб - страницу.
