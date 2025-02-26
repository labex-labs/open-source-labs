# Переключатель

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно добавить код только в `script.js` и `style.css`.

Для отображения компонента переключателя следуйте шагам:

1. Используйте хук `useState()`, чтобы инициализировать переменную состояния `isToggledOn` значением `defaultToggled`.
2. Отобразите элемент `<input>` и привяжите к нему событие `onClick`, чтобы обновить переменную состояния `isToggledOn`. Примените соответствующий `className` к оборачивающему элементу `<label>`.
3. Используйте следующий CSS для стилизации компонента переключателя:

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Вот код:

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
