# Подсказка

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Вот более ясная, компактная и последовательная версия содержания:

---

Этот код создает компонент подсказки. Чтобы использовать его, выполните следующие действия:

1. Используйте хук `useState()`, чтобы создать переменную `show` и установить ее в значение `false`.
2. Отрендерить элемент-контейнер, который содержит элемент подсказки и `children`, переданные в компонент.
3. Обработайте события `onMouseEnter` и `onMouseLeave`, переключая `className` подсказки, который контролируется переменной `show`.

Вот код для компонента подсказки:

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

Чтобы использовать компонент подсказки, вызовите `ReactDOM.createRoot()` с таким кодом:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
