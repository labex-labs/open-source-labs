# Eingabe mit Präfix

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Eingabe mit einem visuellen, nicht bearbeitbaren Präfix zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie `display: flex`, um ein Container-Element mit der Klasse `.input-box` zu erstellen.
2. Entfernen Sie die Grenze und den Umriss aus dem `<input>`-Feld und wenden Sie sie stattdessen auf das übergeordnete Element an, um es wie eine Eingabemaske aussehen zu lassen.
3. Verwenden Sie den pseudo-klassenselektoren `:focus-within`, um das übergeordnete Element entsprechend zu gestalten, wenn der Benutzer mit dem `<input>`-Feld interagiert.

Hier ist der HTML-Code:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

Und hier ist der CSS-Code:

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
