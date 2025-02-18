# Botón con Efecto de Onda (Ripple Effect)

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `script.js` y `style.css`.

Este código renderiza un componente de botón que crea un efecto de onda (ripple effect) cuando se hace clic en él. Así es cómo funciona:

- El hook `useState()` se utiliza para crear dos variables de estado: `coords` e `isRippling`. La variable `coords` almacena las coordenadas del puntero, mientras que `isRippling` almacena el estado de la animación del botón.
- Un hook `useEffect()` se utiliza para cambiar el valor de `isRippling` cada vez que cambia la variable de estado `coords`. Esto inicia la animación del efecto de onda.
- `setTimeout()` se utiliza en el hook anterior para borrar la animación después de que termine de reproducirse.
- Otro hook `useEffect()` se utiliza para restablecer `coords` siempre que la variable de estado `isRippling` sea `false`.
- El evento `onClick` se maneja actualizando la variable de estado `coords` y llamando a la función de devolución de llamada (callback) pasada.

Aquí está el código para el componente `RippleButton`:

```jsx
const RippleButton = ({ children, onClick }) => {
  const [coords, setCoords] = React.useState({ x: -1, y: -1 });
  const [isRippling, setIsRippling] = React.useState(false);

  React.useEffect(() => {
    if (coords.x !== -1 && coords.y !== -1) {
      setIsRippling(true);
      setTimeout(() => setIsRippling(false), 300);
    } else setIsRippling(false);
  }, [coords]);

  React.useEffect(() => {
    if (!isRippling) setCoords({ x: -1, y: -1 });
  }, [isRippling]);

  return (
    <button
      className="ripple-button"
      onClick={(e) => {
        const rect = e.target.getBoundingClientRect();
        setCoords({ x: e.clientX - rect.left, y: e.clientY - rect.top });
        onClick && onClick(e);
      }}
    >
      {isRippling && (
        <span
          className="ripple"
          style={{
            left: coords.x,
            top: coords.y
          }}
        />
      )}
      <span className="content">{children}</span>
    </button>
  );
};
```

Puedes usar este componente de la siguiente manera:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <RippleButton onClick={(e) => console.log(e)}>Click me</RippleButton>
);
```

Y aquí está el CSS para el componente `RippleButton`:

```css
.ripple-button {
  border-radius: 4px;
  border: none;
  margin: 8px;
  padding: 14px 24px;
  background: #1976d2;
  color: #fff;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.ripple-button > .ripple {
  width: 20px;
  height: 20px;
  position: absolute;
  background: #63a4ff;
  display: block;
  content: "";
  border-radius: 9999px;
  opacity: 1;
  animation: 0.9s ease 1 forwards ripple-effect;
}

@keyframes ripple-effect {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(10);
    opacity: 0.375;
  }
  100% {
    transform: scale(35);
    opacity: 0;
  }
}

.ripple-button > .content {
  position: relative;
  z-index: 2;
}
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
