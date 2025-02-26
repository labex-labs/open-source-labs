# React хук useToggler

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для создания переменной состояния типа `boolean`, которая может переключаться между двумя состояниями, следуйте этим шагам:

1. Используйте хук `useState()`, чтобы создать переменную состояния `value` и ее функцию-сеттер.
2. Создайте функцию, которая переключает значение переменной состояния `value`, и закэшируйте ее с использованием хука `useCallback()`.
3. Верните переменную состояния `value` и закешированную функцию-тогглера.

Вот пример реализации:

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

Затем вы можете использовать этот хук в своих компонентах, так:

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
