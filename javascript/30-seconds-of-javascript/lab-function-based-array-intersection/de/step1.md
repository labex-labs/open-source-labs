# Wie man die Array-Schnittmenge mithilfe einer Funktion in JavaScript findet

Um die Elemente zu finden, die in beiden Arrays basierend auf einer bereitgestellten Vergleichsfunktion existieren, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.

2. Verwenden Sie `Array.prototype.filter()` und `Array.prototype.findIndex()` in Kombination mit der bereitgestellten Vergleichsfunktion, um die Schnittwerte zu bestimmen.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. Rufen Sie die `intersectionWith()`-Funktion mit den beiden Arrays und der Vergleichsfunktion als Argumenten auf.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

Dies wird ein Array zurückgeben, das die Schnittwerte zwischen den beiden Arrays enthält, basierend auf der bereitgestellten Vergleichsfunktion.
