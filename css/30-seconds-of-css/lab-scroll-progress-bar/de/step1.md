# Scrollfortschrittsleiste

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um eine Fortschrittsleiste zu erstellen, die den Scrollprozentsatz einer Webseite anzeigt, befolgen Sie diese Schritte:

1. Fügen Sie ein `div`-Element mit der `id` "scroll-progress" in den HTML-Code ein.
2. Im CSS-Code setzen Sie die `position` des Elements auf `fixed`, den `top` auf `0`, die `width` auf `0%`, die `height` auf `4px` und die `background`-Farbe auf `#7983ff`.
3. Setzen Sie den `z-index`-Wert auf eine große Zahl, um sicherzustellen, dass die Fortschrittsleiste oben auf der Seite und über allen Inhalten platziert wird.
4. Im JavaScript-Code wählen Sie das `scroll-progress`-Element mit der Methode `document.getElementById()` aus.
5. Berechnen Sie die Höhe der Webseite mit der Formel `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6. Fügen Sie dem `window`-Objekt einen Ereignis-Listener hinzu, der auf das `scroll`-Ereignis lauscht.
7. In der Ereignis-Listener-Funktion berechnen Sie den Scrollprozentsatz des Dokuments mit der Formel `(scrollTop / height) * 100`.
8. Setzen Sie die `width` des `scroll-progress`-Elements auf den Scrollprozentsatz mit der `style`-Eigenschaft.

Hier ist der Code:

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

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
