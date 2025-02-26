# React useComponentDidMount Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para ejecutar una función de devolución de llamada inmediatamente después de que un componente se monta, se puede usar el hook `useEffect()` con un array vacío como segundo argumento. Esto garantizará que la devolución de llamada proporcionada se ejecute solo una vez cuando el componente se monta. La función `useComponentDidMount()` que se muestra a continuación utiliza este hook para implementar el mismo comportamiento que el método de ciclo de vida `componentDidMount()` de los componentes de clase.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
