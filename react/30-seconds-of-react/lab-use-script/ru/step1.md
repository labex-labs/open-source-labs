# Хук useScript в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для динамической загрузки внешнего скрипта используйте хук `useState()`, чтобы создать переменную состояния, которая будет хранить статус загрузки скрипта. Затем используйте хук `useEffect()` для обработки всей логики загрузки и выгрузки скрипта при любом изменении `src`. Если значение `src` отсутствует, установите `status` в `'idle'` и вернитесь. Используйте `Document.querySelector()` для проверки наличия элемента `<script>` с соответствующим значением `src`. Если нет соответствующего элемента, используйте `Document.createElement()` для его создания и дайте ему соответствующие атрибуты. Используйте атрибут `data-status` для указания статуса скрипта, изначально установив его в `'loading'`. Если существует соответствующий элемент, пропустите инициализацию и обновите `status` из его атрибута `data-status`. Это гарантирует, что не будет создано дублирующееся элементы. Используйте `EventTarget.addEventListener()` для прослушивания событий `'load'` и `'error'` и обработайте их, обновляя атрибут `data-status` и переменную состояния `status`. Наконец, когда компонент размонтируется, используйте `Document.removeEventListener()` для удаления любых слушателей, связанных с элементом.

Вот пример реализации хука `useScript`:

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

Вот пример использования хука `useScript`:

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
