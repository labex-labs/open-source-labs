# Flexbox-Zentrierung

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein untergeordnetes Element sowohl horizontal als auch vertikal innerhalb eines übergeordneten Elements mithilfe von Flexbox zu zentrieren, folgen Sie diesen Schritten:

1. Erstellen Sie eine Flexbox-Layout, indem Sie die `display`-Eigenschaft des übergeordneten Elements auf `flex` setzen.
2. Verwenden Sie die `justify-content`-Eigenschaft, um das untergeordnete Element horizontal zu zentrieren, indem Sie ihren Wert auf `center` setzen.
3. Verwenden Sie die `align-items`-Eigenschaft, um das untergeordnete Element vertikal zu zentrieren, indem Sie ihren Wert auf `center` setzen.
4. Fügen Sie das untergeordnete Element innerhalb des übergeordneten Elements hinzu.

Hier ist ein Beispielcodeausschnitt:

```html
<div class="flexbox-centering">
  <div>Zentrierter Inhalt.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
