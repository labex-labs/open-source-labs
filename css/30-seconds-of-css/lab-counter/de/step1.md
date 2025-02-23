# Zähler

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen benutzerdefinierten Listenzähler zu erstellen, der geschachtelte Listenelemente berücksichtigt, folgen Sie diesen Schritten:

1. Verwenden Sie `counter-reset`, um eine Variable Zähler (Standardwert `0`) zu initialisieren, wobei der Name der Wert des Attributs ist (z.B. `counter`).
2. Verwenden Sie `counter-increment` auf der Variablen Zähler für jedes zählbare Element (z.B. jedes `<li>`).
3. Verwenden Sie `counters()`, um den Wert jeder Variablen Zähler als Teil des `content` des `::before`-Pseudo-Elements für jedes zählbare Element (z.B. jedes `<li>`) anzuzeigen. Der zweite Wert, der an ihn übergeben wird (`'.'`), fungiert als Trennzeichen für geschachtelte Zähler.

Hier ist ein Beispiel für HTML-Code:

```html
<ul>
  <li>Listenelement</li>
  <li>Listenelement</li>
  <li>
    Listenelement
    <ul>
      <li>Listenelement</li>
      <li>Listenelement</li>
      <li>Listenelement</li>
    </ul>
  </li>
</ul>
```

Und hier ist der CSS-Code, um den benutzerdefinierten Listenzähler anzuwenden:

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
