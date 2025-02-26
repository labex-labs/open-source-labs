# Хук useLocalStorage в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция создает значение, сохраняемое в `localStorage`, и функцию для его изменения. Вот, как это работает:

1. Чтобы создать значение, используйте хук `useState()` с функцией для его ленивой инициализации.
2. Чтобы получить сохраненное значение из `localStorage`, используйте блок `try...catch` и `Storage.getItem()`. Если нет сохраненного значения, используйте `Storage.setItem()` для сохранения `defaultValue` и используйте его в качестве начального состояния. Если возникает ошибка, используйте `defaultValue`.
3. Определите функцию, которая обновляет переменную состояния переданным значением и использует `Storage.setItem()` для сохранения его.

Вот код:

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Вы можете использовать эту функцию в своем приложении так:

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
