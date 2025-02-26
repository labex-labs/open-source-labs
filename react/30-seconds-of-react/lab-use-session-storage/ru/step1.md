# Хук React useSessionStorage

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы создать значение с состоянием, которое сохраняется в `sessionStorage`, и функцию для его обновления, следуйте шагам:

1. Используйте хук `useState()` с функцией для ленивой инициализации его значения.
2. Используйте блок `try...catch` и `Storage.getItem()` для попытки получить значение из `Window.sessionStorage`. Если значение не найдено, используйте `Storage.setItem()` для сохранения `defaultValue` и используйте его в качестве начального состояния. Если возникает ошибка, используйте `defaultValue` в качестве начального состояния.
3. Определите функцию, которая обновит переменную состояния переданным значением и использует `Storage.setItem()` для сохранения его.

Вот пример реализации:

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Вы можете использовать этот хук в своем приложении так:

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
