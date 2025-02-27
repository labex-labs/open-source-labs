# Debug

Alle Typen, die die Formatierungseigenschaften von `std::fmt` verwenden möchten, erfordern eine Implementierung, um ausdruckbar zu sein. Automatische Implementierungen werden nur für Typen wie in der `std`-Bibliothek bereitgestellt. Alle anderen müssen auf irgendeine Weise manuell implementiert werden.

Das `fmt::Debug`-Attribut macht dies sehr einfach. _Alle_ Typen können die `fmt::Debug`-Implementierung `ableiten` (automatisch erstellen). Dies gilt nicht für `fmt::Display`, das manuell implementiert werden muss.

```rust
// Diese Struktur kann weder mit `fmt::Display` noch
// mit `fmt::Debug` ausgegeben werden.
struct UnPrintable(i32);

// Das `derive`-Attribut erstellt automatisch die Implementierung,
// die erforderlich ist, um diese `struct` mit `fmt::Debug` ausdruckbar zu machen.
#[derive(Debug)]
struct DebugPrintable(i32);
```

Alle `std`-Bibliothekstypen sind auch automatisch mit `{:?}` ausdruckbar:

```rust
// Leite die `fmt::Debug`-Implementierung für `Structure` ab. `Structure`
// ist eine Struktur, die ein einzelnes `i32` enthält.
#[derive(Debug)]
struct Structure(i32);

// Setze eine `Structure` in die Struktur `Deep`. Mach es auch ausdruckbar.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // Das Ausgeben mit `{:?}` ist ähnlich zu `{}`.
    println!("{:?} Monate im Jahr.", 12);
    println!("{1:?} {0:?} ist der {actor:?} Name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` ist ausdruckbar!
    println!("Jetzt wird {:?} ausgegeben!", Structure(3));

    // Das Problem mit `derive` ist, dass man keine Kontrolle darüber hat,
    // wie die Ergebnisse aussehen. Was, wenn ich möchte, dass nur eine `7` angezeigt wird?
    println!("Jetzt wird {:?} ausgegeben!", Deep(Structure(7)));
}
```

`fmt::Debug` macht also definitiv diese ausdruckbar, opfert aber etwas an Eleganz. Rust bietet auch "schönes Ausgeben" mit `{:#?}`.

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Schönes Ausgeben
    println!("{:#?}", peter);
}
```

Man kann `fmt::Display` manuell implementieren, um die Darstellung zu steuern.
