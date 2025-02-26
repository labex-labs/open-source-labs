# Hook useSSR de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para comprobar si el código se está ejecutando en un navegador o en un servidor, cree un hook personalizado que use `typeof`, `Window`, `Window.document` y `Document.createElement()` para determinar si el DOM está disponible. Utilice el hook `useState()` para definir la variable de estado `inBrowser` y el hook `useEffect()` para actualizarla y limpiarla al final. Utilice el hook `useMemo()` para memoizar los valores de retorno del hook personalizado.

Aquí está el código:

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return (
    <p>
      {isBrowser
        ? "Ejecutándose en el navegador"
        : "Ejecutándose en el servidor"}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
