# Неуправляемый элемент `<select>`

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Это компонент, который отображает управляемый элемент `<select>`. Компонент принимает массив значений и функцию обратного вызова для передачи выбранного значения в его родительский компонент. Вот шаги по использованию этого компонента:

- Используйте свойство `selectedValue` для установки начального значения элемента `<select>`.
- Используйте свойство `onValueChange` для указания функции обратного вызова, которая должна вызываться при изменении значения элемента `<select>`.
- Используйте `Array.prototype.map()` для массива `values`, чтобы создать элемент `<option>` для каждого переданного значения.
- Каждый элемент в `values` должен быть массивом из двух элементов, где первый элемент — это `value` элемента, а второй — отображаемый текст для него.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Вот пример использования этого компонента:

```jsx
const choices = [
  ["grapefruit", "Грейпфрут"],
  ["lime", "Лайм"],
  ["coconut", "Кокос"],
  ["mango", "Манго"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
