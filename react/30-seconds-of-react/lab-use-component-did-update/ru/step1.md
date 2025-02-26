# Хуки React useComponentDidUpdate

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавлять код в `script.js` и `style.css`.

В этом коде представлен пользовательский хук под названием `useComponentDidUpdate`, который выполняет предоставленную функцию `callback` каждый раз, когда компонент обновляется. Вот шаги, которые этот хук выполняет:

1. Создайте переменную `mounted` с использованием хука `useRef()`. Эта переменная отслеживает, был ли компонент монтирован или нет.
2. Используйте хук `useEffect()` для установки значения `mounted` в `true` в первый раз, когда хук выполняется.
3. При последующих выполнениях хука выполните предоставленную функцию `callback` только в том случае, если компонент уже был монтирован.
4. Если предоставляется второй аргумент `condition`, хук будет выполняться только в том случае, если любая из его зависимостей изменится.
5. Этот хук ведет себя аналогично методу жизненного цикла `componentDidUpdate()` классовых компонентов.

Вот код:

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Текущее значение равно ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Значение: {value}, другое значение: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Увеличить значение</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Увеличить другое значение
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
