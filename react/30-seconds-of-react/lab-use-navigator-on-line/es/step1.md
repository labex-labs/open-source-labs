# React useNavigatorOnLine Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para comprobar si el cliente está en línea o fuera de línea, se puede crear una función `getOnLineStatus` que utilice la API web `Navigator.onLine`. Luego, para implementar esta funcionalidad en un componente React, se puede usar el hook personalizado `useNavigatorOnLine`. Este hook crea una variable de estado llamada `status` usando el hook `useState()` y la establece con el valor devuelto por `getOnLineStatus()`. El hook `useEffect()` se utiliza para agregar listeners de eventos para cuando cambia el estado de conexión en línea / fuera de línea, actualizar la variable de estado `status` en consecuencia y limpiar esos listeners cuando el componente se desmonta. Finalmente, la variable `isOnline` devuelta por `useNavigatorOnLine()` se puede usar para renderizar un mensaje que indique si el cliente está en línea o fuera de línea.

```jsx
const getOnLineStatus = () =>
  typeof navigator !== "undefined" && typeof navigator.onLine === "boolean"
    ? navigator.onLine
    : true;

const useNavigatorOnLine = () => {
  const [status, setStatus] = React.useState(getOnLineStatus());

  const setOnline = () => setStatus(true);
  const setOffline = () => setStatus(false);

  React.useEffect(() => {
    window.addEventListener("online", setOnline);
    window.addEventListener("offline", setOffline);

    return () => {
      window.removeEventListener("online", setOnline);
      window.removeEventListener("offline", setOffline);
    };
  }, []);

  return status;
};

const StatusIndicator = () => {
  const isOnline = useNavigatorOnLine();

  return <span>You are {isOnline ? "online" : "offline"}.</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <StatusIndicator />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
