# Состояние чекбокса с множественным выбором

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код отображает список чекбоксов и отправляет выбранное значение или значения в родительский компонент с использованием обратного вызова. Вот шаги по созданию этого:

1. Используйте хук `useState()`, чтобы инициализировать переменную состояния `data` с помощью свойства `options`.
2. Создайте функцию `toggle`, которая обновляет переменную состояния `data` с выбранным вариантом или вариантами и вызывает функцию обратного вызова `onChange` с ними.
3. Создайте карту переменной состояния `data`, чтобы сгенерировать отдельные чекбоксы и их метки. Свяжите функцию `toggle` с обработчиком `onClick` каждого чекбокса.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Вот пример использования этого:

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
