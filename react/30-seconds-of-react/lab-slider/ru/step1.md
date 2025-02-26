# Неуправляемый ввод диапазона

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы создать ползунок в React, используйте компонент `Slider` и передайте в него пропсы `min`, `max`, `defaultValue` и `onValueChange`.

В компоненте `Slider` задайте `type` элемента `<input>` как `"range"` для создания ползунка. Используйте пропс `defaultValue`, переданный от родителя, в качестве начального значения для неуправляемого поля ввода. Используйте событие `onChange`, чтобы вызвать обратный вызов `onValueChange` и передать новое значение в родительский компонент.

Вот код для компонента `Slider`:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Чтобы отрендерить компонент `Slider`, используйте `ReactDOM.createRoot` и передайте функцию обратного вызова `onValueChange`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
