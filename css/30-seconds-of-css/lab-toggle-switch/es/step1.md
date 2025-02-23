# Interruptor con conmutación

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Aquí hay una versión más concisa y clara del contenido:

Para crear un interruptor con conmutación solo con CSS, siga estos pasos:

1. Asocie la etiqueta `<label>` con el elemento `<input>` de casilla de verificación utilizando el atributo `for`.
2. Utilice el pseudo-elemento `::after` de la etiqueta `<label>` para crear un mango circular para el interruptor.
3. Utilice el selector de pseudo-clase `:checked` para cambiar la posición del mango, utilizando `transform: translateX(20px)` y el `background-color` del interruptor.
4. Oculte visualmente el elemento `<input>` utilizando `position: absolute` y `left: -9999px`.

Aquí está el código HTML:

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

Aquí está el código CSS:

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
