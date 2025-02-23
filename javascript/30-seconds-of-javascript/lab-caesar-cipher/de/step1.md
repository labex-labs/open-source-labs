# Caesar-Chiffre

Um das Caesar-Chiffre zu verwenden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Rufen Sie die `caesarCipher`-Funktion mit dem zu verschlüsselnden oder zu entschlüsselnden String, dem Verschiebewert und einem Boolean, der angibt, ob entschlüsselt werden soll oder nicht.
3. Die `caesarCipher`-Funktion verwendet den Modulo-Operator (`%`) und den ternären Operator (`?`), um den richtigen Verschlüsselungs- oder Entschlüsselungsschlüssel zu berechnen.
4. Sie verwendet den Spread-Operator (`...`) und `Array.prototype.map()`, um über die Buchstaben des gegebenen Strings zu iterieren.
5. Sie verwendet `String.prototype.charCodeAt()` und `String.fromCharCode()`, um jeden Buchstaben entsprechend umzuwandeln, wobei Sonderzeichen, Leerzeichen usw. ignoriert werden.
6. Sie verwendet `Array.prototype.join()`, um alle Buchstaben zu einem String zu kombinieren.
7. Wenn Sie einen verschlüsselten String entschlüsseln möchten, übergeben Sie `true` als letztes Argument, `decrypt`, wenn Sie die `caesarCipher`-Funktion aufrufen.

Hier ist der Code für die `caesarCipher`-Funktion:

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

Hier sind einige Beispiele für die Verwendung der `caesarCipher`-Funktion:

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
