# React useRequestAnimationFrame Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para ejecutar una función de animación antes de cada repintado, use el hook `useRef()` para crear las variables `requestRef` y `previousTimeRef`. Luego, defina una función `animate()` que actualice estas variables, ejecute la `callback` y llame perpetuamente a `Window.requestAnimationFrame()`. Por último, use el hook `useEffect()` con un array vacío para inicializar el valor de `requestRef` con `Window.requestAnimationFrame()`, y use el valor devuelto y `Window.cancelAnimationFrame()` para limpiar cuando el componente se desmonte.

A continuación, se muestra una implementación de ejemplo de `useRequestAnimationFrame()`:

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

Para usar este hook personalizado en un componente, simplemente pase una función de devolución de llamada a él. Por ejemplo, para crear un contador simple que se actualice a 100 FPS:

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
