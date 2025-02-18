# Seguimiento de Gradiente del Cursor del Mouse

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear un efecto de hover en el que el gradiente siga el cursor del mouse, sigue estos pasos:

1. Declara dos variables CSS, `--x` y `--y`, para seguir la posición del mouse en el botón.
2. Declara una variable CSS, `--size`, para modificar las dimensiones del gradiente.
3. Utiliza `background: radial-gradient(circle closest-side, pink, transparent)` para crear el gradiente en la posición correcta.
4. Registra un manejador para el evento `'mousemove'` utilizando `Document.querySelector()` y `EventTarget.addEventListener()`.
5. Actualiza los valores de las variables CSS `--x` y `--y` utilizando `Element.getBoundingClientRect()` y `CSSStyleDeclaration.setProperty()`.

Aquí está el código HTML para el botón:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

Y aquí está el código CSS:

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Finalmente, aquí está el código JavaScript:

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.
