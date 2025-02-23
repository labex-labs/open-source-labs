# Zeige zusätzlichen Inhalt beim Hovern

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Karte zu erstellen, die beim Hovern zusätzlichen Inhalt anzeigt, folge diesen Schritten:

1. Verwende `overflow: hidden` auf der Karte, um alle Elemente zu verstecken, die vertikal überlaufen.
2. Verwende die Pseudoklassen-Selektoren `:hover` und `:focus-within`, um die Styling der Karte zu ändern, wenn das Element gehovert, fokusiert oder eines seiner Nachkommen fokusiert wird.
3. Setze `transition: 0.3s ease all`, um einen reibungslosen Übergangseffekt beim Hovern/Fokussieren zu erstellen.

Hier ist ein Beispiel für den HTML-Code der Karte:

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link zur Quelle</a>
    </p>
  </div>
</div>
```

Und hier ist der CSS-Code, um die Karte zu stylen:

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Bitte klicke in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend kannst du die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschau.
