# Hook useWindowSize de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para rastrear las dimensiones de la ventana del navegador, se pueden seguir los siguientes pasos:

1. Utilizar el hook `useState()` para inicializar una variable de estado `windowSize` que contendrá las dimensiones de la ventana. Inicializar con ambos valores establecidos en `undefined` para evitar desajustes entre los renderizados del servidor y el cliente.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. Crear una función `handleResize()` que utilice `Window.innerWidth` y `Window.innerHeight` para actualizar la variable de estado. Esta función se llamará cada vez que se active el evento `'resize'`.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Utilizar el hook `useEffect()` para establecer un oyente adecuado para el evento `'resize'` al montar y eliminarlo al desmontar.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

Juntando todo, el hook personalizado `useWindowSize()` se puede definir como sigue:

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

Para usar el hook `useWindowSize()`, simplemente llámelo en un componente y desestructura los valores de `width` y `height` del objeto devuelto.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Tamaño de la ventana: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
