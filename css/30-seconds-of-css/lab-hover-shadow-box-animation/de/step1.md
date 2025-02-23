# Hover Shadow Box Animation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Schattenbox um den Text zu erstellen, wenn dieser angehoben wird, folgen Sie diesen Schritten:

1. Setzen Sie `transform: perspective(1px)`, um dem Element einen 3D-Raum zu geben, indem Sie den Abstand zwischen der Z-Ebene und dem Benutzer beeinflussen, und `translateZ(0)`, um das `p`-Element entlang der z-Achse im 3D-Raum neu zu positionieren.
2. Verwenden Sie `box-shadow`, um die Box transparent zu machen.
3. Aktivieren Sie die Transitions für sowohl `box-shadow` als auch `transform` mithilfe der `transition-property`-Eigenschaft.
4. Wenden Sie eine neue `box-shadow` und `transform: scale(1.2)` an, um die Skala des Texts zu ändern, indem Sie die `:hover`, `:active` und `:focus`-Pseudo-Klassen-Selektoren verwenden.
5. Fügen Sie die Klasse `hover-shadow-box-animation` zum `p`-Element hinzu.

Hier ist der HTML-Code:

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

Und hier ist der CSS-Code:

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
