# React хук useKeyPress

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция слушает изменения состояния нажатой определенной клавиши. Чтобы использовать ее:

- Вызовите `useKeyPress()` с целевой клавишей в качестве аргумента.
- `useKeyPress()` возвращает логическое значение, которое показывает, нажата ли в настоящее время клавиша.
- Функция использует хук `useState()` для создания переменной состояния, которая хранит состояние нажатой заданной клавиши.
- Она определяет две функций-обработчики, которые обновляют переменную состояния при нажатии или отпускании клавиши соответственно.
- Хуки `useEffect()` и `EventTarget.addEventListener()` используются для обработки событий `'keydown'` и `'keyup'`.
- Наконец, `EventTarget.removeEventListener()` используется для очистки после отмонтирования компонента.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

Вот пример использования `useKeyPress()` в компоненте React:

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
