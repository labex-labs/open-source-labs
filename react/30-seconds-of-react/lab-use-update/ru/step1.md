# Хук useUpdate в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавлять код в `script.js` и `style.css`.

Для принудительного перерендеринга компонента при вызове используйте хук `useReducer()`, чтобы создавать новый объект каждый раз при его обновлении и возвращать его диспетчер. Вот пример реализации функции `useUpdate()`:

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

Затем вы можете использовать `useUpdate()` в своем компоненте, чтобы вызвать перерендер при необходимости:

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Time: {Date.now()}</div>
      <button onClick={update}>Update</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
