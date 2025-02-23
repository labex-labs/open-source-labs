# Ajustar una imagen dentro de un contenedor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para ajustar una imagen dentro de su contenedor mientras se conserva su relación de aspecto, puedes usar `object-fit: contain`. Para llenar el contenedor con la imagen mientras se conserva su relación de aspecto, utiliza `object-fit: cover`. Si quieres posicionar la imagen en el centro del contenedor, puedes usar `object-position: center`.

Aquí hay un ejemplo de cómo puedes usar estas propiedades:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

Y el CSS correspondiente:

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
