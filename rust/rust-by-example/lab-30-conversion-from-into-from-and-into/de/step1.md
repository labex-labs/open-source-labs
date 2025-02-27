# `From` und `Into`

Die Traits [`From`](#from) und [`Into`](#into) sind von Natur aus miteinander verknüpft, und das ist tatsächlich Teil ihrer Implementierung. Wenn Sie in der Lage sind, Typ A aus Typ B umzuwandeln, dann sollte es leicht zu glauben sein, dass wir in der Lage sein sollten, Typ B in Typ A umzuwandeln.

## `From`

Der Trait [`From`](#from) ermöglicht es einem Typ, festzulegen, wie er sich selbst aus einem anderen Typ erstellt, und bietet somit einen sehr einfachen Mechanismus zur Umwandlung zwischen mehreren Typen. Es gibt zahlreiche Implementierungen dieses Traits in der Standardbibliothek für die Umwandlung von primitiven und üblichen Typen.

Zum Beispiel können wir leicht einen `str` in eine `String` umwandeln

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

Wir können ähnliches tun, um eine Umwandlung für unseren eigenen Typ zu definieren.

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

Der Trait [`Into`](#into) ist einfach das Gegenteil des `From`-Traits. Das heißt, wenn Sie den `From`-Trait für Ihren Typ implementiert haben, ruft `Into` ihn bei Bedarf auf.

Das Verwenden des `Into`-Traits erfordert normalerweise die Angabe des Typs, in den umgewandelt werden soll, da der Compiler dies in der Regel nicht bestimmen kann. Dies ist jedoch ein geringer Kompromiss, wenn man bedenkt, dass wir diese Funktionalität kostenlos erhalten.

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // Versuchen Sie, die Typangabe zu entfernen
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
