# Animación de caja con sombra al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una caja con sombra alrededor del texto cuando se pasa el cursor sobre él, siga estos pasos:

1. Establezca `transform: perspective(1px)` para dar al elemento un espacio tridimensional afectando la distancia entre el plano Z y el usuario, y `translateZ(0)` para reposicionar el elemento `p` a lo largo del eje z en el espacio tridimensional.
2. Utilice `box-shadow` para hacer que la caja sea transparente.
3. Habilite transiciones para tanto `box-shadow` como `transform` utilizando la propiedad `transition-property`.
4. Aplique una nueva `box-shadow` y `transform: scale(1.2)` para cambiar la escala del texto utilizando los selectores pseudo-clases `:hover`, `:active` y `:focus`.
5. Agregue la clase `hover-shadow-box-animation` al elemento `p`.

Aquí está el código HTML:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

Y aquí está el código CSS:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
