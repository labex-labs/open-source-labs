# Hook useHash de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código rastrea y actualiza el valor del hash de la ubicación del navegador. Para usarlo, siga estos pasos:

1. Utilice el hook `useState()` para obtener de manera perezosa la propiedad `hash` del objeto `Location`.
2. Utilice el hook `useCallback()` para crear un controlador que actualice el estado `hash` cuando se dispare el evento `'hashchange'`.
3. Utilice el hook `useEffect()` para agregar un oyente para el evento `'hashchange'` al montar y eliminarlo al desmontar.
4. Utilice el hook `useCallback()` para crear una función que actualice la propiedad `hash` del objeto `Location` con el valor dado.
5. En su componente, llame a `useHash()` para obtener el valor actual de `hash` y una función `updateHash()` para cambiarlo.
6. Utilice la función `updateHash()` para cambiar el valor de `hash`.
7. Renderice el valor actual de `hash` en un componente.
8. Cree un campo de entrada que permita al usuario cambiar el valor de `hash`.

Aquí está el código:

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Valor de hash actual: {hash}</p>
      <p>Editar hash: </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
