# React useComponentWillUnmount Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para ejecutar una devolución de llamada inmediatamente antes de que un componente sea desmontado y destruido, puedes usar el hook `useEffect()` con un array vacío como segundo argumento. Devuelve la devolución de llamada proporcionada para que se ejecute solo una vez antes de la limpieza. Este comportamiento es similar al método de ciclo de vida `componentWillUnmount()` de los componentes de clase. También puedes usar el siguiente fragmento de código para crear un hook personalizado `useComponentWillUnmount()` que tome una función `onUnmountHandler` como argumento y la ejecute antes de que el componente sea desmontado:

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

Luego, puedes usar este hook personalizado en tu componente funcional de la siguiente manera:

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

Esto registrará "Component will unmount" en la consola cuando el componente esté a punto de ser desmontado.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
