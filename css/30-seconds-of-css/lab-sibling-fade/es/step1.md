# Sibling Fade

`index.html` y `style.css` ya se han proporcionado en la VM.

Para desvanecer a los hermanos de un elemento sobre el que se pasa el cursor:

1. Anima los cambios de `opacidad` utilizando la propiedad `transition`.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Cambia la `opacidad` de todos los elementos excepto el que el mouse está sobre a `0.5` utilizando los selectores pseudo-clase `:hover` y `:not`.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Aquí hay un ejemplo de código HTML:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
