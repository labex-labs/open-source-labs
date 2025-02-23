# Transición de altura

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Este fragmento de código realiza una transición en la altura de un elemento desde `0` hasta `auto` cuando su altura es desconocida mediante los siguientes pasos:

- Utiliza la propiedad `transition` para especificar que los cambios en `max-height` deben transicionarse durante un período de `0,3 s`.
- Utiliza la propiedad `overflow` establecida en `hidden` para evitar que el contenido del elemento oculto desborde su contenedor.
- Utiliza la propiedad `max-height` para especificar una altura inicial de `0`.
- Utiliza la pseudo-clase `:hover` para cambiar `max-height` al valor de la variable `--max-height` establecida por JavaScript.
- Utiliza la propiedad `Element.scrollHeight` y el método `CSSStyleDeclaration.setProperty()` para establecer el valor de `--max-height` en la altura actual del elemento.
- **Nota:** Este enfoque provoca un reflujo en cada fotograma de animación, lo que puede causar retrasos cuando hay un gran número de elementos debajo del elemento en transición.

```html
<div class="trigger">
  Pasa el cursor por encima de mí para ver una transición de altura.
  <div class="el">Contenido adicional</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
