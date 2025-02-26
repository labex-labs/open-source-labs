# Carrusel

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código renderiza un componente de carrusel. Estos son los pasos que sigue:

1. Utiliza el hook `useState()` para crear la variable de estado `active` y la inicializa en `0` (el índice del primer elemento del carrusel).
2. Utiliza el hook `useEffect()` para configurar un temporizador con `setTimeout()`. Cuando el temporizador se activa, actualiza el valor de `active` al índice del siguiente elemento del carrusel (utilizando el operador módulo para volver al principio si es necesario). También limpia el temporizador cuando el componente se desmonta.
3. Calcula la `className` para cada elemento del carrusel mapeando sobre ellos y aplicando la clase adecuada según si el elemento está actualmente activo o no.
4. Renderiza los elementos del carrusel utilizando `React.cloneElement()`, pasando cualquier otro prop utilizando `...rest`, y agregando la `className` calculada a cada elemento.

Los estilos CSS definen el diseño del carrusel y sus elementos. El contenedor del carrusel tiene `position: relative`, mientras que los elementos tienen `position: absolute` y `visibility: hidden` por defecto. Cuando un elemento está activo, obtiene una clase `visible`, que establece su `visibility` en `visible`.

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

Aquí está el código completo:

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
