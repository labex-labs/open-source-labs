# React useOnGlobalEvent Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función ejecuta una función de devolución de llamada cada vez que ocurre un evento en el objeto global. Para implementar esta función:

1. Utilice el hook `useRef()` para crear una variable, `listener`, que contendrá la referencia del oyente.
2. Utilice el hook `useRef()` para crear una variable que contendrá los valores anteriores de los argumentos `type` y `options`.
3. Utilice el hook `useEffect()` y `EventTarget.addEventListener()` para escuchar el evento `type` dado en el objeto global `Window`.
4. Utilice `EventTarget.removeEventListener()` para eliminar cualquier oyente existente y limpiar cuando el componente se desmonte.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Este es un ejemplo de cómo utilizar esta función:

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
