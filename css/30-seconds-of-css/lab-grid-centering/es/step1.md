# Centrado en una cuadrícula

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para centrar un elemento hijo tanto horizontal como verticalmente dentro de un elemento padre, siga estos pasos:

1. Cree un diseño de cuadrícula utilizando `display: grid`.
2. Utilice `justify-content: center` para centrar el hijo horizontalmente.
3. Utilice `align-items: center` para centrar el hijo verticalmente.

Aquí hay una estructura HTML de ejemplo:

```html
<div class="parent">
  <div class="child">Contenido centrado.</div>
</div>
```

Y el CSS correspondiente:

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
