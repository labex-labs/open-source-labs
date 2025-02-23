# Círculo

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una forma circular usando puro CSS, utiliza la propiedad `border-radius: 50%` para curvar los bordes del elemento. Asegúrate de establecer tanto `width` como `height` con el mismo valor para asegurar un círculo perfecto. Si se usan valores diferentes, se creará una elipse en lugar de eso. Aquí hay un fragmento de código de ejemplo:

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
