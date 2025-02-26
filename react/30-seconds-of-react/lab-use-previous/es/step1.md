# Hook usePrevious de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para almacenar el estado o las propiedades anteriores, se puede crear un hook personalizado. Estos son los pasos:

1. Defina un hook personalizado que tome un argumento `value`.
2. Utilice el hook `useRef()` para crear una `ref` para el `value`.
3. Utilice el hook `useEffect()` para recordar el último `value`.
4. Devuelva el valor `ref.current`.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

A continuación, se muestra un ejemplo de uso del hook `usePrevious`:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Actual: {value} - Anterior: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Incrementar</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

El componente `Counter` muestra los valores actual y anterior de `value`. Cuando se hace clic en el botón `Incrementar`, `value` se actualiza y el valor anterior se almacena utilizando el hook `usePrevious`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
