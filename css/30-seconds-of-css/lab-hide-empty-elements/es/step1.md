# Ocultar elementos vacíos

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para ocultar elementos sin contenido, utiliza la pseudo-clase `:empty`. Por ejemplo, si tienes el siguiente código HTML:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

Puedes utilizar el siguiente código CSS para ocultar el elemento del botón sin contenido:

```css
p:empty {
  display: none;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
