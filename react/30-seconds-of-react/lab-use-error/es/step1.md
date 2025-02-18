# React useError Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo necesitas agregar código a `script.js` y `style.css`.

Este código crea un despachador de errores. Utiliza tres hooks de React para gestionar el estado del error y despacharlo a la interfaz de usuario.

Así es cómo funciona el código:

1. El hook `useState()` crea una variable de estado llamada `error` que almacena el objeto de error. Toma un valor inicial de `err`, que se pasa como argumento al hook.

2. El hook `useEffect()` se utiliza para "lanzar" el error siempre que tenga un valor verdadero. Este hook toma una función y un array de dependencias como argumentos. En este caso, la función comprueba si la variable de estado `error` tiene un valor verdadero (es decir, no es nula, indefinida, 0, falsa o una cadena vacía), y la lanza si es así. El array de dependencias es `[error]`, lo que significa que el efecto se volverá a ejecutar siempre que cambie la variable `error`.

3. El hook `useCallback()` se utiliza para crear una función almacenada en caché llamada `dispatchError`, que actualiza la variable de estado `error` y devuelve la nueva función. Este hook toma una función y un array de dependencias como argumentos. En este caso, la función toma un argumento `err`, que es el nuevo objeto de error a despachar. El array de dependencias es `[]`, lo que significa que la función almacenada en caché solo se volverá a crear si el componente se vuelve a renderizar.

A continuación, se muestra un ejemplo de cómo usar el hook `useError()` en un componente:

1. Crea un nuevo componente llamado `ErrorButton`.

2. Dentro del componente, llama al hook `useError()` para obtener la función `dispatchError`.

3. Crea una función manejadora de clics llamada `clickHandler` que llame a `dispatchError` con un nuevo objeto de error.

4. Renderiza un botón que llame a `clickHandler` cuando se haga clic en él.

Aquí está el código:

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
