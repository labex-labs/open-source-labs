# Hash-Tabellen (Hash Maps) und Besitz (Ownership)

Für Typen, die das `Copy`-Trait implementieren, wie `i32`, werden die Werte in die Hash-Tabelle kopiert. Bei eigenen Werten wie `String` werden die Werte verschoben, und die Hash-Tabelle wird der Besitzer dieser Werte sein, wie in Listing 8-22 gezeigt.

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

Listing 8-22: Zeigt, dass Schlüssel und Werte von der Hash-Tabelle besessen werden, sobald sie eingefügt wurden

Wir können die Variablen `field_name` und `field_value` nicht mehr verwenden, nachdem sie mit dem Aufruf von `insert` in die Hash-Tabelle verschoben wurden.

Wenn wir Referenzen auf Werte in die Hash-Tabelle einfügen, werden die Werte nicht in die Hash-Tabelle verschoben. Die Werte, auf die die Referenzen verweisen, müssen mindestens so lange gültig sein wie die Hash-Tabelle. Wir werden uns diese Probleme ausführlicher in "Validating References with Lifetimes" (Überprüfen von Referenzen mit Lebensdauern) ansehen.
