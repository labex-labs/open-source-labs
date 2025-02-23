# Hover-Unterstrich-Animation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen animierten Unterstrich-Effekt zu erstellen, wenn der Benutzer über den Text fährt, folgen Sie diesen Schritten:

1. Verwenden Sie `display: inline-block`, um sicherzustellen, dass der Unterstrich genau die Breite des Textinhalts umfasst.
2. Verwenden Sie das `::after`-Pseudo-Element mit `width: 100%` und `position: absolute`, um es unterhalb des Inhalts zu platzieren.
3. Verwenden Sie `transform: scaleX(0)`, um das Pseudo-Element zunächst zu verstecken.
4. Verwenden Sie den `:hover`-Pseudo-Klassen-Selektor, um `transform: scaleX(1)` anzuwenden und das Pseudo-Element beim Hovern anzuzeigen.
5. Animieren Sie `transform` mit `transform-origin: left` und einem geeigneten `transition`.
6. Entfernen Sie die `transform-origin`-Eigenschaft, um die Transformation von der Mitte des Elements aus zu starten.

Hier ist ein Beispiel-HTML-Code, um den Effekt auf ein Textelement anzuwenden:

```html
<p class="hover-underline-animation">Hover this text to see the effect!</p>
```

Und hier ist der entsprechende CSS-Code:

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
