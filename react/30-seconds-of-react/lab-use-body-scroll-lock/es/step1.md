# React useBodyScrollLock Hook

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este fragmento de código permite a los usuarios bloquear el desplazamiento del cuerpo cuando un modal está abierto. Aquí está cómo funciona:

Primero, se define la función `useBodyScrollLock`, que utiliza el hook `useLayoutEffect` para bloquear el desplazamiento del elemento `body`. Este hook se ejecuta solo una vez cuando el componente se monta, y establece el valor de `overflow` del elemento `body` en `'hidden'`. Cuando el componente se desmonta, se restaura el valor original de `overflow`.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Luego, se define el componente `Modal`, que utiliza la función `useBodyScrollLock`. Este componente muestra un mensaje en una caja que está centrada en la pantalla. Cuando se hace clic en la caja, el modal se cierra y el desplazamiento del cuerpo se desbloquea.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll bloqueado! <br /> Haz clic en mí para desbloquear
      </p>
    </div>
  );
};
```

Finalmente, se define el componente `MyApp`, que renderiza un botón que abre el componente `Modal` cuando se hace clic en él.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Abrir modal</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
