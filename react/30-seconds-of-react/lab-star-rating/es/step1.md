# Puntuación de estrellas

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Crea un componente `Star` que muestre cada estrella individual con la apariencia adecuada según el estado del componente padre. Luego, define un componente `StarRating` que use el hook `useState()` para definir las variables de estado `rating` y `selection` con los valores iniciales adecuados.

En `StarRating`, crea un método llamado `hoverOver` que actualice `selection` de acuerdo con el `evento` proporcionado. Si `evento` no se proporciona o es `null`, restablece `selection` a `0`. Utiliza el atributo `.data-star-id` del destino del evento para determinar el valor de `selection`.

A continuación, crea una matriz de 5 elementos usando `Array.from()` y crea componentes individuales `<Star>` usando `Array.prototype.map()`. Maneja los eventos `onMouseOver` y `onMouseLeave` del elemento envolvente usando `hoverOver`. Maneja el evento `onClick` usando `setRating`.

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

Finalmente, renderiza el componente `StarRating` con un valor inicial de `2` llamando a `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
