# React useSearchParam Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para seguir el parámetro de búsqueda de la ubicación del navegador, siga los siguientes pasos:

1. Cree una devolución de llamada usando el hook `useCallback()`. La devolución de llamada debe usar el constructor `URLSearchParams` para obtener el valor actual del parámetro deseado.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. Cree una variable de estado que almacene el valor actual del parámetro usando el hook `useState()`.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. Establezca los oyentes de eventos adecuados para actualizar la variable de estado al montar y limpíelos al desmontar usando el hook `useEffect()`.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

A continuación, se muestra un ejemplo de cómo usar este hook personalizado en un componente:

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Valor del parámetro post: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        Ver publicación 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Salir
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Este ejemplo crea un componente `MyApp` que usa el hook personalizado `useSearchParam` para seguir el valor del parámetro `post` en la búsqueda de ubicación. El valor de `post` se muestra en una etiqueta de párrafo. También se incluyen dos botones para demostrar cómo cambiar el valor del parámetro de búsqueda de ubicación.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
