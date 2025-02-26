# Hook useDebounce de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para debounce un valor dado, se puede crear un hook personalizado que tome un `valor` y un `retraso`. Utilice el hook `useState()` para almacenar el valor debounce y el hook `useEffect()` para actualizar el valor debounce cada vez que se actualice `valor`. Para retrasar la invocación del setter de la variable de estado anterior por `retraso` ms, use `setTimeout()`. Para limpiar cuando se desmonte el componente, use `clearTimeout()`. Esto es particularmente útil cuando se trata de la entrada del usuario.

A continuación, se muestra una implementación de ejemplo del hook `useDebounce()`:

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

Puede usar el hook `useDebounce()` en un componente de la siguiente manera:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Actual: {value} - Debounce: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Incrementar</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
