# Неуправляемое поле ввода

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код отображает неуправляемый элемент `<input>`, который использует обратный вызов-функцию для информирования его родителя о обновлениях значения. Чтобы использовать его:

- Передайте начальное значение из родителя с использованием свойства `defaultValue`.
- Передайте обратную вызов-функцию с именем `onValueChange`, чтобы обработать обновления значения.
- Используйте событие `onChange`, чтобы вызвать обратный вызов и отправить новое значение родителю.

Вот пример:

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
