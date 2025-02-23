# Triángulo

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una forma triangular con CSS puro, siga estos pasos:

1. Utilice tres bordes con el mismo `border-width` (`20px`) para crear la forma triangular.
2. Establezca el `border-color` del lado opuesto al que apunta el triángulo al color deseado. Los bordes adyacentes deben tener un `border-color` de `transparent`.
3. Para ajustar el tamaño del triángulo, altere los valores de `border-width`.

A continuación, se muestra un fragmento de código de ejemplo:

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
