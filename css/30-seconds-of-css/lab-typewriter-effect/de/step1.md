# Schreibmaschineeffekt

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Animation mit Schreibmaschineeffekt zu erstellen, folgen Sie diesen Schritten:

1. Definieren Sie zwei Animationen, `typing` und `blink`. `typing` animiert die Zeichen, und `blink` animiert den Cursor.
2. Verwenden Sie das `::after`-Pseudo-Element, um den Cursor zum Container-Element hinzuzufügen.
3. Verwenden Sie JavaScript, um den Text für das innere Element festzulegen und die Variable `--characters` zu setzen, die die Anzahl der Zeichen enthält. Diese Variable wird verwendet, um den Text zu animieren.
4. Verwenden Sie `white-space: nowrap` und `overflow: hidden`, um den Inhalt sofern notwendig unsichtbar zu machen.

Hier ist der HTML-Code:

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

Und hier ist der CSS-Code:

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

Und schließlich hier ist der JavaScript-Code:

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
