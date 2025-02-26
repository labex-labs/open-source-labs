# Sternenbewertung

> In der VM wurden bereits `index.html` und `script.js` zur Verfügung gestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Erstellen Sie eine `Star`-Komponente, die jeden einzelnen Stern mit einem passenden Aussehen basierend auf dem Zustand der übergeordneten Komponente rendert. Definieren Sie dann eine `StarRating`-Komponente, die den `useState()`-Hook verwendet, um die `rating`- und `selection`-Zustandsvariablen mit passenden Anfangswerten zu definieren.

In `StarRating` erstellen Sie eine Methode namens `hoverOver`, die `selection` gemäß dem bereitgestellten `event` aktualisiert. Wenn `event` nicht bereitgestellt wird oder es `null` ist, setzen Sie `selection` auf `0`. Verwenden Sie das `.data-star-id`-Attribut des Ziels des Ereignisses, um den Wert von `selection` zu bestimmen.

Als Nächstes erstellen Sie ein Array von 5 Elementen mit `Array.from()` und erstellen Sie einzelne `<Star>`-Komponenten mit `Array.prototype.map()`. Behandeln Sie die `onMouseOver`- und `onMouseLeave`-Ereignisse des umschließenden Elements mit `hoverOver`. Behandeln Sie das `onClick`-Ereignis mit `setRating`.

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

Schließlich rendern Sie die `StarRating`-Komponente mit einem Anfangswert von `2`, indem Sie `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);` aufrufen.

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
