# Benutzerdefinierter Radiobutton

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen stilisierten Radiobutton mit Animation bei einem Statuswechsel zu erstellen, folgen Sie diesen Schritten:

1. Erstellen Sie einen `.radio-container` mit Flexbox, um das passende Layout für die Radiobuttons zu erstellen.
2. Setzen Sie die Stile des `<input>` zurück und verwenden Sie es, um den Umriss und den Hintergrund des Radiobuttons zu erstellen.
3. Verwenden Sie das `::before`-Element, um den inneren Kreis des Radiobuttons zu erstellen.
4. Erzeugen Sie einen Animationseffekt bei einem Statuswechsel, indem Sie `transform: scale(1)` und eine CSS-Übergangsanimation verwenden.

Hier ist ein Beispiel-HTML-Ausschnitt:

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Äpfel</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Orangen</label>
</div>
```

Und hier ist die zugehörige CSS:

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
