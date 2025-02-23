# Relación de aspecto

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Este código crea un contenedor reactivo con una relación de aspecto específica utilizando propiedades personalizadas de CSS y la función `calc()`. Siga estos pasos para lograr esto:

1. Defina la relación de aspecto deseada utilizando una propiedad personalizada de CSS, `--aspect-ratio`.
2. Establezca la propiedad `position` del elemento contenedor en `relative` y su propiedad `height` en `0`.
3. Calcule la altura del elemento contenedor utilizando la función `calc()` y la propiedad personalizada `--aspect-ratio`, y asígnela como la propiedad `padding-bottom`.
4. Establezca el hijo directo del elemento contenedor en `position: absolute`, `top: 0`, `left: 0`, `width: 100%` y `height: 100%`.
5. Mantenga la relación de aspecto del elemento hijo estableciendo su propiedad `object-fit` en `cover`.

Utilice el siguiente código HTML y CSS para crear el contenedor:

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
