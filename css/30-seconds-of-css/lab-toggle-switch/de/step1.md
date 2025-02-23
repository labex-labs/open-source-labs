# Umschalter

In der VM wurden bereits `index.html` und `style.css` zur Verfügung gestellt.

Hier ist eine kürzere und klarere Version des Inhalts:

Um einen Umschalter ausschließlich mit CSS zu erstellen, folgen Sie diesen Schritten:

1. Verbinden Sie das `<label>` mit dem Checkbox-`<input>`-Element mithilfe des `for`-Attributs.
2. Verwenden Sie das `::after`-Pseudo-Element des `<label>`, um eine kreisförmige Klinke für den Umschalter zu erstellen.
3. Verwenden Sie den `:checked`-Pseudo-Klassen-Selektor, um die Position der Klinke zu ändern, indem Sie `transform: translateX(20px)` und die `background-color` des Umschalters verwenden.
4. Verbergen Sie das `<input>`-Element visuell, indem Sie `position: absolute` und `left: -9999px` verwenden.

Hier ist der HTML-Code:

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

Hier ist der CSS-Code:

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
