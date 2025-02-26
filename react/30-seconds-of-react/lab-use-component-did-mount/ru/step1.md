# Хук useComponentDidMount в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавлять код в `script.js` и `style.css`.

Для выполнения обратного вызова сразу после монтирования компонента вы можете использовать хук `useEffect()` с пустым массивом в качестве второго аргумента. Это обеспечит то, что предоставленный обратный вызов будет выполнен только один раз при монтировании компонента. Функция `useComponentDidMount()`, показанная ниже, использует этот хук для реализации того же поведения, что и метод жизненного цикла `componentDidMount()` классовых компонентов.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
