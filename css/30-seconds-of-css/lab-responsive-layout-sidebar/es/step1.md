# Diseño adaptable con barra lateral

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un diseño adaptable con una área de contenido y una barra lateral, use `display: grid` en el contenedor padre, `minmax()` para la segunda columna (barra lateral) para permitir que ocupe entre `150px` y `20%`, y `1fr` para la primera columna (contenido principal) para ocupar el resto del espacio restante. Aquí hay un ejemplo de código HTML y CSS:

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
