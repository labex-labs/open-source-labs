# Überschreiben eines Werts

Wenn wir einen Schlüssel und einen Wert in eine Hash-Tabelle einfügen und dann denselben Schlüssel mit einem anderen Wert einfügen, wird der mit diesem Schlüssel verknüpfte Wert ersetzt. Auch wenn der Code in Listing 8-23 zweimal `insert` aufruft, enthält die Hash-Tabelle nur ein Schlüssel-Wert-Paar, da wir beide Male den Wert für den Schlüssel der Blue-Mannschaft einfügen.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

Listing 8-23: Ersetzen eines mit einem bestimmten Schlüssel gespeicherten Werts

Dieser Code wird `{"Blue": 25}` ausgeben. Der ursprüngliche Wert von `10` wurde überschrieben.
