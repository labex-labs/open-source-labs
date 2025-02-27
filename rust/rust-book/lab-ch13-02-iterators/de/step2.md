# Der Iterator-Trait und die next-Methode

Alle Iteratoren implementieren einen Trait namens `Iterator`, der in der Standardbibliothek definiert ist. Die Definition des Traits sieht so aus:

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // Methoden mit Standardimplementierungen weggelassen
}
```

Beachten Sie, dass diese Definition einige neue Syntax verwendet: `type Item` und `Self::Item`, die einen _assozierten Typ_ mit diesem Trait definieren. Wir werden uns in Kapitel 19 im Detail mit assoziierten Typen befassen. Für jetzt brauchen Sie nur zu wissen, dass dieser Code besagt, dass das Implementieren des `Iterator`-Traits auch die Definition eines `Item`-Typs erfordert und dieser `Item`-Typ im Rückgabetyp der `next`-Methode verwendet wird. Mit anderen Worten, der `Item`-Typ wird der Typ sein, der vom Iterator zurückgegeben wird.

Der `Iterator`-Trait erfordert von den Implementierenden nur die Definition einer Methode: die `next`-Methode, die jeweils ein Element des Iterators zurückgibt, in `Some` verpackt, und wenn die Iteration beendet ist, `None` zurückgibt.

Wir können die `next`-Methode direkt auf Iteratoren aufrufen; Listing 13-12 zeigt, welche Werte von wiederholten Aufrufen von `next` auf dem von dem Vektor erstellten Iterator zurückgegeben werden.

Dateiname: `src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Listing 13-12: Aufrufen der `next`-Methode auf einem Iterator

Beachten Sie, dass wir `v1_iter` mutabel machen mussten: Der Aufruf der `next`-Methode auf einem Iterator ändert den internen Zustand, den der Iterator verwendet, um zu verfolgen, wo er sich in der Sequenz befindet. Mit anderen Worten, dieser Code _konsumiert_ oder verbraucht den Iterator. Jeder Aufruf von `next` verbraucht ein Element aus dem Iterator. Wir mussten `v1_iter` nicht mutabel machen, als wir eine `for`-Schleife verwendeten, weil die Schleife die Eigentumsgewalt über `v1_iter` übernahm und es hinter den Kulissen mutabel machte.

Beachten Sie auch, dass die Werte, die wir aus den Aufrufen von `next` erhalten, unveränderliche Referenzen auf die Werte im Vektor sind. Die `iter`-Methode erzeugt einen Iterator über unveränderliche Referenzen. Wenn wir einen Iterator erstellen möchten, der die Eigentumsgewalt über `v1` übernimmt und die Werte als Besitz zurückgibt, können wir `into_iter` statt `iter` aufrufen. Ähnlich können wir `iter_mut` statt `iter` aufrufen, wenn wir über veränderliche Referenzen iterieren möchten.
