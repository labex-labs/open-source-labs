# Хук useMergeState в React

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Чтобы создать состояние и функцию для его обновления путём объединения нового состояния, используйте хук `useState()`, чтобы создать переменную состояния и инициализировать её значением `initialState`. Создайте функцию, которая будет обновлять переменную состояния путём объединения нового состояния с существующим. Если новое состояние является функцией, вызовите её с предыдущим состоянием в качестве аргумента и используйте результат. Если аргумент не указан, переменная состояния будет инициализирована пустым объектом (`{}`). Следующий код демонстрирует, как это реализовать с использованием пользовательского хука `useMergeState`:

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

Вот пример использования хука `useMergeState` в компоненте с именем `MyApp`:

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
