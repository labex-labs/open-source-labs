# Texto con degradado

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para darle un color degradado al texto, puedes utilizar propiedades de CSS. Primero, utiliza la propiedad `background` con un valor de `linear-gradient()` para darle al elemento de texto un fondo degradado. Luego, utiliza `webkit-text-fill-color: transparent` para rellenar el texto con un color transparente. Finalmente, utiliza `webkit-background-clip: text` para recortar el fondo con el texto y rellenar el texto con el fondo degradado como color. Aquí hay un fragmento de código de ejemplo:

```html
<p class="gradient-text">Texto con degradado</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
