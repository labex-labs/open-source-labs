# Tarjeta que se desplaza

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una tarjeta que se desplace al pasar el cursor por encima, siga estos pasos:

1. Establezca la perspectiva adecuada en el elemento `.container` para permitir el efecto de desplazamiento.
2. Agregue una transición para la propiedad `transform` del elemento `.card`.
3. Utilice `Document.querySelector()` para seleccionar el elemento `.card` y agregue listeners de eventos para los eventos `mousemove` y `mouseout`.
4. Utilice `Element.getBoundingClientRect()` para obtener las coordenadas `x`, `y`, el ancho y el alto del elemento `.card`.
5. Calcule la distancia relativa como un valor entre `-1` y `1` para los ejes `x` e `y` y aplíquela a través de la propiedad `transform`.

A continuación, se muestra el código HTML y CSS de ejemplo para la tarjeta:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Tarjeta</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card.content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

Y aquí está el código JavaScript para agregar el efecto de pasar el cursor por encima:

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
