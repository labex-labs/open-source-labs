# Menü bei Mausüberlagerung

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Menü-Überlagerung anzuzeigen, wenn der Benutzer über einem Bild schwebt, verwenden Sie eine `<figure>`, um das `<img>`-Element zu umschließen, und ein `<div>`-Element, das die Menü-Links enthalten wird. Wenden Sie die folgenden CSS-Eigenschaften an, um das Bild beim Hovern zu animieren und einen Schiefeffekt zu erzeugen:

- `opacity`
- `right`
  Legen Sie das `left`-Attribut des `<div>` auf das Negative der Breite des Elements fest. Setzen Sie es auf `0`, wenn Sie über das übergeordnete Element schweben, um das Menü einzuschieben. Schließlich verwenden Sie `display: flex`, `flex-direction: column` und `justify-content: center` auf dem `<div>`, um die Menüpunkte vertikal zentrieren.

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Home</a>
    <a href="#">Pricing</a>
    <a href="#">About</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
