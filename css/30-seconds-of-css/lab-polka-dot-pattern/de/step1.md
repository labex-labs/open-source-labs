# Punktmuster-Hintergrund

`index.html` und `style.css` wurden bereits in der virtuellen Maschine (VM) bereitgestellt.

Um ein Punktmuster-Hintergrund zu erstellen, können Sie die folgenden Schritte ausführen:

1. Setzen Sie die Eigenschaft `background-color` auf schwarz.
2. Verwenden Sie die Eigenschaft `background-image` mit zwei `radial-gradient()`-Werten, um zwei Punkte zu erstellen.
3. Geben Sie die Größe des Musters mit der Eigenschaft `background-size` an. Verwenden Sie `background-position`, um die beiden Gradienten richtig zu platzieren.
4. Setzen Sie `background-repeat` auf `repeat`.
5. Beachten Sie, dass die festgelegten `height`- und `width`-Werte des Elements nur zu Demonstrationszwecken dienen.

Hier ist ein Beispiel für HTML-Code für ein div-Element mit der Klasse `polka-dot`:

```html
<div class="polka-dot"></div>
```

Und hier ist der entsprechende CSS-Code:

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image: radial-gradient(#fff 10%, transparent 11%), radial-gradient(#fff
        10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Web-Service auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzusehen.
