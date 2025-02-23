# Tarjeta con recorte de imagen

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una tarjeta con un recorte de imagen, siga estos pasos:

1. Agregue un fondo coloreado a un elemento `.container` utilizando la propiedad `background`.
2. Cree un elemento `.card` y agregue un elemento `figure` dentro de él con la imagen deseada y cualquier otro contenido.
3. Utilice el pseudo-elemento `::before` para agregar un `border` alrededor del elemento `figure`. Establezca el color del borde para que coincida con el color de `background` del elemento `.container` para crear la ilusión de un recorte en la `.card`.

A continuación, se muestra un ejemplo de código HTML para la tarjeta:

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

Y aquí está el código CSS correspondiente:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
