# Aliasing

L'instruction `type` peut être utilisée pour donner un nouveau nom à un type existant. Les types doivent avoir des noms au format `UpperCamelCase`, sinon le compilateur générera un avertissement. L'exception à cette règle sont les types primitifs : `usize`, `f32`, etc.

```rust
// `NanoSecond`, `Inch` et `U64` sont de nouveaux noms pour `u64`.
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`.
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // Notez que les alias de type *ne* fournissent pas de sécurité supplémentaire au niveau du type, car
    // les alias ne sont *pas* de nouveaux types
    println!("{} nanosecondes + {} pouces = {} unité?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

L'utilisation principale des alias est de réduire le code répétitif ; par exemple, le type `io::Result<T>` est un alias pour le type `Result<T, io::Error>`.
