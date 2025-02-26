# React useDefault хук

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Вот код:

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

Для создания состояния с начальным значением, используйте хук `useState()` в React. Проверьте, является ли начальное значение `null` или `undefined`. Если да, верните `defaultState` вместо этого, в противном случае верните фактическое состояние `value` и функцию `setValue`. Код выше показывает, как реализовать эту функциональность в пользовательском хуке под названием `useDefault`.

В приведенном примере `useDefault` используется для создания состояния `user` с начальным значением `{ name: 'Adam' }`. Начальное состояние установлено в `{ name: 'John' }`. В компоненте `UserCard` `user` отображается вместе с полем ввода для обновления его имени. Также есть кнопка "Clear", чтобы сбросить состояние до `null`. Наконец, компонент отображается с использованием `ReactDOM.createRoot()`.

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
