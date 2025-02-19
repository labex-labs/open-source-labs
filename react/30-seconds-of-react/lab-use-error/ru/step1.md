# Хук React useError

> Файлы `index.html` и `script.js` уже предоставлены в виртуальной машине (VM). В общем, вам нужно добавить код только в файлы `script.js` и `style.css`.

Этот код создает диспетчер ошибок. Он использует три хука React для управления состоянием ошибки и передачи ее в пользовательский интерфейс.

Вот как работает этот код:

1. Хук `useState()` создает переменную состояния с именем `error`, которая хранит объект ошибки. Он принимает начальное значение `err`, которое передается в качестве аргумента в хук.

2. Хук `useEffect()` используется для "выбрасывания" ошибки, если она имеет истинное значение. Этот хук принимает функцию и массив зависимостей в качестве аргументов. В данном случае функция проверяет, имеет ли переменная состояния `error` истинное значение (то есть не является `null`, `undefined`, `0`, `false` или пустой строкой), и выбрасывает ее, если это так. Массив зависимостей - `[error]`, что означает, что эффект будет повторно выполняться каждый раз, когда переменная `error` изменяется.

3. Хук `useCallback()` используется для создания закэшированной функции с именем `dispatchError`, которая обновляет переменную состояния `error` и возвращает новую функцию. Этот хук принимает функцию и массив зависимостей в качестве аргументов. В данном случае функция принимает аргумент `err`, который представляет собой новый объект ошибки, который нужно передать. Массив зависимостей - `[]`, что означает, что закэшированная функция будет пересоздаваться только при повторном рендеринге компонента.

Вот пример того, как использовать хук `useError()` в компоненте:

1. Создайте новый компонент с именем `ErrorButton`.

2. Внутри компонента вызовите хук `useError()` для получения функции `dispatchError`.

3. Создайте функцию обработчика клика с именем `clickHandler`, которая вызывает `dispatchError` с новым объектом ошибки.

4. Отрендерите кнопку, которая вызывает `clickHandler` при нажатии.

Вот код:

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
