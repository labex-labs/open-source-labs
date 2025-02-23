# Lista con títulos de sección flotantes

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una lista con títulos flotantes para cada sección, siga estos pasos:

1. Aplique `overflow-y: auto` al contenedor de la lista para permitir el desbordamiento vertical.
2. Utilice `display: grid` en el contenedor interno (`<dl>`) para crear un diseño con dos columnas.
3. Establezca los títulos (`<dt>`) en `grid-column: 1` y el contenido (`<dd>`) en `grid-column: 2`.
4. Finalmente, aplique `position: sticky` y `top: 0.5rem` a los títulos para crear un efecto flotante.

Aquí está el código HTML:

```html
<div class="container">
  <div class="floating-stack">
    <dl>
      <dt>A</dt>
      <dd>Argelia</dd>
      <dd>Angola</dd>

      <dt>B</dt>
      <dd>Benín</dd>
      <dd>Botswana</dd>
      <dd>Burkina Faso</dd>
      <dd>Burundi</dd>

      <dt>C</dt>
      <dd>Cabo Verde</dd>
      <dd>Camerún</dd>
      <dd>República Centroafricana</dd>
      <dd>Tchad</dd>
      <dd>Comoras</dd>
      <dd>Congo, República Democrática del</dd>
      <dd>Congo, República del</dd>
      <dd>Costa de Marfil</dd>

      <dt>D</dt>
      <dd>Yibuti</dd>

      <dt>E</dt>
      <dd>Egipto</dd>
      <dd>Guinea Ecuatorial</dd>
      <dd>Eritrea</dd>
      <dd>Eswatini (anteriormente Suazilandia)</dd>
      <dd>Etiopía</dd>
    </dl>
  </div>
</div>
```

Y aquí está el código CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns: 2.5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0.5rem;
  left: 0.5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding: 0.25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0.75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0.25rem;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
