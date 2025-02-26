# Hook useMergeState de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un valor con estado y una función para actualizarlo mediante la fusión del nuevo estado proporcionado, use el hook `useState()` para crear una variable de estado y agréguela a `initialState`. Cree una función que actualizará la variable de estado fusionando el nuevo estado proporcionado con el existente. Si el nuevo estado es una función, llámela con el estado anterior como argumento y utilice el resultado. Si no se proporciona ningún argumento, la variable de estado se inicializará con un objeto vacío (`{}`). El siguiente código demuestra cómo implementar esto usando el hook personalizado `useMergeState`:

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

A continuación, se muestra un ejemplo de uso del hook `useMergeState` en un componente llamado `MyApp`:

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

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
