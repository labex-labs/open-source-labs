# Entrada con prefijo

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una entrada con un prefijo visual no editable, siga estos pasos:

1. Utilice `display: flex` para crear un elemento contenedor con la clase `.input-box`.
2. Quite el borde y el contorno del campo `<input>` y aplíquelos al elemento padre en su lugar para que se vea como una caja de entrada.
3. Utilice el selector de pseudo-clase `:focus-within` para dar estilo al elemento padre en consecuencia cuando el usuario interactúa con el campo `<input>`.

Aquí está el código HTML:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

Y aquí está el código CSS:

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
