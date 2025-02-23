# Navigationsliste-Element: Hover- und Focus-Effekt

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen benutzerdefinierten Hover- und Focus-Effekt für Navigationspunkte zu erstellen, verwenden Sie CSS-Transformationen wie folgt:

1. Verwenden Sie das `::before`-Pseudo-Element am Listenelement-Anker, um einen Hover-Effekt zu erzeugen. Verbergen Sie es mit `transform: scale(0)`.
2. Verwenden Sie die `:hover`- und `:focus`-Pseudo-Klassen-Selektoren, um das Pseudo-Element zu `transform: scale(1)` zu überführen und seinen farbigen Hintergrund anzuzeigen.
3. Verhindern Sie, dass das Pseudo-Element den Ankerelement überdeckt, indem Sie `z-index` verwenden.

Sie können den folgenden HTML-Code für Ihr Navigationsmenü verwenden:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

Und wenden Sie die folgenden CSS-Regeln an:

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
