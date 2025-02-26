# Carousel

> In der VM wurden bereits `index.html` und `script.js` bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Dieser Code rendert eine Carousel - Komponente. Hier sind die Schritte, die er ausführt:

1. Es verwendet den Hook `useState()`, um die `active` - Zustandsvariable zu erstellen und initialisiert sie mit `0` (dem Index des ersten Elements im Carousel).
2. Es verwendet den Hook `useEffect()`, um einen Timer mit `setTimeout()` einzurichten. Wenn der Timer abläuft, aktualisiert es den Wert von `active` auf den Index des nächsten Elements im Carousel (mit dem Modulo - Operator, um ggf. zurück zum Anfang zu springen). Es bereinigt auch den Timer, wenn die Komponente abmontiert wird.
3. Es berechnet die `className` für jedes Carousel - Element, indem es über sie iteriert und die passende Klasse basierend darauf anwendet, ob das Element aktuell aktiv ist oder nicht.
4. Es rendert die Carousel - Elemente mit `React.cloneElement()`, übergibt alle zusätzlichen Props mit `...rest` und fügt die berechnete `className` zu jedem Element hinzu.

Die CSS - Stile definieren das Layout des Carousels und seiner Elemente. Der Carousel - Container hat `position: relative`, während die Elemente standardmäßig `position: absolute` und `visibility: hidden` haben. Wenn ein Element aktiv ist, bekommt es eine `visible` - Klasse, die seine `Visibility` auf `visible` setzt.

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

Hier ist der vollständige Code:

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

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
