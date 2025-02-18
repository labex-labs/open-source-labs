# Alerta Cerrable

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `script.js` y `style.css`.

Renderiza un componente de alerta con la propiedad `type`.

El componente `Alert` recibe las siguientes propiedades:

- `isDefaultShown`: un valor booleano que determina si la alerta se muestra inicialmente o no (el valor predeterminado es `false`).
- `timeout`: un número que especifica la duración en milisegundos antes de que la alerta se desvanezca (el valor predeterminado es `250`).
- `type`: una cadena que determina el tipo de alerta (por ejemplo, "warning", "error", "info").
- `message`: una cadena que contiene el mensaje a mostrar en la alerta.

El componente realiza lo siguiente:

- Utiliza el hook `useState()` para crear las variables de estado `isShown` e `isLeaving` y las establece en `false` inicialmente.
- Define una variable `timeoutId` para mantener la instancia del temporizador y limpiarla cuando el componente se desmonte.
- Utiliza el hook `useEffect()` para actualizar el valor de `isShown` a `true` y limpiar el intervalo utilizando `timeoutId` cuando el componente se desmonte.
- Define una función `closeAlert` para establecer que el componente se quite del DOM mostrando una animación de desvanecimiento y estableciendo `isShown` en `false` a través de `setTimeout()`.
- Renderiza el componente de alerta si `isShown` es `true`. El componente tiene los estilos adecuados según la propiedad `type` y se desvanece si `isLeaving` es `true`.

Aquí está el código:

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
