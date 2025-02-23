# Sibling Fade

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um die Geschwister eines über dem Mauszeiger liegenden Elements auszublenden:

1. Animieren Sie Änderungen an der `opacity` mithilfe der `transition`-Eigenschaft.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Ändern Sie die `opacity` aller Elemente außer demjenigen, über dem die Maus sich befindet, auf `0.5` mithilfe der `:hover`- und `:not`-Pseudo-Klassen-Selektoren.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Hier ist ein Beispiel für HTML-Code:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
