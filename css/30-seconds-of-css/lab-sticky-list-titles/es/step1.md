# Lista con Encabezados de Sección Pegajosos

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una lista con encabezados pegajosos para cada sección, siga estos pasos:

1. Permita que el contenedor de la lista (`<dl>`) desborde verticalmente utilizando `overflow-y: auto`.
2. Pegue los encabezados (`<dt>`) en la parte superior del contenedor estableciendo su `posición` en `pegajosa` y aplicando `top: 0`.
3. Utilice el siguiente código HTML y CSS:

HTML:

```html
<div class="container">
  <dl class="sticky-stack">
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
```

CSS:

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
