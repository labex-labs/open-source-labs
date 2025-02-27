# Erstellen eines neuen Vektors

Um einen neuen leeren Vektor zu erstellen, rufen wir die Funktion `Vec::new` auf, wie in Listing 8-1 gezeigt.

```rust
let v: Vec<i32> = Vec::new();
```

Listing 8-1: Erstellen eines neuen, leeren Vektors, um Werte vom Typ `i32` zu speichern

Beachten Sie, dass wir hier eine Typangabe hinzugefügt haben. Da wir keinen Wert in diesen Vektor einfügen, weiß Rust nicht, welchen Elementtyp wir speichern möchten. Dies ist ein wichtiger Punkt. Vektoren werden mit Generics implementiert; wir werden im Kapitel 10 behandeln, wie Sie Generics mit Ihren eigenen Typen verwenden. Im Moment wissen Sie nur, dass der vom Standardbibliothek bereitgestellte Typ `Vec<T>` beliebige Typen speichern kann. Wenn wir einen Vektor erstellen, um einen bestimmten Typ zu speichern, können wir den Typ innerhalb von spitzen Klammern angeben. In Listing 8-1 haben wir Rust mitgeteilt, dass der `Vec<T>` in `v` `i32`-Typ-Elemente speichern wird.

Oftmals werden Sie einen `Vec<T>` mit Anfangswerten erstellen, und Rust wird den Typ des zu speichernden Werts ableiten, sodass Sie diese Typangabe selten benötigen. Rust bietet bequem die `vec!`-Makro an, das einen neuen Vektor erstellt, der die Ihnen gegebenen Werte speichert. Listing 8-2 erstellt einen neuen `Vec<i32>`, der die Werte `1`, `2` und `3` enthält. Der ganzzahlige Typ ist `i32`, weil das der Standardganzzahlttyp ist, wie wir in "Datentypen" diskutiert haben.

```rust
let v = vec![1, 2, 3];
```

Listing 8-2: Erstellen eines neuen Vektors, der Werte enthält

Da wir Anfangs-`i32`-Werte angegeben haben, kann Rust ableiten, dass der Typ von `v` `Vec<i32>` ist, und die Typangabe ist nicht erforderlich. Als Nächstes werden wir uns ansehen, wie man einen Vektor modifiziert.
