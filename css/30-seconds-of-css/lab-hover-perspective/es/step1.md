# Transformación en perspectiva al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una transformación en perspectiva con una animación al pasar el cursor sobre un elemento:

1. Utilice la propiedad `transform` con las funciones `perspective()` y `rotateY()` para aplicar una perspectiva al elemento. Por ejemplo, para crear una perspectiva izquierda, use `transform: perspective(1500px) rotateY(15deg);`. Para crear una perspectiva derecha, use `transform: perspective(1500px) rotateY(-15deg);`.

2. Utilice la propiedad `transition` para animar la propiedad `transform` cuando el elemento está siendo sobrevolado. Por ejemplo, `transition: transform 1s ease 0s;`.

3. Para reflejar el efecto en perspectiva de izquierda a derecha, cambie el valor de `rotateY()` a negativo en la perspectiva derecha. Por ejemplo, use `transform: perspective(1500px) rotateY(-15deg);`.

Ejemplo de HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Ejemplo de CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
