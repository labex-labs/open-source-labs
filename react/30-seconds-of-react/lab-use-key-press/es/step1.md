# Hook useKeyPress de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función escucha los cambios en el estado presionado de una tecla dada. Para usarlo:

- Llame a `useKeyPress()` con la tecla objetivo como argumento.
- `useKeyPress()` devuelve un valor booleano que indica si la tecla está siendo presionada actualmente.
- La función utiliza el hook `useState()` para crear una variable de estado que almacena el estado presionado de la tecla dada.
- Define dos funciones de controlador que actualizan la variable de estado al presionar o soltar la tecla en consecuencia.
- El hook `useEffect()` y `EventTarget.addEventListener()` se utilizan para manejar los eventos `'keydown'` y `'keyup'`.
- Finalmente, `EventTarget.removeEventListener()` se utiliza para realizar la limpieza después de que el componente se desmonte.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

A continuación, se muestra un ejemplo de uso de `useKeyPress()` en un componente de React:

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
