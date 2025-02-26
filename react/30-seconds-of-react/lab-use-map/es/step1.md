# Hook useMap de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

- El hook `useMap()` crea un objeto `Map` con estado y un conjunto de funciones para manipularlo utilizando los hooks de React.
- El hook `useState()` inicializa el estado del `Map` con el `initialValue`.
- El hook `useMemo()` crea un conjunto de acciones inmutables que manipulan la variable de estado `map` utilizando el establecedor de estado para crear un nuevo `Map` cada vez.
- El hook `useMap()` devuelve un array que contiene la variable de estado `map` y las `actions` creadas.
- El componente `MyApp` utiliza el hook `useMap()` para inicializar el objeto `Map` con estado y proporciona botones para agregar, reiniciar y eliminar elementos del `Map`.
- La función `JSON.stringify()` formatea el objeto `Map` en una cadena JSON legible.

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
      <button onClick={handleAdd}>Agregar</button>
      <button onClick={handleReset}>Reiniciar</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Eliminar manzanas
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
