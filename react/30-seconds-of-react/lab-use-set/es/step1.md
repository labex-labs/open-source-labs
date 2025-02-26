# React useSet Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función crea un objeto `Set` con estado y un conjunto de funciones que pueden manipular el estado.

Para usar esta función:

- Llame a `useState()` y al constructor `Set` para crear un nuevo `Set` a partir del `initialValue`.
- Utilice `useMemo()` para crear un conjunto de funciones inmutables que pueden manipular la variable de estado `set`. Cree un nuevo `Set` cada vez utilizando el setter de estado.
- Devuelva tanto la variable de estado `set` como las `actions` creadas.

A continuación, se muestra una implementación de ejemplo de esta función:

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

A continuación, se muestra un ejemplo de uso de esta función:

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Agregar</button>
      <button onClick={() => clear()}>Restablecer</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Quitar manzanas
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
