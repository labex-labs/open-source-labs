# Imagen con texto superpuesto

`index.html` y `style.css` ya se han proporcionado en la VM.

Para mostrar una imagen con un texto superpuesto, utiliza los elementos `<figure>` y `<figcaption>`. Utiliza la propiedad `linear-gradient` en CSS para crear el efecto de superposición sobre la imagen. Aquí hay un fragmento de código de ejemplo:

```html
<figure class="text-overlay-image">
  <img src="https://picsum.photos/id/971/400/400.jpg" />
  <figcaption>
    <h3>Business <br />Pricing</h3>
  </figcaption>
</figure>
```

```css
.text-overlay-image {
  box-sizing: border-box;
  position: relative;
  margin: 8px;
  max-width: 400px;
  max-height: 400px;
  width: 100%;
}

.text-overlay-image figcaption {
  box-sizing: border-box;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(0deg, #00000088 30%, #ffffff44 100%);
  color: #fff;
  padding: 16px;
  font: 700 28px/1.2 sans-serif;
}

.text-overlay-image figcaption h3 {
  margin: 0;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
