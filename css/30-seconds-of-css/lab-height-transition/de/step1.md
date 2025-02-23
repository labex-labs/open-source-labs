# Höhenübergang

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Dieser Codeausschnitt überträgt die Höhe eines Elements von `0` auf `auto`, wenn die Höhe unbekannt ist, indem er die folgenden Schritte ausführt:

- Verwenden Sie die `transition`-Eigenschaft, um anzugeben, dass Änderungen an `max-height` über eine Dauer von `0,3 s` übergeben werden sollen.
- Verwenden Sie die `overflow`-Eigenschaft, die auf `hidden` festgelegt ist, um zu verhindern, dass der Inhalt des versteckten Elements das Container überläuft.
- Verwenden Sie die `max-height`-Eigenschaft, um eine Anfangshöhe von `0` anzugeben.
- Verwenden Sie die `:hover`-Pseudoklasse, um die `max-height` auf den Wert der von JavaScript festgelegten `--max-height`-Variablen zu ändern.
- Verwenden Sie die `Element.scrollHeight`-Eigenschaft und die `CSSStyleDeclaration.setProperty()`-Methode, um den Wert von `--max-height` auf die aktuelle Höhe des Elements zu setzen.
- **Hinweis:** Dieser Ansatz verursacht bei jedem Animationsrahmen einen Neulayoutvorgang, was bei einer großen Anzahl von Elementen unterhalb des übergehenden Elements zu Verzögerungen führen kann.

```html
<div class="trigger">
  Hover over me to see a height transition.
  <div class="el">Additional content</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
