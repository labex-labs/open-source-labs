# Reset de Box-Sizing

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para garantizar que el `ancho` y el `alto` de un elemento no se vean afectados por el `borde` o el `relleno`, utiliza la propiedad CSS `box-sizing: border-box`. Esto incluye el `relleno` y el `borde` en el cálculo del `ancho` y el `alto` del elemento. Si quieres heredar la propiedad `box-sizing` de un elemento padre, utiliza `box-sizing: inherit`.

Aquí hay un ejemplo de uso de la propiedad `box-sizing` con dos elementos `div`:

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

En este ejemplo, el primer elemento `div` tiene `box-sizing: border-box`, y el segundo elemento `div` tiene `box-sizing: content-box`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
