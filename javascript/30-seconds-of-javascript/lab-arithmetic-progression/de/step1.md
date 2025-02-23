# Beispielcode für arithmetische Progression

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Hier ist ein Beispielcode, der ein Array von Zahlen in arithmetischer Progression erstellt. Das Array beginnt mit einer gegebenen positiven ganzen Zahl und geht bis zu einer bestimmten Grenze:

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

Um diesen Code zu verwenden, rufen Sie einfach die Funktion `arithmeticProgression` mit zwei Argumenten auf: die startende positive ganze Zahl und die Grenze. Beispielsweise:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
