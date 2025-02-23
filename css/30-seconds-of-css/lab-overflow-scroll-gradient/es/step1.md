# Degradado de desplazamiento con desbordamiento

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para agregar un degradado con desvanecimiento a un elemento con desbordamiento e indicar que hay más contenido que se puede desplazar, siga estos pasos:

1. Utilice el pseudo-elemento `::after` para crear un `linear-gradient()` que desvanezca de `transparent` a `white` (de arriba hacia abajo).
2. Coloque y mida el pseudo-elemento en su padre utilizando `position: absolute`, `width` y `height`.
3. Excluya el pseudo-elemento de los eventos del mouse utilizando `pointer-events: none`, lo que permite que el texto detrás de él siga siendo seleccionable/interactivo.

A continuación, se muestra un fragmento de código HTML y CSS de ejemplo:

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
