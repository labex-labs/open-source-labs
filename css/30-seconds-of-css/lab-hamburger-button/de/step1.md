# Hamburger-Button

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Hamburger-Menü zu erstellen, das beim Hovern in einen Kreuz-Button übergeht, folgen Sie diesen Schritten:

1. Verwenden Sie ein `div`-Container `.hamburger-menu`, der die obere, untere und mittlere Leiste enthält.
2. Legen Sie den Container auf `display: flex` mit `flex-flow: column wrap` fest.
3. Fügen Sie Abstand zwischen den Leisten hinzu, indem Sie `justify-content: space-between` verwenden.
4. Verwenden Sie `transform: rotate()`, um die obere und untere Leiste um 45 Grad zu drehen, und `opacity: 0`, um die mittlere Leiste beim Hovern auszufärben.
5. Verwenden Sie `transform-origin: left`, damit sich die Leisten um den linken Punkt drehen.

Hier ist der entsprechende HTML-Code:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

Und hier ist der CSS-Code:

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
