# Specifying Multiple Trait Bounds with the + Syntax

Wir können auch mehrere Trait Bounds angeben. Nehmen wir an, dass wir möchten, dass `notify` sowohl die Anzeigeformatierung als auch `summarize` auf `item` verwenden: Wir geben in der `notify`-Definition an, dass `item` sowohl `Display` als auch `Summary` implementieren muss. Wir können dies mit der `+`-Syntax tun:

```rust
pub fn notify(item: &(impl Summary + Display)) {
```

Die `+`-Syntax ist auch gültig mit Trait Bounds für generische Typen:

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```

Mit den zwei angegebenen Trait Bounds kann der Körper von `notify` `summarize` aufrufen und `{}` verwenden, um `item` zu formatieren.
