# if let

Für einige Anwendungsfälle ist `match` bei der Abgleichung von Enums umständlich. Beispielsweise:

```rust
// Definiere `optional` vom Typ `Option<i32>`
let optional = Some(7);

match optional {
    Some(i) => {
        println!("Dies ist ein wirklich langer String und `{:?}`", i);
        // ^ Zwei Einzüge erforderlich, um `i` aus der Option zu extrahieren.
    },
    _ => {},
    // ^ Erforderlich, da `match` erschöpfend ist. Sieht das nicht wie verschwendeter Platz aus?
};
```

`if let` ist für diesen Anwendungsfall sauberer und erlaubt zusätzlich die Angabe verschiedener Fehlermöglichkeiten:

```rust
fn main() {
    // Alle haben den Typ `Option<i32>`
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // Der `if let`-Ausdruck lautet: "Wenn `let` `number` in `Some(i)` auflöst,
    // führe den Block (`{}`) aus."
    if let Some(i) = number {
        println!("Matched {:?}!", i);
    }

    // Wenn Sie einen Fehler angeben müssen, verwenden Sie ein `else`:
    if let Some(i) = letter {
        println!("Matched {:?}!", i);
    } else {
        // Die Auflösung ist fehlgeschlagen. Wechseln Sie zum Fehlerfall.
        println!("Hat keine Zahl übereinstimmt. Lass es mit einem Buchstaben sein!");
    }

    // Geben Sie eine veränderte Fehlerbedingung an.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Matched {:?}!", i);
    // Die Auflösung ist fehlgeschlagen.计算一个`else if`条件，看是否应该采用替代的失败分支：
    } else if i_like_letters {
        println!("Hat keine Zahl übereinstimmt. Lass es mit einem Buchstaben sein!");
    } else {
        // Die Bedingung hat false ergeben. Dieser Zweig ist die Standardoption:
        println!("Ich mag keine Buchstaben. Lass es mit einem Emoticon :) sein!");
    }
}
```

Auf die gleiche Weise kann `if let` verwendet werden, um jeden Enum-Wert abzugleichen:

```rust
// Unser Beispiel-Enum
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // Erstellen Sie Beispielvariablen
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // Variable a stimmt mit Foo::Bar überein
    if let Foo::Bar = a {
        println!("a ist foobar");
    }

    // Variable b stimmt nicht mit Foo::Bar überein
    // Daher wird nichts ausgegeben
    if let Foo::Bar = b {
        println!("b ist foobar");
    }

    // Variable c stimmt mit Foo::Qux überein, das einen Wert hat
    // Ähnlich wie Some() im vorherigen Beispiel
    if let Foo::Qux(value) = c {
        println!("c ist {}", value);
    }

    // Die Bindung funktioniert auch mit `if let`
    if let Foo::Qux(value @ 100) = c {
        println!("c ist einhundert");
    }
}
```

Ein weiterer Vorteil ist, dass `if let` uns ermöglicht, nicht parametrisierte Enum-Varianten abzugleichen. Dies gilt auch in Fällen, in denen das Enum `PartialEq` nicht implementiert oder abgeleitet hat. In solchen Fällen würde `if Foo::Bar == a` fehlschlagen, weil Instanzen des Enums nicht verglichen werden können, jedoch wird `if let` weiterhin funktionieren.

Möchten Sie eine Herausforderung annehmen? Reparieren Sie das folgende Beispiel, um `if let` zu verwenden:

```rust
// Dieses Enum implementiert und leitet absichtlich weder `PartialEq` ab.
// Deshalb schlägt das Vergleichen von Foo::Bar == a unten fehl.
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // Variable a stimmt mit Foo::Bar überein
    if Foo::Bar == a {
    // ^-- Dies verursacht einen Kompilierungsfehler. Verwenden Sie stattdessen `if let`.
        println!("a ist foobar");
    }
}
```
