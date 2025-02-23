# Tarjeta Giratoria

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una tarjeta de dos caras que gire al pasar el cursor, siga estos pasos:

1. Establezca la propiedad `backface-visibility` de las tarjetas en `none` para evitar que la cara posterior sea visible por defecto.
2. Inicialmente, establezca `rotateY(-180deg)` para la cara posterior de la tarjeta y `rotateY(0deg)` para la cara frontal de la tarjeta.
3. Al pasar el cursor, establezca `rotateY(180deg)` para la cara frontal de la tarjeta y `rotateY(0deg)` para la cara posterior de la tarjeta.
4. Establezca el valor adecuado de `perspectiva` para crear el efecto de rotación.

A continuación, se muestra un ejemplo de código HTML y CSS:

```html
<div class="card">
  <div class="card-side front">
    <div>Front Side</div>
  </div>
  <div class="card-side back">
    <div>Back Side</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
