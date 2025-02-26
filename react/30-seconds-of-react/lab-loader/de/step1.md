# Rotierender Ladeindicator

> In der VM wurden bereits `index.html` und `script.js` zur Verfügung gestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

**Zeigt eine rotierende Ladekomponente an.**

Um eine rotierende Ladekomponente anzuzeigen, folgen Sie diesen Schritten:

1. Rendern Sie ein SVG-Element, dessen Maße durch die `size`-Eigenschaft bestimmt werden.
2. Verwenden Sie CSS, um das SVG zu animieren und eine Rotationsanimation zu erstellen. Spezifisch fügen Sie die `.loader`-Klasse zum SVG hinzu und legen Sie die `animation`-Eigenschaft auf `rotate 2s linear infinite` fest. Definieren Sie auch die `rotate`-Keyframes mit einer `transform`-Eigenschaft, die das SVG um 360 Grad rotiert.
3. Fügen Sie ein `circle`-Element zum SVG hinzu, das den rotierenden Kreis darstellt. Um den Kreis zu animieren, fügen Sie den `.loader circle`-Selector hinzu und legen Sie die `animation`-Eigenschaft auf `dash 1.5s ease-in-out infinite` fest. Definieren Sie auch die `dash`-Keyframes mit den `stroke-dasharray`- und `stroke-dashoffset`-Eigenschaften, die ein gestricheltes Strichmuster erzeugen, das sich um den Kreis bewegt.
4. Schließlich erstellen Sie eine `Loader`-Komponente, die das SVG mit der als Breite und Höhe Attribute übergebene `size`-Eigenschaft rendert.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

Um die `Loader`-Komponente mit einer Größe von 24 zu verwenden, rufen Sie `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);` auf.

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
