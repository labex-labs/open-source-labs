# Definieren unseres eigenen Smart Pointers

Lassen Sie uns einen Smart Pointer ähnlich dem von der Standardbibliothek bereitgestellten `Box<T>`-Typ erstellen, um zu erfahren, wie Smart Pointer standardmäßig anders als Referenzen verhalten. Dann werden wir uns ansehen, wie man die Möglichkeit erhält, den Dereferenzierungsoperator zu verwenden.

Der `Box<T>`-Typ wird letztendlich als Tuple-Struktur mit einem Element definiert, daher definiert Listing 15-8 einen `MyBox<T>`-Typ auf die gleiche Weise. Wir definieren auch eine `new`-Funktion, um der auf `Box<T>` definierten `new`-Funktion zu entsprechen.

Dateiname: `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Listing 15-8: Definieren eines `MyBox<T>`-Typs

Wir definieren eine Struktur namens `MyBox` und deklarieren einen generischen Parameter `T` \[1\], weil wir wollen, dass unser Typ Werte beliebiger Typen aufnimmt. Der `MyBox`-Typ ist eine Tuple-Struktur mit einem Element vom Typ `T`. Die `MyBox::new`-Funktion nimmt einen Parameter vom Typ `T` \[2\] und gibt eine `MyBox`-Instanz zurück, die den übergebenen Wert enthält \[3\].

Lassen Sie uns versuchen, die `main`-Funktion in Listing 15-7 zu Listing 15-8 hinzuzufügen und sie zu ändern, um den von uns definierten `MyBox<T>`-Typ anstelle von `Box<T>` zu verwenden. Der Code in Listing 15-9 wird nicht kompilieren, weil Rust nicht weiß, wie man `MyBox` dereferenziert.

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Listing 15-9: Versuch, `MyBox<T>` auf die gleiche Weise zu verwenden wie Referenzen und `Box<T>`

Hier ist der resultierende Kompilierungsfehler:

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

Unser `MyBox<T>`-Typ kann nicht dereferenziert werden, weil wir diese Fähigkeit für unseren Typ nicht implementiert haben. Um die Dereferenzierung mit dem `*`-Operator zu ermöglichen, implementieren wir das `Deref`-Trait.
