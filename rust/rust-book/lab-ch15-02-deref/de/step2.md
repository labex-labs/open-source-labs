# Dem Zeiger auf den Wert folgen

Eine reguläre Referenz ist eine Art Zeiger, und eine Möglichkeit, einen Zeiger zu verstehen, ist als Pfeil auf einen an einem anderen Ort gespeicherten Wert. In Listing 15-6 erstellen wir eine Referenz auf einen `i32`-Wert und verwenden dann den Dereferenzierungsoperator, um dem Zeiger auf den Wert zu folgen.

Dateiname: `src/main.rs`

```rust
fn main() {
  1 let x = 5;
  2 let y = &x;

  3 assert_eq!(5, x);
  4 assert_eq!(5, *y);
}
```

Listing 15-6: Verwendung des Dereferenzierungsoperators, um einem Zeiger auf einen `i32`-Wert zu folgen

Die Variable `x` enthält einen `i32`-Wert `5` \[1\]. Wir setzen `y` gleich einer Referenz auf `x` \[2\]. Wir können feststellen, dass `x` gleich `5` ist \[3\]. Wenn wir jedoch eine Aussage über den Wert in `y` machen möchten, müssen wir `*y` verwenden, um dem Zeiger auf den Wert zu folgen, auf den er zeigt (d. h. _dereferenzieren_), damit der Compiler den tatsächlichen Wert vergleichen kann \[4\]. Nachdem wir `y` dereferenziert haben, haben wir Zugang zum ganzzahligen Wert, auf den `y` zeigt, den wir mit `5` vergleichen können.

Wenn wir versuchen würden, `assert_eq!(5, y);` zu schreiben, würden wir diesen Kompilierungsfehler erhalten:

```bash
error[E0277]: kann `{integer}` nicht mit `&{integer}` vergleichen
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ keine Implementierung für `{integer} ==
&{integer}`
  |
  = Hilfe: Das Trait `PartialEq<&{integer}>` ist für `{integer}` nicht implementiert
```

Das Vergleichen einer Zahl und einer Referenz auf eine Zahl ist nicht möglich, da es sich um verschiedene Typen handelt. Wir müssen den Dereferenzierungsoperator verwenden, um dem Zeiger auf den Wert zu folgen, auf den er zeigt.
