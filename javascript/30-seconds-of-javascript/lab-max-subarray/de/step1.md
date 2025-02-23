# Maximum Subarray Algorithm

Um das Programmieren zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Dieser Algorithmus findet ein zusammenhängendes Teilarray mit der größten Summe innerhalb eines Arrays von Zahlen. Um diesen Algorithmus zu implementieren, folgen Sie diesen Schritten:

- Verwenden Sie einen greedy Ansatz, um die aktuelle `Summe` und das aktuelle Maximum, `maxSum`, zu verfolgen. Setzen Sie `maxSum` auf `-Infinity`, um sicherzustellen, dass der höchste negative Wert zurückgegeben wird, wenn alle Werte negativ sind.
- Definieren Sie Variablen, um den maximalen Startindex, `sMax`, den maximalen Endindex, `eMax`, und den aktuellen Startindex, `s`, zu verfolgen.
- Verwenden Sie `Array.prototype.forEach()`, um über die Werte zu iterieren und den aktuellen Wert zur `Summe` hinzuzufügen.
- Wenn die aktuelle `Summe` größer als `maxSum` ist, aktualisieren Sie die Indexwerte und die `maxSum`.
- Wenn die `Summe` unter `0` liegt, setzen Sie sie auf `0` und aktualisieren Sie den Wert von `s` auf den nächsten Index.
- Verwenden Sie `Array.prototype.slice()`, um das Teilarray zurückzugeben, das durch die Indexvariablen angegeben wird.

Hier ist der JavaScript-Code für den Algorithmus:

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

Hier ist ein Beispiel, wie die Funktion verwendet werden kann:

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
