# Переключатель показа/скрытия пароля

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Следующий код отображает поле ввода пароля с кнопкой показа. Он использует хук `useState()`, чтобы создать переменную состояния `shown` и установить ее начальное значение в `false`. Когда нажимается кнопка `Show/Hide`, вызывается функция `setShown`, которая переключает `type` ввода между `'text'` и `'password'`.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Show/Hide</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
