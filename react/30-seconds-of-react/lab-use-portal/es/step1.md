# React usePortal Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un portal que renderice hijos fuera del componente padre, siga estos pasos:

1. Utilice el hook `useState()` para crear una variable de estado que almacene las funciones `render()` y `remove()` para el portal.
2. Utilice `ReactDOM.createPortal()` y `ReactDOM.unmountComponentAtNode()` para crear un portal y una función para eliminarlo. Utilice el hook `useCallback()` para envolver y memoizar estas funciones como `createPortal()`.
3. Utilice el hook `useEffect()` para llamar a `createPortal()` y actualizar la variable de estado cada vez que cambie el valor de `el`.
4. Finalmente, devuelva la función `render()` de la variable de estado.

A continuación, se muestra una implementación de ejemplo:

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

Para usar este hook, cree un componente que llame a `usePortal()` con el elemento DOM deseado como argumento. Este componente luego puede usar la función `render()` devuelta para renderizar contenido en el portal:

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
