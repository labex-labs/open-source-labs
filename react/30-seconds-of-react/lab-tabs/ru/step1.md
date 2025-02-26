# Вкладки

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для отображения компонента меню и представления вкладок следуйте шагам:

1. Определите компонент `Tabs`. Используйте хук `useState()` для установки переменной состояния `bindIndex` в `defaultIndex`.
2. Определите компонент `TabItem` и отфильтруйте `children`, переданные в компонент `Tabs`, чтобы удалить все ненужные узлы, кроме `TabItem`. Вы можете сделать это, определив имя функции.
3. Определите функцию `changeTab`. Эта функция будет выполняться при нажатии пользователем на `<button>` из меню.
4. `changeTab` выполняет переданный обратный вызов `onTabClick` и обновляет `bindIndex` в зависимости от нажатого элемента.
5. Используйте `Array.prototype.map()` для отображения меню и представления вкладок на собранных узлах.
6. Используйте значение `bindIndex` для определения активной вкладки и примените правильный `className`.

Вот CSS-код для стилизации меню и представления вкладок:

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

Вот JavaScript-код для реализации компонента `Tabs`:

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

Наконец, вот пример использования компонента `Tabs`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

Пожалуйста, нажмите кнопку "Запустить в браузере" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
