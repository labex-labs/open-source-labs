# Zentrierung mit display: table

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Kindelement sowohl vertikal als auch horizontal innerhalb seines Eltern-elements zu zentrieren, folgen Sie diesen Schritten:

1. Fügen Sie ein Container-Element mit einer festen `height` und `width` hinzu.

```html
<div class="container"></div>
```

2. Fügen Sie das Kindelement innerhalb des Container-Elements hinzu und geben Sie es die Klasse `.center`.

```html
  <div class="center"><span>Zentrierter Inhalt</span></div>
</div>
```

3. Wenden Sie in der CSS die folgenden Stile auf das Container-Element an:

- Setzen Sie `height` und `width` auf die gewünschten festen Werte.
- Fügen Sie eine Grenze hinzu (optional).

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. Wenden Sie in der CSS die folgenden Stile auf das Kindelement an:

- Verwenden Sie `display: table`, um das `.center`-Element wie ein `<table>`-Element zu verhalten.
- Setzen Sie `height` und `width` auf `100%`, um das Element den verfügbaren Platz innerhalb seines Eltern-elements zu füllen.
- Verwenden Sie `display: table-cell` auf dem Kindelement, um es wie ein `<td>`-Element zu verhalten.
- Verwenden Sie `text-align: center` und `vertical-align: middle` auf dem Kindelement, um es horizontal und vertikal zu zentrieren.

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
