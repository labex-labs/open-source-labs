# Methoden, die den Iterator konsumieren

Der `Iterator`-Trait hat eine Reihe von verschiedenen Methoden mit Standardimplementierungen, die von der Standardbibliothek bereitgestellt werden; Sie können sich über diese Methoden in der API-Dokumentation der Standardbibliothek für den `Iterator`-Trait informieren. Einige dieser Methoden rufen in ihrer Definition die `next`-Methode auf, weshalb Sie die `next`-Methode implementieren müssen, wenn Sie den `Iterator`-Trait implementieren.

Methoden, die `next` aufrufen, werden als _konsumierende Adapter_ bezeichnet, weil ihr Aufruf den Iterator aufbraucht. Ein Beispiel ist die `sum`-Methode, die die Eigentumsgewalt über den Iterator übernimmt und durch wiederholtes Aufrufen von `next` durch die Elemente iteriert, wodurch der Iterator verbraucht wird. Während der Iteration addiert sie jedes Element zu einem laufenden Gesamtwert und gibt den Gesamtwert zurück, wenn die Iteration abgeschlossen ist. Listing 13-13 hat einen Test, der den Einsatz der `sum`-Methode veranschaulicht.

Dateiname: `src/lib.rs`

```rust
#[test]
fn iterator_sum() {
    let v1 = vec![1, 2, 3];

    let v1_iter = v1.iter();

    let total: i32 = v1_iter.sum();

    assert_eq!(total, 6);
}
```

Listing 13-13: Aufrufen der `sum`-Methode, um die Summe aller Elemente im Iterator zu erhalten

Wir dürfen `v1_iter` nicht mehr verwenden, nachdem der Aufruf von `sum` erfolgt ist, weil `sum` die Eigentumsgewalt über den Iterator übernimmt, auf dem wir sie aufrufen.
