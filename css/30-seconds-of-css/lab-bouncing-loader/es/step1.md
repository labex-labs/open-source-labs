# Cargador rebotante

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación de cargador rebotante:

1. Defina una animación `@keyframes` que use las propiedades `opacity` y `transform`, con una traducción en un solo eje en `transform: translate3d()` para una mejor rendimiento.
2. Cree un contenedor padre con la clase `.bouncing-loader` que use `display: flex` y `justify-content: center` para centrar los círculos rebotantes.
3. Asigne a los tres elementos `<div>` de los círculos rebotantes el mismo `width`, `height` y `border-radius: 50%` para que queden circulares.
4. Aplique la animación `bouncing-loader` a cada uno de los tres círculos rebotantes.
5. Utilice un `animation-delay` diferente para cada círculo y `animation-direction: alternate` para crear el efecto adecuado.

Aquí está el código HTML:

```html
<div class="bouncing-loader">
  <div></div>
  <div></div>
  <div></div>
</div>
```

Y aquí está el código CSS:

```css
@keyframes bouncing-loader {
  to {
    opacity: 0.1;
    transform: translate3d(0, -16px, 0);
  }
}

.bouncing-loader {
  display: flex;
  justify-content: center;
}

.bouncing-loader > div {
  width: 16px;
  height: 16px;
  margin: 3rem 0.2rem;
  background: #8385aa;
  border-radius: 50%;
  animation: bouncing-loader 0.6s infinite alternate;
}

.bouncing-loader > div:nth-child(2) {
  animation-delay: 0.2s;
}

.bouncing-loader > div:nth-child(3) {
  animation-delay: 0.4s;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
