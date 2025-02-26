# Хук useHash в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код отслеживает и обновляет значение хэша адреса в браузере. Чтобы использовать его, следуйте шагам:

1. Используйте хук `useState()`, чтобы лениво получить свойство `hash` объекта `Location`.
2. Используйте хук `useCallback()`, чтобы создать обработчик, который обновляет состояние `hash`, когда событие `'hashchange'` срабатывает.
3. Используйте хук `useEffect()`, чтобы добавить слушатель для события `'hashchange'` при монтировании и удалить его при демонтировании.
4. Используйте хук `useCallback()`, чтобы создать функцию, которая обновляет свойство `hash` объекта `Location` заданным значением.
5. В своем компоненте вызовите `useHash()`, чтобы получить текущее значение `hash` и функцию `updateHash()`, чтобы изменить его.
6. Используйте функцию `updateHash()`, чтобы изменить значение `hash`.
7. Отобразите текущее значение `hash` в компоненте.
8. Создайте поле ввода, которое позволяет пользователю изменить значение `hash`.

Вот код:

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Текущее значение хэша: {hash}</p>
      <p>Изменить хэш: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
