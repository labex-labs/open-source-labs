# Verwendung der Kurzschreibweise für Feldinitialisierung

Da die Parameter-Namen und die Struct-Feldnamen in Listing 5-4 genau gleich sind, können wir die Syntax der _Kurzschreibweise für Feldinitialisierung_ verwenden, um `build_user` umzuschreiben, sodass es genau das gleiche Verhalten hat, aber ohne die Wiederholung von `username` und `email`, wie in Listing 5-5 gezeigt.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}
```

Listing 5-5: Eine `build_user`-Funktion, die die Kurzschreibweise für Feldinitialisierung verwendet, da die `username`- und `email`-Parameter den gleichen Namen wie die Struct-Felder haben

Hier erstellen wir eine neue Instanz des `User`-Structs, der ein Feld namens `email` hat. Wir möchten den Wert des `email`-Felds auf den Wert des `email`-Parameters der `build_user`-Funktion setzen. Da das `email`-Feld und der `email`-Parameter den gleichen Namen haben, müssen wir nur `email` schreiben, anstatt `email: email`.
