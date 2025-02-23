# Wechselndes Text

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Animation mit wechselndem Text zu erstellen, folgen Sie diesen Schritten:

1. Erstellen Sie ein `<span>`-Element mit der Klasse "alternating" und der `id` "alternating-text", um den Text zu speichern, der gewechselt werden soll:

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. Definieren Sie in der CSS eine Animation namens `alternating-text`, die das `<span>`-Element durch Festlegen von `display: none` verschwinden lässt:

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

3. Definieren Sie in JavaScript ein Array mit den verschiedenen Wörtern, die gewechselt werden sollen, und verwenden Sie das erste Wort, um den Inhalt des `<span>`-Elements zu initialisieren:

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. Verwenden Sie `EventTarget.addEventListener()`, um einen Event-Listener für das `'animationiteration'`-Event zu definieren. Dies wird den Event-Handler jedes Mal ausführen, wenn eine Iteration der Animation abgeschlossen ist. Im Event-Handler verwenden Sie `Element.innerHTML`, um das nächste Element im `texts`-Array als Inhalt des `<span>`-Elements anzuzeigen:

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
