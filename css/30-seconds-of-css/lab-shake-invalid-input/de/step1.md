# Schütteln bei ungültiger Eingabe

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Schüttelanimation bei ungültiger Eingabe zu erstellen, folgen Sie diesen Schritten:

1. Verwenden Sie das `pattern`-Attribut, um eine reguläre Ausdruck zu definieren, der die erlaubte Eingabe angibt. Beispielsweise verwenden Sie `[A-Za-z]*`, um nur Buchstaben zuzulassen.
2. Definieren Sie eine Schüttelanimation mithilfe von `@keyframes`. Legen Sie die `margin-left`-Eigenschaft fest, um das Eingabefeld nach links und rechts zu bewegen.
3. Verwenden Sie die `:invalid`-Pseudo-Klasse, um die Schüttelanimation auf das Eingabefeld anzuwenden.
4. Optionalerweise fügen Sie einer roten Box-Schattierung zum Eingabefeld hinzu, um den Fehler anzuzeigen.

Hier ist ein Beispielcodeausschnitt:

```html
<input type="text" placeholder="Nur Buchstaben" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
