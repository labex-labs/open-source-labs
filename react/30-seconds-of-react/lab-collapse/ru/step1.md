# Свертываемое содержимое

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция отображает компонент с возможностью свертывания с кнопкой, которая переключает видимость его содержимого. Вот, как это использовать:

1. Используйте хук `useState()` для создания переменной состояния `isCollapsed`, которая представляет, свернуто или развернуто содержимое в данный момент. Инициализируйте ее значением `collapsed`.
2. Используйте элемент `<button>` для переключения состояния `isCollapsed` и отображения/скрытия содержимого, переданного через пропс `children`.
3. Используйте `isCollapsed` для применения соответствующего CSS-класса к контейнеру содержимого, либо `collapsed`, либо `expanded`, что определяет его внешний вид.
4. Обновите атрибут `aria-expanded` контейнера содержимого в зависимости от состояния `isCollapsed`, чтобы сделать компонент доступным для пользователей с ограниченными возможностями.

Вот CSS-код, необходимый для этого компонента:

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

И вот JavaScript-код:

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Показать" : "Скрыть"} содержимое
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

Для использования этого компонента просто вызовите его с содержимым, которое вы хотите свернуть:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>Это свертывание</h1>
    <p>Привет, мир!</p>
  </Collapse>
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
