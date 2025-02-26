# React useTitle Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para establecer el título de la página, se puede usar el hook personalizado `useTitle`. Este hook utiliza `typeof` para comprobar si `Document` está definido. Si está definido, se utiliza el hook `useRef()` para almacenar el título original del `Document`. Luego, se utiliza el hook `useEffect()` para establecer `Document.title` con el valor pasado cuando el componente se monta y limpiar cuando se desmonta.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

En el código de ejemplo, el componente `Alert` utiliza el hook `useTitle` para establecer el título en "Alert". El componente `MyApp` renderiza un botón que alterna el componente `Alert`.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>¡Alerta! El título ha cambiado</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>Alternar alerta</button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
