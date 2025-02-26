# Хук React useEffectOnce

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавлять код в `script.js` и `style.css`.

Ниже приведен код, реализующий функцию `useEffectOnce(callback, when)`, которая запускает `callback` только один раз, когда условие `when` становится истинным.

Для реализации этой функции:

- Создайте переменную `hasRunOnce` с использованием хука `useRef()` для отслеживания статуса выполнения эффекта.
- Используйте хук `useEffect()`, который запускается только при изменении условия `when`.
- Внутри хука `useEffect()` проверьте, является ли `when` истинным и был ли эффект ранее выполнен. Если оба условия истинны, запустите `callback` и установите `hasRunOnce` в `true`.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

Вот пример использования `useEffectOnce()`:

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

В примере `useEffectOnce()` используется для вывода в консоль "mounted" при первом нажатии на кнопку. Хук `useEffectOnce()` передается два аргумента: `callback` для выполнения и условие `when` для проверки. Условие `when` установлено в состояние `clicked`, поэтому `callback` выполняется только при первом нажатии, когда `clicked` становится истинным.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
