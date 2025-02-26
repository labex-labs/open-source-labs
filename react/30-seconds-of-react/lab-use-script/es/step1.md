# Hook useScript de React

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para cargar dinámicamente un script externo, use el hook `useState()` para crear una variable de estado que almacene el estado de carga del script. A continuación, use el hook `useEffect()` para manejar toda la lógica de carga y descarga del script cada vez que cambie el `src`. Si no hay un valor de `src`, establezca el `status` en `'idle'` y devuelva. Use `Document.querySelector()` para comprobar si existe un elemento `<script>` con el valor de `src` adecuado. Si no existe ningún elemento relevante, use `Document.createElement()` para crear uno y dale los atributos adecuados. Use el atributo `data-status` como una forma de indicar el estado del script, estableciéndolo inicialmente en `'loading'`. Si existe un elemento relevante, omita la inicialización y actualice el `status` a partir de su atributo `data-status`. Esto garantiza que no se creará ningún elemento duplicado. Use `EventTarget.addEventListener()` para escuchar los eventos `'load'` y `'error'` y manejarlos actualizando el atributo `data-status` y la variable de estado `status`. Finalmente, cuando el componente se desmonta, use `Document.removeEventListener()` para quitar cualquier oyente vinculado al elemento.

A continuación, se muestra una implementación de ejemplo del hook `useScript`:

```jsx
const useScript = (src) => {
  const [status, setStatus] = React.useState(src ? "loading" : "idle");

  React.useEffect(() => {
    if (!src) {
      setStatus("idle");
      return;
    }

    let script = document.querySelector(`script[src="${src}"]`);

    if (!script) {
      script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.setAttribute("data-status", "loading");
      document.body.appendChild(script);

      const setDataStatus = (event) => {
        script.setAttribute(
          "data-status",
          event.type === "load" ? "ready" : "error"
        );
      };
      script.addEventListener("load", setDataStatus);
      script.addEventListener("error", setDataStatus);
    } else {
      setStatus(script.getAttribute("data-status"));
    }

    const setStateStatus = (event) => {
      setStatus(event.type === "load" ? "ready" : "error");
    };

    script.addEventListener("load", setStateStatus);
    script.addEventListener("error", setStateStatus);

    return () => {
      if (script) {
        script.removeEventListener("load", setStateStatus);
        script.removeEventListener("error", setStateStatus);
      }
    };
  }, [src]);

  return status;
};
```

A continuación, se muestra un ejemplo de uso del hook `useScript`:

```jsx
const script =
  "data:text/plain;charset=utf-8;base64,KGZ1bmN0aW9uKCl7IGNvbnNvbGUubG9nKCdIZWxsbycpIH0pKCk7";

const Child = () => {
  const status = useScript(script);
  return <p>Child status: {status}</p>;
};

const MyApp = () => {
  const status = useScript(script);
  return (
    <>
      <p>Parent status: {status}</p>
      <Child />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
