# Wie man den Median eines Arrays von Zahlen berechnet

Um den Median eines Arrays von Zahlen zu berechnen, folgen Sie diesen Schritten:

1. Finden Sie die Mitte des Arrays.
2. Verwenden Sie `Array.prototype.sort()`, um die Werte zu sortieren.
3. Wenn `Array.prototype.length` ungerade ist, geben Sie die Zahl an der Mitte zurück. Wenn es gerade ist, geben Sie den Durchschnitt der beiden mittleren Zahlen zurück.
4. Um zu beginnen, zu programmieren und `node` zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist ein Beispielcodeausschnitt, der diese Logik implementiert:

```js
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = [...arr].sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};
```

Sie können diese Funktion mit einem Array von Zahlen wie unten gezeigt aufrufen:

```js
median([5, 6, 50, 1, -5]); // 5
```
