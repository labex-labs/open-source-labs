# Verarbeiten einer Reihe von Elementen mit Iteratoren

Das Iterator-Muster ermöglicht es Ihnen, eine bestimmte Aufgabe nacheinander auf einer Sequenz von Elementen auszuführen. Ein Iterator ist für die Logik verantwortlich, über jedes Element zu iterieren und zu bestimmen, wann die Sequenz beendet ist. Wenn Sie Iteratoren verwenden, müssen Sie diese Logik nicht selbst neu implementieren.

In Rust sind Iteratoren _träge_, was bedeutet, dass sie keinen Effekt haben, bis Sie Methoden aufrufen, die den Iterator konsumieren, um ihn aufzuzehren. Beispielsweise erstellt der Code in Listing 13-10 einen Iterator über die Elemente im Vektor `v1`, indem er die auf `Vec<T>` definierte `iter`-Methode aufruft. Dieser Code macht alleine nichts nützliches.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();
```

Listing 13-10: Erstellen eines Iterators

Der Iterator wird in der Variable `v1_iter` gespeichert. Nachdem wir einen Iterator erstellt haben, können wir ihn auf verschiedene Weise verwenden. In Listing 3-5 haben wir über ein Array iteriert, indem wir eine `for`-Schleife verwendet haben, um auf jedem seiner Elemente einige Code auszuführen. Unter der Haube wurde hierbei implizit ein Iterator erstellt und anschließend konsumiert, aber wir haben bisher übersehen, wie genau das funktioniert.

Im Beispiel in Listing 13-11 trennen wir die Erstellung des Iterators von der Verwendung des Iterators in der `for`-Schleife. Wenn die `for`-Schleife mit dem Iterator in `v1_iter` aufgerufen wird, wird jedes Element im Iterator in einer Iteration der Schleife verwendet, was jeweils den Wert ausgibt.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();

for val in v1_iter {
    println!("Got: {val}");
}
```

Listing 13-11: Verwenden eines Iterators in einer `for`-Schleife

In Sprachen, in denen die Standardbibliotheken keine Iteratoren zur Verfügung stellen, würden Sie wahrscheinlich dieselbe Funktionalität implementieren, indem Sie eine Variable bei Index 0 starten, diese Variable verwenden, um in den Vektor zu indexieren und einen Wert zu erhalten, und die Variable in einer Schleife erhöhen, bis sie die Gesamtzahl der Elemente im Vektor erreicht hat.

Iterators übernehmen all diese Logik für Sie und reduzieren somit die wiederholenden Codezeilen, die Sie möglicherweise falsch programmieren könnten. Iterators geben Ihnen mehr Flexibilität, um dieselbe Logik mit vielen verschiedenen Arten von Sequenzen zu verwenden, nicht nur mit Datenstrukturen, in die Sie indexieren können, wie Vektoren. Lassen Sie uns untersuchen, wie Iterators das tun.
