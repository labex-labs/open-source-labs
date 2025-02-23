# Botón de radio personalizado

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un botón de radio con estilo y animación al cambiar de estado, siga estos pasos:

1. Cree un `.radio-container` usando flexbox para crear el diseño adecuado para los botones de radio.
2. Restablezca los estilos en el `<input>` y úselo para crear el contorno y el fondo del botón de radio.
3. Utilice el elemento `::before` para crear el círculo interno del botón de radio.
4. Cree un efecto de animación al cambiar de estado usando `transform: scale(1)` y una transición CSS.

A continuación, se muestra un fragmento de código HTML de ejemplo:

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

Y aquí está el CSS correspondiente:

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
