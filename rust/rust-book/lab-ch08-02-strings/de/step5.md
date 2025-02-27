# Anhängen an einen String mit push_str und push

Wir können einen `String` erweitern, indem wir die `push_str`-Methode verwenden, um einen String-Slice anzuhängen, wie in Listing 8-15 gezeigt.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Listing 8-15: Anhängen eines String-Slices an einen `String` mit der `push_str`-Methode

Nach diesen beiden Zeilen wird `s` den Wert `foobar` enthalten. Die `push_str`-Methode nimmt einen String-Slice entgegen, da wir nicht unbedingt die Eigentumsgewalt über den Parameter übernehmen möchten. Beispielsweise möchten wir in dem Code in Listing 8-16 nach dem Anhängen des Inhalts von `s2` an `s1` weiterhin `s2` verwenden können.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 ist {s2}");
```

Listing 8-16: Verwenden eines String-Slices nach dem Anhängen seines Inhalts an einen `String`

Wenn die `push_str`-Methode die Eigentumsgewalt über `s2` übernehmen würde, könnten wir seinen Wert nicht in der letzten Zeile ausgeben. Dieser Code funktioniert jedoch wie erwartet!

Die `push`-Methode nimmt ein einzelnes Zeichen als Parameter und fügt es zum `String` hinzu. Listing 8-17 fügt den Buchstaben _l_ zu einem `String` mit der `push`-Methode hinzu.

```rust
let mut s = String::from("lo");
s.push('l');
```

Listing 8-17: Hinzufügen eines Zeichens zu einem `String`-Wert mit `push`

Dadurch wird `s` den Wert `lol` enthalten.
