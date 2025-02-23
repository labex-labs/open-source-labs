# Hijos Distribuidos Igualmente

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para distribuir los elementos hijos de manera equitativa dentro de un elemento padre, utiliza el diseño flexbox estableciendo la propiedad `display` del elemento padre en `flex`. Para distribuir los hijos horizontalmente con un espacio igual entre ellos, utiliza `justify-content: space-between`. Para distribuir los hijos con espacio alrededor de ellos, utiliza `justify-content: space-around`. Aquí hay un ejemplo:

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
