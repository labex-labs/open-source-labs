# Mostrar contenido adicional al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una tarjeta que muestre contenido adicional al pasar el cursor sobre ella, siga estos pasos:

1. Utilice `overflow: hidden` en la tarjeta para ocultar cualquier elemento que desborde verticalmente.
2. Utilice los selectores de pseudo-clases `:hover` y `:focus-within` para cambiar el estilo de la tarjeta cuando el elemento se pasa el cursor sobre él, está enfocado o cualquiera de sus descendientes está enfocado.
3. Establezca `transition: 0.3s ease all` para crear un efecto de transición suave al pasar el cursor sobre/enfocar.

A continuación, se muestra un ejemplo de código HTML para la tarjeta:

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

Y aquí está el código CSS para dar estilo a la tarjeta:

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
