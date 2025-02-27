# for-Schleifen

In einer `for`-Schleife ist der Wert, der direkt nach dem Schlüsselwort `for` steht, ein Muster. Beispielsweise ist in `for x in y` das `x` das Muster. Listing 18-3 zeigt, wie man in einer `for`-Schleife ein Muster verwendet, um ein Tupel zu _zerlegen_ oder auseinanderzubrechen, als Teil der `for`-Schleife.

Dateiname: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

Listing 18-3: Verwenden eines Musters in einer `for`-Schleife, um ein Tupel zu zerlegen

Der Code in Listing 18-3 wird Folgendes ausgeben:

    a is at index 0
    b is at index 1
    c is at index 2

Wir verwenden die `enumerate`-Methode, um einen Iterator anzupassen, sodass er einen Wert und den Index für diesen Wert produziert, die in ein Tupel eingefügt werden. Der erste produzierte Wert ist das Tupel `(0, 'a')`. Wenn dieser Wert mit dem Muster `(index, value)` übereinstimmt, wird `index` `0` und `value` `'a'` sein, was die erste Zeile der Ausgabe druckt.
