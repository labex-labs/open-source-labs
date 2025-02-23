# Cargador de pulso

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación del cargador con efecto de pulso utilizando la propiedad `animation-delay`, siga estos pasos:

1. Utilice `@keyframes` para definir una animación para dos elementos `<div>`. Establezca el punto de partida (`0%`) para ambos elementos para que no tengan `width` o `height` y estén posicionados en el centro. Para el punto final (`100%`), que ambos elementos aumenten en `width` y `height`, pero restablezcan su `position` a `0`.
2. Utilice `opacity` para la transición de `1` a `0` al animar para dar a los elementos `<div>` un efecto de desaparición a medida que se expanden.
3. Establezca un `width` y `height` predefinidos para el contenedor padre, `.ripple-loader`. Utilice `position: relative` para posicionar sus hijos.
4. Utilice `animation-delay` en el segundo elemento `<div>`, para que cada elemento inicie su animación en un momento diferente.

A continuación, se muestra el código HTML y CSS para lograr esto:

```html
<div class="ripple-loader">
  <div></div>
  <div></div>
</div>
```

```css
.ripple-loader {
  position: relative;
  width: 64px;
  height: 64px;
}

.ripple-loader div {
  position: absolute;
  border: 4px solid #454ade;
  border-radius: 50%;
  animation: ripple-loader 1s ease-out infinite;
}

.ripple-loader div:nth-child(2) {
  animation-delay: -0.5s;
}

@keyframes ripple-loader {
  0% {
    top: 32px;
    left: 32px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0;
    left: 0;
    width: 64px;
    height: 64px;
    opacity: 0;
  }
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
