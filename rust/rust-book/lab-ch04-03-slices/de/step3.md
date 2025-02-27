# String-Literale als Slices

Denken Sie daran, dass wir über die intern im Binär gespeicherten String-Literale gesprochen haben. Jetzt, da wir über Slices Bescheid wissen, können wir String-Literale richtig verstehen:

```rust
let s = "Hello, world!";
```

Der Typ von `s` hier ist `&str`: es ist ein Slice, der auf diesen spezifischen Punkt im Binär zeigt. Dies ist auch der Grund, warum String-Literale unveränderlich sind; `&str` ist eine unveränderliche Referenz.
