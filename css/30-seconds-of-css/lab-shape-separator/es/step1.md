# Separador de formas

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un elemento separador entre dos bloques diferentes utilizando una forma SVG, siga estos pasos:

1. Utilice el pseudo-elemento `::after`.
2. Agregue la forma SVG (un triángulo de 24x12) a través de una URI de datos utilizando la propiedad `background-image`. La imagen de fondo se repetirá por defecto y cubrirá toda la área del pseudo-elemento.
3. Establezca el color deseado para el separador utilizando la propiedad `background` del elemento padre.

Utilice el siguiente código HTML:

```html
<div class="shape-separator"></div>
```

Y aplique las siguientes reglas CSS:

```css
.shape-separator {
  position: relative;
  height: 48px;
  background: #9c27b0;
}

.shape-separator::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 12'%3E%3Cpath d='m12 0l12 12h-24z' fill='transparent'/%3E%3C/svg%3E");
  position: absolute;
  width: 100%;
  height: 12px;
  bottom: 0;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
