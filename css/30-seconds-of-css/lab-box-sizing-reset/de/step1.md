# Box-Sizing-Reset

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um sicherzustellen, dass die `width` und `height` eines Elements nicht durch `border` oder `padding` beeinflusst werden, verwenden Sie die CSS-Eigenschaft `box-sizing: border-box`. Dies umfasst die `padding` und den `border` bei der Berechnung der `width` und `height` des Elements. Wenn Sie die `box-sizing`-Eigenschaft von einem übergeordneten Element vererben möchten, verwenden Sie `box-sizing: inherit`.

Hier ist ein Beispiel für die Verwendung der `box-sizing`-Eigenschaft mit zwei `div`-Elementen:

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

In diesem Beispiel hat das erste `div`-Element `box-sizing: border-box`, und das zweite `div`-Element hat `box-sizing: content-box`.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
