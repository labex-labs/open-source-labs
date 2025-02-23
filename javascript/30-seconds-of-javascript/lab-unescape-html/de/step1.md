# Entschlüsseln von HTML

Diese Funktion entschlüsselt escapte HTML-Zeichen. Um sie zu verwenden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein.
3. Kopieren und einfügen Sie den folgenden Code:

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. Rufen Sie die `unescapeHTML`-Funktion auf und übergeben Sie ihr einen String mit escapten Zeichen.
5. Die Funktion wird den entschlüsselten String zurückgeben.

Beispielverwendung:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
