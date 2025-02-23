# Hübscher Textunterstrich

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um zu vermeiden, dass die Absätze den Unterstrich abschneiden, verwenden Sie `text-shadow` mit vier Werten, um einen dicken Schatten zu erstellen, der die Linie bedeckt, an der die Absätze den Unterstrich treffen. Stellen Sie sicher, dass die `text-shadow`-Farbe der `background`-Farbe entspricht, und passen Sie die `px`-Werte für größere Schriftarten an. Erstellen Sie den tatsächlichen Unterstrich mit `background-image` mit einem `linear-gradient()` und `currentColor`. Legen Sie `background-position`, `background-repeat` und `background-size` fest, um den Farbverlauf an der richtigen Position zu platzieren. Verwenden Sie den `::selection`-Pseudo-Klassen-Selektor, um sicherzustellen, dass der Textschatten nicht mit der Texterfassung interferiert. Beachten Sie, dass dieser Effekt nativ als `text-decoration-skip-ink: auto` implementiert ist, aber es gibt weniger Kontrolle über den Unterstrich.

Hier ist ein Beispiel-Codeausschnitt:

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
