# Implementieren des Deref-Traits

Wie in "Implementing a Trait on a Type" besprochen, müssen wir für die erforderlichen Methoden eines Traits Implementierungen bereitstellen, um es zu implementieren. Das von der Standardbibliothek bereitgestellte `Deref`-Trait erfordert, dass wir eine Methode namens `deref` implementieren, die `self` entleiht und einen Verweis auf die innere Daten zurückgibt. Listing 15-10 enthält eine Implementierung von `Deref`, die zur Definition von `MyBox<T>` hinzugefügt werden soll.

Dateiname: `src/main.rs`

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
  1 type Target = T;

    fn deref(&self) -> &Self::Target {
      2 &self.0
    }
}
```

Listing 15-10: Implementieren von `Deref` auf `MyBox<T>`

Die Syntax `type Target = T;` \[1\] definiert einen assoziierten Typ für das `Deref`-Trait, um ihn zu verwenden. Assoziierte Typen sind eine etwas andere Art, einen generischen Parameter zu deklarieren, aber Sie müssen sich hierfür vorerst nicht kümmern; wir werden sie im Kapitel 19 im Detail behandeln.

Wir füllen den Körper der `deref`-Methode mit `&self.0` aus, sodass `deref` einen Verweis auf den Wert zurückgibt, auf den wir mit dem `*`-Operator zugreifen möchten \[2\]; erinnern Sie sich aus "Using Tuple Structs Without Named Fields to Create Different Types", dass `.0` auf den ersten Wert in einer Tuple-Struktur zugreift. Die `main`-Funktion in Listing 15-9, die `*` auf den `MyBox<T>`-Wert aufruft, kompiliert jetzt, und die Assertions werden bestanden!

Ohne das `Deref`-Trait kann der Compiler nur `&`-Referenzen dereferenzieren. Die `deref`-Methode gibt dem Compiler die Möglichkeit, einen Wert beliebigen Typs, der `Deref` implementiert, zu nehmen und die `deref`-Methode aufzurufen, um einen `&`-Verweis zu erhalten, auf den er weiß, wie er ihn dereferenziert.

Als wir in Listing 15-9 `*y` eingegeben haben, hat Rust hinter den Kulissen tatsächlich diesen Code ausgeführt:

```rust
*(y.deref())
```

Rust ersetzt den `*`-Operator mit einem Aufruf der `deref`-Methode und anschließend einem einfachen Dereferenzieren, sodass wir nicht darüber nachdenken müssen, ob wir die `deref`-Methode aufrufen müssen oder nicht. Diese Rust-Funktion ermöglicht es uns, Code zu schreiben, der unabhängig davon funktioniert, ob wir eine reguläre Referenz oder einen Typ haben, der `Deref` implementiert.

Der Grund, warum die `deref`-Methode einen Verweis auf einen Wert zurückgibt und dass das einfache Dereferenzieren außerhalb der Klammern in `*(y.deref())` immer noch erforderlich ist, hat mit dem Besitzsystem zu tun. Wenn die `deref`-Methode den Wert direkt statt eines Verweises auf den Wert zurückgäbe, würde der Wert aus `self` bewegt werden. Wir möchten in diesem Fall oder in den meisten Fällen, in denen wir den Dereferenzierungsoperator verwenden, nicht die Eigentumsgewalt über den inneren Wert in `MyBox<T>` ergreifen.

Beachten Sie, dass der `*`-Operator nur einmal mit einem Aufruf der `deref`-Methode und anschließend einem Aufruf des `*`-Operators ersetzt wird, jedes Mal, wenn wir in unserem Code einen `*` verwenden. Da die Substitution des `*`-Operators nicht endlos rekursiert, erhalten wir schließlich Daten vom Typ `i32`, die mit dem `5` in `assert_eq!` in Listing 15-9 übereinstimmen.
