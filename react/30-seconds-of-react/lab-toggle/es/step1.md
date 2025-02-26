# Conmutación (Toggle)

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para renderizar un componente de conmutación, siga estos pasos:

1. Utilice el hook `useState()` para inicializar la variable de estado `isToggledOn` con `defaultToggled`.
2. Renderice un elemento `<input>` y asocie su evento `onClick` para actualizar la variable de estado `isToggledOn`. Aplique la `className` adecuada al elemento `<label>` envolvente.
3. Utilice el siguiente CSS para dar estilo al componente de conmutación:

```css
.toggle input[type="checkbox"] {
  display: none;
}

.toggle.on {
  background-color: green;
}

.toggle.off {
  background-color: red;
}
```

Aquí está el código:

```jsx
const Toggle = ({ defaultToggled = false }) => {
  const [isToggleOn, setIsToggleOn] = React.useState(defaultToggled);

  return (
    <label className={isToggleOn ? "toggle on" : "toggle off"}>
      <input
        type="checkbox"
        checked={isToggleOn}
        onChange={() => setIsToggleOn(!isToggleOn)}
      />
      {isToggleOn ? "ON" : "OFF"}
    </label>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Toggle />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
