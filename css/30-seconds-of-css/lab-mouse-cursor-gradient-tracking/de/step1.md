# Verfolgung des Farbverlaufs (Gradient) mit dem Mauszeiger

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um einen Hover-Effekt zu erstellen, bei dem der Farbverlauf (Gradient) dem Mauszeiger folgt, gehen Sie wie folgt vor:

1. Deklarieren Sie zwei CSS-Variablen, `--x` und `--y`, um die Position des Mauszeigers auf der Schaltfläche zu verfolgen.
2. Deklarieren Sie eine CSS-Variable, `--size`, um die Abmessungen des Farbverlaufs (Gradient) zu ändern.
3. Verwenden Sie `background: radial-gradient(circle closest-side, pink, transparent)`, um den Farbverlauf (Gradient) an der richtigen Position zu erstellen.
4. Registrieren Sie einen Handler für das `'mousemove'`-Ereignis mit `Document.querySelector()` und `EventTarget.addEventListener()`.
5. Aktualisieren Sie die Werte der CSS-Variablen `--x` und `--y` mit `Element.getBoundingClientRect()` und `CSSStyleDeclaration.setProperty()`.

Hier ist der HTML-Code für die Schaltfläche:

```html
<button class="mouse-cursor-gradient-tracking">
  <span>Hover me</span>
</button>
```

Und hier ist der CSS-Code:

```css
.mouse-cursor-gradient-tracking {
  position: relative;
  background: #7983ff;
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  border: none;
  color: white;
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.mouse-cursor-gradient-tracking span {
  position: relative;
}

.mouse-cursor-gradient-tracking::before {
  --size: 0;
  content: "";
  position: absolute;
  left: var(--x);
  top: var(--y);
  width: var(--size);
  height: var(--size);
  background: radial-gradient(circle closest-side, pink, transparent);
  transform: translate(-50%, -50%);
  transition:
    width 0.2s ease,
    height 0.2s ease;
}

.mouse-cursor-gradient-tracking:hover::before {
  --size: 200px;
}
```

Schließlich ist hier der JavaScript-Code:

```js
let btn = document.querySelector(".mouse-cursor-gradient-tracking");
btn.addEventListener("mousemove", (e) => {
  let rect = e.target.getBoundingClientRect();
  let x = e.clientX - rect.left;
  let y = e.clientY - rect.top;
  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
});
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
