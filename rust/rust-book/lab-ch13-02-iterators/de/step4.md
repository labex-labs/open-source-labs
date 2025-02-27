# Methoden, die andere Iteratoren erzeugen

_Iterator-Adapter_ sind Methoden, die auf dem `Iterator`-Trait definiert sind und den Iterator nicht konsumieren. Stattdessen erzeugen sie verschiedene Iteratoren, indem sie einen Aspekt des ursprünglichen Iterators ändern.

Listing 13-14 zeigt ein Beispiel für den Aufruf der Iterator-Adapter-Methode `map`, die eine Closure annimmt, die auf jedes Element während der Iteration aufgerufen wird. Die `map`-Methode gibt einen neuen Iterator zurück, der die modifizierten Elemente produziert. Die Closure erstellt hier einen neuen Iterator, in dem jedes Element aus dem Vektor um 1 erhöht wird.

Dateiname: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

Listing 13-14: Aufrufen des Iterator-Adapters `map`, um einen neuen Iterator zu erstellen

Dieser Code erzeugt jedoch eine Warnung:

    warning: unused `Map` that must be used
     --> src/main.rs:4:5
      |
    4 |     v1.iter().map(|x| x + 1);
      |     ^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = note: `#[warn(unused_must_use)]` on by default
      = note: iterators are lazy and do nothing unless consumed

Der Code in Listing 13-14 tut nichts; die von uns angegebene Closure wird nie aufgerufen. Die Warnung erinnert uns daran, warum: Iterator-Adapter sind träge, und wir müssen hier den Iterator konsumieren.

Um diese Warnung zu beheben und den Iterator zu konsumieren, verwenden wir die `collect`-Methode, die wir in Listing 12-1 mit `env::args` verwendet haben. Diese Methode konsumiert den Iterator und sammelt die resultierenden Werte in einem Sammlungstyp.

In Listing 13-15 sammeln wir in einen Vektor die Ergebnisse der Iteration über den Iterator, der aus dem Aufruf von `map` zurückgegeben wird. Dieser Vektor wird schließlich jedes Element aus dem ursprünglichen Vektor enthalten, um 1 erhöht.

Dateiname: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

Listing 13-15: Aufrufen der `map`-Methode, um einen neuen Iterator zu erstellen, und anschließend Aufrufen der `collect`-Methode, um den neuen Iterator zu konsumieren und einen Vektor zu erstellen

Da `map` eine Closure annimmt, können wir jede beliebige Operation angeben, die wir auf jedes Element ausführen möchten. Dies ist ein großartiges Beispiel dafür, wie Closures es Ihnen ermöglichen, ein Verhalten zu personalisieren, während Sie das Iterationsverhalten, das der `Iterator`-Trait bietet, wiederverwenden.

Sie können mehrere Aufrufe von Iterator-Adaptern verkettieren, um komplexe Aktionen auf leserliche Weise auszuführen. Aber da alle Iteratoren träge sind, müssen Sie eine der konsumierenden Adapter-Methoden aufrufen, um Ergebnisse aus Aufrufen von Iterator-Adaptern zu erhalten.
