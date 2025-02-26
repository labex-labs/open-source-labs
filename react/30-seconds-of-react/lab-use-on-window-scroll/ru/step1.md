# Хук useOnWindowScroll в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция выполняет обратный вызов каждый раз, когда окно прокручивается. Для его реализации:

1. Используйте хук `useRef()` для создания переменной ссылки `listener`.
2. Используйте хук `useEffect()` и `EventTarget.addEventListener()` для прослушивания события `'scroll'` объекта `Window` и назначения ссылки на слушатель `listener.current`.
3. Используйте `EventTarget.removeEventListener()` для удаления любых существующих слушателей при демонтировании компонента.

Вот код:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

Для тестирования функции вы можете использовать ее в компоненте так:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

Это будет выводить вертикальную позицию прокрутки окна каждый раз, когда оно прокручивается.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
