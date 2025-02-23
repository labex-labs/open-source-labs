# Text abbrechen

In der VM wurden bereits `index.html` und `style.css` bereitgestellt.

Um Text, der länger als eine Zeile ist, abzuschneiden und am Ende einen Auslassungspunkt hinzuzufügen, verwenden Sie die folgenden CSS-Eigenschaften:

- `overflow: hidden`, um zu verhindern, dass der Text außerhalb seiner Maße verläuft
- `white-space: nowrap`, um zu verhindern, dass der Text in der Höhe mehr als eine Zeile überschreitet
- `text-overflow: ellipsis`, um einen Auslassungspunkt hinzuzufügen, wenn der Text außerhalb seiner Maße verläuft
- Geben Sie eine feste `width` für das Element an, um zu wissen, wann ein Auslassungspunkt angezeigt werden soll

Beachten Sie, dass diese Methode nur für einzelne Zeilen-Elemente funktioniert. Beispielsweise:

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
