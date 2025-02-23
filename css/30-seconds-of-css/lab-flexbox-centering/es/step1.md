# Centrado con Flexbox

`index.html` y `style.css` ya se han proporcionado en la VM.

Para centrar un elemento hijo tanto horizontal como verticalmente dentro de un elemento padre utilizando flexbox, siga estos pasos:

1. Cree un diseño con flexbox estableciendo la propiedad `display` del elemento padre en `flex`.
2. Utilice la propiedad `justify-content` para centrar el hijo horizontalmente estableciendo su valor en `center`.
3. Utilice la propiedad `align-items` para centrar el hijo verticalmente estableciendo su valor en `center`.
4. Agregue el elemento hijo dentro del elemento padre.

A continuación, se muestra un fragmento de código de ejemplo:

```html
<div class="flexbox-centering">
  <div>Contenido centrado.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
