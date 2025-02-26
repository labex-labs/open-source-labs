# Хук React usePortal

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы создать портал, который отображает дочерние элементы вне родительского компонента, следуйте этим шагам:

1. Используйте хук `useState()`, чтобы создать переменную состояния, которая хранит функции `render()` и `remove()` для портала.
2. Используйте `ReactDOM.createPortal()` и `ReactDOM.unmountComponentAtNode()` для создания портала и функции для его удаления. Используйте хук `useCallback()`, чтобы обернуть и мемоизировать эти функции как `createPortal()`.
3. Используйте хук `useEffect()`, чтобы вызвать `createPortal()` и обновить переменную состояния каждый раз, когда значение `el` меняется.
4. Наконец, верните функцию `render()` переменной состояния.

Вот пример реализации:

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

Чтобы использовать этот хук, создайте компонент, который вызывает `usePortal()` с желаемым DOM-элементом в качестве аргумента. Затем этот компонент может использовать возвращаемую функцию `render()` для отображения содержимого в портале:

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
