# Barra de progreso de desplazamiento (Scroll Progress Bar)

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear una barra de progreso que muestre el porcentaje de desplazamiento de una página web, sigue estos pasos:

1. Agrega un elemento `div` con el `id` "scroll-progress" al código HTML.
2. En el código CSS, establece la `position` del elemento en `fixed`, el `top` en `0`, el `width` en `0%`, la `height` en `4px` y el color de `background` en `#7983ff`.
3. Establece el valor de `z-index` en un número grande para asegurarte de que la barra de progreso se coloque en la parte superior de la página y por encima de cualquier contenido.
4. En el código JavaScript, selecciona el elemento `scroll-progress` utilizando el método `document.getElementById()`.
5. Calcula la altura de la página web utilizando la fórmula `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6. Agrega un detector de eventos (event listener) al objeto `window` que escuche el evento `scroll`.
7. En la función del detector de eventos, calcula el porcentaje de desplazamiento del documento utilizando la fórmula `(scrollTop / height) * 100`.
8. Establece el `width` del elemento `scroll-progress` al porcentaje de desplazamiento utilizando la propiedad `style`.

Aquí está el código:

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
