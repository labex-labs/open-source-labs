# Verschiebender Karteneffekt

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Karte zu erstellen, die beim Hovern verschiebt, folgen Sie diesen Schritten:

1. Setzen Sie die passende `Perspektive` auf das `.container`-Element, um den Verschiebeeffekt zu ermöglichen.
2. Fügen Sie eine `Transition` für die `transform`-Eigenschaft des `.card`-Elements hinzu.
3. Verwenden Sie `Document.querySelector()`, um das `.card`-Element auszuwählen und Eventlistener für die `mousemove`- und `mouseout`-Ereignisse hinzuzufügen.
4. Verwenden Sie `Element.getBoundingClientRect()`, um die `x`, `y`, `Breite` und `Höhe` des `.card`-Elements zu erhalten.
5. Berechnen Sie die relative Entfernung als Wert zwischen `-1` und `1` für die `x`- und `y`-Achsen und wenden Sie sie über die `transform`-Eigenschaft an.

Hier ist der Beispiel-HTML- und CSS-Code für die Karte:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Karte</h3>
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

Und hier ist der JavaScript-Code, um den Hover-Effekt hinzuzufügen:

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

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
