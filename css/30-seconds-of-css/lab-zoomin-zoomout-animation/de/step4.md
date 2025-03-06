# Anwenden der Animation

Nachdem wir nun unsere Keyframes definiert haben, müssen wir die Animation auf unser Box-Element anwenden.

1. Öffnen Sie erneut die Datei `style.css` und ändern Sie den Selektor `.zoom-in-out-box` wie folgt:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. Lassen Sie uns die hinzugefügte `animation`-Eigenschaft verstehen:

   - `animation` ist eine Kurzschreibweise, mit der mehrere Animations-Eigenschaften auf einmal festgelegt werden können.
   - `zoom-in-zoom-out` ist der Name unserer Keyframes-Animation.
   - `1s` gibt an, dass ein Zyklus der Animation 1 Sekunde dauert.
   - `ease` ist die Timing-Funktion, die bewirkt, dass die Animation langsam startet, beschleunigt und dann wieder verlangsamt.
   - `infinite` bedeutet, dass die Animation unendlich wiederholt wird.

3. Speichern Sie die Datei `style.css` nach diesen Änderungen.

4. Wenn der Webserver bereits läuft, aktualisieren Sie einfach die Registerkarte **Web 8080**. Wenn nicht, klicken Sie in der unteren rechten Ecke auf "Go Live", um den Server zu starten, und öffnen Sie dann die Registerkarte **Web 8080**.

Sie sollten jetzt sehen, wie Ihr rosa Quadrat in einer kontinuierlichen Animation sanft ein- und auszoomt. Das Quadrat wird größer, bis es das 1,5-fache seiner ursprünglichen Größe erreicht, und schrumpft dann wieder auf die normale Größe zurück. Dieser Zyklus wiederholt sich unendlich.
