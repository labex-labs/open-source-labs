# Хук useTitle в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Для установки заголовка страницы можно использовать пользовательский хук `useTitle`. Этот хук использует `typeof`, чтобы проверить, определено ли `Document`. Если оно определено, то хук `useRef()` используется для хранения исходного заголовка `Document`. Затем хук `useEffect()` используется для установки `Document.title` значению, переданному при монтировании компонента, и очистки при демонтировании.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

В примера коде компонент `Alert` использует хук `useTitle`, чтобы установить заголовок в "Alert". Компонент `MyApp` отображает кнопку, которая переключает компонент `Alert`.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title has changed</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Toggle alert</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
