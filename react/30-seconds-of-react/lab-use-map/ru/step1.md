# React useMap хук

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

- Хук `useMap()` создает состояние `Map` объекта и набор функций для его управления с использованием React-хуков.
- Хук `useState()` инициализирует состояние `Map` с `initialValue`.
- Хук `useMemo()` создает набор не-модифицирующих действий, которые манипулируют переменной состояния `map`, используя установщик состояния для создания новой `Map` каждый раз.
- Хук `useMap()` возвращает массив, содержащий переменную состояния `map` и созданные `actions`.
- Компонент `MyApp` использует хук `useMap()` для инициализации состояния `Map` объекта и предоставляет кнопки для добавления, сброса и удаления элементов из `Map`.
- Функция `JSON.stringify()` форматирует `Map` объект в читаемую JSON строку.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Remove apples
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
