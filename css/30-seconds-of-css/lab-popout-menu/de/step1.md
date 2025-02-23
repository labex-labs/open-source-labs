# Popup-Menü

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein interaktives Popup-Menü beim Hovern/Fokussieren anzuzeigen, folgen Sie diesen Schritten:

1. Verwenden Sie in der CSS `left: 100%`, um das Popup-Menü rechts vom Eltern-Element zu positionieren.
2. Verwenden Sie `visibility: hidden` anstelle von `display: none`, um das Popup-Menü zunächst zu verstecken und damit Übergänge anzuwenden.
3. Wenden Sie die Pseudo-Klassen-Selektoren `:hover`, `:focus` und `:focus-within` auf das Eltern-Element an, um das Popup-Menü anzuzeigen, wenn es gehovert/fokussiert wird.
4. Verwenden Sie den folgenden HTML- und CSS-Code:

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Popout menu</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
