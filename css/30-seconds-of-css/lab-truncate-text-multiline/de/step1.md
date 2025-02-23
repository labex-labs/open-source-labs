# Mehrzeilige Texte kürzen

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um Text zu kürzen, der länger als eine Zeile ist, folgen Sie diesen Schritten:

1. Verwenden Sie `overflow: hidden`, um zu verhindern, dass der Text seine Abmessungen überschreitet.
2. Legen Sie eine feste `width` von `400px` fest, um sicherzustellen, dass das Element mindestens eine konstante Dimension hat.
3. Legen Sie `height: 109.2px` fest, wie berechnet aus der `font-size`, mit der Formel `font-size * line-height * numberOfLines` (in diesem Fall `26 * 1.4 * 3 = 109.2`).
4. Fügen Sie die Klasse `truncate-text-multiline` zum `p`-Element in Ihrer HTML hinzu.
5. Legen Sie `font-size: 26px` und `line-height: 1.4` in der CSS für die `.truncate-text-multiline`-Klasse fest.
6. Legen Sie `color: #333` und `background: #f5f6f9` fest, um den Text zu gestalten.
7. Um einen Farbverlauf von `transparent` zu der `background-color` zu erstellen, fügen Sie die folgenden CSS-Regeln zum `.truncate-text-multiline::after`-Pseudo-Element hinzu:

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

Dies wird einen Farbverlauf-Container mit einer Höhe von `36.4px` erstellen, berechnet für den Farbverlauf-Container, basierend auf der Formel `font-size * line-height` (in diesem Fall `26 * 1.4 = 36.4`). Das `::after`-Pseudo-Element ist in der unteren rechten Ecke des `.truncate-text-multiline`-Elements positioniert.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zuvorschauen.
