# Zugreifen auf Werte in einer Hash-Tabelle (Hash Map)

Wir können einen Wert aus der Hash-Tabelle abrufen, indem wir seinen Schlüssel an die `get`-Methode übergeben, wie in Listing 8-21 gezeigt.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Listing 8-21: Zugreifen auf die Punktzahl der Blue-Mannschaft, die in der Hash-Tabelle gespeichert ist

Hier wird `score` den Wert haben, der mit der Blue-Mannschaft verknüpft ist, und das Ergebnis wird `10` sein. Die `get`-Methode gibt ein `Option<&V>` zurück; wenn es in der Hash-Tabelle keinen Wert für diesen Schlüssel gibt, gibt `get` `None` zurück. Dieses Programm behandelt das `Option`-Objekt, indem es `copied` aufruft, um ein `Option<i32>` anstelle eines `Option<&i32>` zu erhalten, und dann `unwrap_or`, um `score` auf Null zu setzen, wenn `scores` keinen Eintrag für den Schlüssel hat.

Wir können über jedes Schlüssel-Wert-Paar in einer Hash-Tabelle auf ähnliche Weise wie bei Vektoren mithilfe einer `for`-Schleife iterieren:

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

Dieser Code wird jedes Paar in beliebiger Reihenfolge ausgeben:

```rust
Yellow: 50
Blue: 10
```
