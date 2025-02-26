# Hook useEventListener de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función agrega un listener de eventos para el tipo de evento especificado en el elemento dado. Para usar esta función, siga estos pasos:

1. Utilice el hook `useRef()` para crear una referencia que contendrá el `handler`.
2. Utilice el hook `useEffect()` para actualizar el valor de la referencia `savedHandler` cada vez que cambie el `handler`.
3. Utilice el hook `useEffect()` para agregar un listener de eventos al elemento dado y limpiarlo cuando se desmonte.
4. Omita el último argumento, `el`, para usar la `Ventana` por defecto.

Aquí está el código:

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

Y aquí está un ejemplo de uso de la función `useEventListener()`:

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Coordenadas del mouse: {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
