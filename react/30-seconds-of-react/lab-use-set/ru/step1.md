# React хук useSet

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция создает объект `Set` со состоянием и набором функций, которые могут манипулировать состоянием.

Для использования этой функции:

- Вызовите `useState()` и конструктор `Set`, чтобы создать новый `Set` из `initialValue`.
- Используйте `useMemo()`, чтобы создать набор функций, которые не изменяют состояние, и которые могут манипулировать переменной состояния `set`. Каждый раз используйте установщик состояния, чтобы создать новый `Set`.
- Верните как переменную состояния `set`, так и созданные `actions`.

Вот пример реализации этой функции:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

Вот пример использования этой функции:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Добавить</button>
      <button onClick={() => clear()}>Сбросить</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Удалить apples
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
