# Erstellen von Instanzen aus anderen Instanzen mit der Struct-Update-Syntax

Es ist oft nützlich, eine neue Instanz eines Structs zu erstellen, die die meisten Werte aus einer anderen Instanz enthält, aber einige ändert. Dies kannst du mit der _Struct-Update-Syntax_ tun.

Zunächst zeigen wir in Listing 5-6, wie man normalerweise eine neue `User`-Instanz in `user2` erstellt, ohne die Update-Syntax. Wir setzen einen neuen Wert für `email`, verwenden aber sonst die gleichen Werte aus `user1`, die wir in Listing 5-2 erstellt haben.

Dateiname: `src/main.rs`

```rust
fn main() {
    --snip--

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
}
```

Listing 5-6: Erstellen einer neuen `User`-Instanz, indem man einen der Werte aus `user1` verwendet

Mit der Struct-Update-Syntax können wir das gleiche Ergebnis mit weniger Code erreichen, wie in Listing 5-7 gezeigt. Die Syntax `..` gibt an, dass die verbleibenden Felder, die nicht explizit festgelegt werden, den gleichen Wert wie die Felder in der angegebenen Instanz haben sollen.

Dateiname: `src/main.rs`

```rust
fn main() {
    --snip--


    let user2 = User {
        email: String::from("another@example.com"),
      ..user1
    };
}
```

Listing 5-7: Verwenden der Struct-Update-Syntax, um einen neuen `email`-Wert für eine `User`-Instanz festzulegen, aber die restlichen Werte aus `user1` zu verwenden

Der Code in Listing 5-7 erstellt auch eine Instanz in `user2`, die einen anderen Wert für `email` hat, aber die gleichen Werte für die `username`, `active` und `sign_in_count`-Felder aus `user1` hat. Das `..user1` muss zuletzt stehen, um anzugeben, dass alle verbleibenden Felder ihre Werte aus den entsprechenden Feldern in `user1` erhalten sollen, aber wir können uns entscheiden, beliebig viele Felder in beliebiger Reihenfolge Werte zuzuweisen, unabhängig von der Reihenfolge der Felder in der Struct-Definition.

Beachte, dass die Struct-Update-Syntax `=` wie eine Zuweisung verwendet; dies liegt daran, dass sie die Daten bewegt, genau wie wir es in "Variablen und Daten, die mit Move interagieren" gesehen haben. In diesem Beispiel können wir `user1` nicht mehr verwenden, nachdem wir `user2` erstellt haben, weil die `String` im `username`-Feld von `user1` in `user2` bewegt wurde. Wenn wir `user2` sowohl für `email` als auch für `username` neue `String`-Werte gegeben hätten und somit nur die `active`- und `sign_in_count`-Werte aus `user1` verwendet hätten, wäre `user1` nach dem Erstellen von `user2` immer noch gültig. Sowohl `active` als auch `sign_in_count` sind Typen, die das `Copy`-Trait implementieren, sodass das Verhalten, das wir in "Nur auf dem Stack gespeicherte Daten: Copy" diskutiert haben, anwendbar wäre.
