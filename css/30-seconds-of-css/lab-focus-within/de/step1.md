# Focus Within

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um das Aussehen eines Formulars zu ändern, wenn eines seiner untergeordneten Elemente fokusiert ist, verwenden Sie die Pseudoklasse `:focus-within`, um Stile auf das übergeordnete Element anzuwenden. Beispielsweise hat im gegebenen HTML-Code das `form`-Element bei fokussiertem Eingabefeld einen grünen Hintergrund. Um Stile auf die untergeordneten Elemente anzuwenden, verwenden Sie passende CSS-Selektoren wie `label` und `input`.

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
