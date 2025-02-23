# Girador de Donas

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para indicar la carga del contenido, crea un girador de donas con un `bordesemi-transparente` para todo el elemento. Excluye un lado para servir como indicador de carga de la dona. Luego, define y utiliza una animación adecuada, utilizando `transform: rotate()` para rotar el elemento. Aquí hay un ejemplo de código en HTML y CSS:

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
