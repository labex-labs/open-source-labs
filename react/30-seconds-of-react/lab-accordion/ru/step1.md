# Свертывающийся аккордеон

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно добавить код только в `script.js` и `style.css`.

Для отображения аккордеонного меню с несколькими свертывающимися элементами содержимого вы можете следовать следующим шагам:

1. Определите компонент `AccordionItem`, который отображает `<button>` и обновляет компонент,.notify его родителя через обратный вызов `handleClick`.
2. Используйте свойство `isCollapsed` в `AccordionItem`, чтобы определить его внешний вид и установить его `className`.
3. Определите компонент `Accordion` и используйте хук `useState()`, чтобы инициализировать значение переменной состояния `bindIndex` значением `defaultIndex`.
4. Отфильтруйте `children`, чтобы удалить ненужные узлы, кроме `AccordionItem`, определив имя функции.
5. Используйте `Array.prototype.map()` для отображения отдельных свертывающихся элементов на собранных узлах.
6. Определите `changeItem`, которая будет выполняться при нажатии на `<button>` `AccordionItem`.
7. `changeItem` выполняет переданный обратный вызов `onItemClick` и обновляет `bindIndex` на основе нажатого элемента.

Вот код:

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
