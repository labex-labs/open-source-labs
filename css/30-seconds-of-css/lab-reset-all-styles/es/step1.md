# Restablece todos los estilos

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para restablecer todos los estilos a sus valores predeterminados, utiliza la propiedad `all`. Esta propiedad no afectará a las propiedades `direction` y `unicode-bidi`. Aquí hay un ejemplo de cómo utilizarla:

```html
<div class="reset-all-styles">
  <h5>Título</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
