# Хуки React usePersistedState

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот хук возвращает состояние, сохраняемое в `localStorage`, и функцию для его обновления. Чтобы использовать его, следуйте шагам:

1. Используйте хук `useState()` для инициализации `value` значением `defaultValue`.
2. Используйте хук `useRef()` для создания ссылки, которая будет хранить `name` значения в `Window.localStorage`.
3. Используйте 3 экземпляра хука `useEffect()` для инициализации, изменения `value` и изменения `name` соответственно.
4. При первом монтировании компонента используйте `Storage.getItem()`, чтобы обновить `value`, если есть сохраненное значение, или `Storage.setItem()`, чтобы сохранить текущее значение.
5. При обновлении `value` используйте `Storage.setItem()`, чтобы сохранить новое значение.
6. При обновлении `name` используйте `Storage.setItem()`, чтобы создать новый ключ, обновить `nameRef` и использовать `Storage.removeItem()`, чтобы удалить предыдущий ключ из `Window.localStorage`.
7. Обратите внимание, что хук предназначен для использования с примитивными значениями (то есть не объектами) и не учитывает изменения в `Window.localStorage` из-за другого кода. Эти два вопроса могут быть легко обработаны (например, сериализация JSON и обработка события `'storage'`).

Вот код:

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
