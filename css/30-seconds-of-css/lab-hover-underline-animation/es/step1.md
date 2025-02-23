# Animación de subrayado al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un efecto de subrayado animado cuando el usuario pase el cursor sobre el texto, siga estos pasos:

1. Utilice `display: inline-block` para que el subrayado cubra solo el ancho del contenido del texto.
2. Utilice el pseudo-elemento `::after` con `width: 100%` y `position: absolute` para colocarlo debajo del contenido.
3. Utilice `transform: scaleX(0)` para ocultar inicialmente el pseudo-elemento.
4. Utilice el selector de pseudo-clase `:hover` para aplicar `transform: scaleX(1)` y mostrar el pseudo-elemento al pasar el cursor.
5. Anime `transform` utilizando `transform-origin: left` y una transición adecuada.
6. Quite la propiedad `transform-origin` para que la transformación origine desde el centro del elemento.

A continuación, se muestra un ejemplo de código HTML para aplicar el efecto a un elemento de texto:

```html
<p class="hover-underline-animation">
  Pase el cursor sobre este texto para ver el efecto!
</p>
```

Y aquí está el código CSS correspondiente:

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
