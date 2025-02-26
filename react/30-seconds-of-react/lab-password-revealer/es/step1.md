# Alternador de Mostrar/Ocultar Contraseña

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

El siguiente código muestra un campo de entrada de contraseña con un botón de revelación. Utiliza el hook `useState()` para crear la variable de estado `shown` y establecer su valor inicial en `false`. Cuando se hace clic en el botón `Mostrar/Ocultar`, se llama a la función `setShown`, lo que alterna el `type` del input entre `'text'` y `'password'`.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Mostrar/Ocultar</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
