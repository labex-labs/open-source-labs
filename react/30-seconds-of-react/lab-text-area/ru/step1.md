# Неуправляемый элемент <textarea>

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Эта функция отображает элемент `<textarea>`, который не контролируется родительским компонентом. Она использует функцию обратного вызова для передачи значения ввода в родительский компонент.

Для использования этой функции:

- Передайте свойство `defaultValue` из родительского компонента в качестве начального значения поля ввода.
- Используйте событие `onChange` для вызова обратного вызова `onValueChange` и отправки нового значения в родительский компонент.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Пример использования:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
