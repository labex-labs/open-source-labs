# Хук useNavigatorOnLine в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для проверки, находится ли клиент в сети или оффлайн, вы можете создать функцию `getOnLineStatus`, которая использует веб-API `Navigator.onLine`. Затем, чтобы реализовать эту функциональность в компоненте React, вы можете использовать пользовательский хук `useNavigatorOnLine`. Этот хук создает переменную состояния под названием `status` с использованием хука `useState()` и устанавливает ее в значение, возвращаемое функцией `getOnLineStatus()`. Хук `useEffect()` используется для добавления слушателей событий при изменении статуса подключения/отключения, обновления переменной состояния `status` в соответствии и очистки этих слушателей при демонтировании компонента. Наконец, переменная `isOnline`, возвращаемая функцией `useNavigatorOnLine()`, может быть использована для отображения сообщения о том, находится ли клиент в сети или оффлайн.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
