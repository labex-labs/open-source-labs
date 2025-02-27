# Erstellen von Typsynonymen mit Typalias

Rust bietet die Möglichkeit, einen _Typalias_ zu deklarieren, um einem bestehenden Typ einen anderen Namen zu geben. Dazu verwenden wir das Schlüsselwort `type`. Beispielsweise können wir den Alias `Kilometers` für `i32` wie folgt erstellen:

```rust
type Kilometers = i32;
```

Jetzt ist der Alias `Kilometers` ein _Synonym_ für `i32`; im Gegensatz zu den `Millimeters`- und `Meters`-Typen, die wir in Listing 19-15 erstellt haben, ist `Kilometers` kein separater, neuer Typ. Werte vom Typ `Kilometers` werden genauso behandelt wie Werte vom Typ `i32`:

    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x + y = {}", x + y);

Da `Kilometers` und `i32` der gleiche Typ sind, können wir Werte beider Typen addieren und `Kilometers`-Werte an Funktionen übergeben, die `i32`-Parameter akzeptieren. Mit dieser Methode erhalten wir jedoch nicht die Typsicherheitsvorteile, die wir beim zuvor diskutierten Newtype-Pattern erhalten. Mit anderen Worten, wenn wir `Kilometers`- und `i32`-Werte irgendwo vermischen, gibt der Compiler uns keine Fehlermeldung.

Der Hauptanwendungsfall für Typsynonyme ist die Reduzierung von Wiederholungen. Beispielsweise könnte wir einen längeren Typ wie diesen haben:

```rust
Box<dyn Fn() + Send + 'static>
```

Das Schreiben dieses langen Typs in Funktionssignaturen und als Typanmerkungen überall im Code kann mühsam und fehleranfällig sein. Stellen Sie sich vor, ein Projekt voller Code wie in Listing 19-24.

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

Listing 19-24: Verwenden eines langen Typs an vielen Stellen

Ein Typalias macht diesen Code leichter zu verwalten, indem die Wiederholungen reduziert werden. In Listing 19-25 haben wir einen Alias namens `Thunk` für den umständlichen Typ eingeführt und können alle Verwendung des Typs durch den kürzeren Alias `Thunk` ersetzen.

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

Listing 19-25: Einführung eines Typaliases `Thunk` zur Reduzierung von Wiederholungen

Dieser Code ist viel einfacher lesbar und zu schreiben! Die Wahl eines aussagekräftigen Namens für einen Typalias kann auch dazu beitragen, Ihre Absicht zu kommunizieren (_Thunk_ ist ein Begriff für Code, der zu einem späteren Zeitpunkt ausgewertet werden soll, also ein passender Name für eine Closure, die gespeichert wird).

Typalias werden auch häufig mit dem `Result<T, E>`-Typ verwendet, um Wiederholungen zu reduzieren. Betrachten Sie das `std::io`-Modul in der Standardbibliothek. I/O-Operationen geben oft ein `Result<T, E>` zurück, um Situationen zu behandeln, wenn die Operationen fehlschlagen. Diese Bibliothek hat eine `std::io::Error`-Struktur, die alle möglichen I/O-Fehler darstellt. Viele der Funktionen in `std::io` werden `Result<T, E>` zurückgeben, wobei das `E` `std::io::Error` ist, wie diese Funktionen im `Write`-Trait:

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

Das `Result<..., Error>` wird oft wiederholt. Daher hat `std::io` diese Typaliasdeklaration:

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

Da diese Deklaration im `std::io`-Modul ist, können wir den vollqualifizierten Alias `std::io::Result<T>` verwenden; das heißt, ein `Result<T, E>`, wobei das `E` als `std::io::Error` ausgefüllt ist. Die Funktionssignaturen des `Write`-Traits sehen so aus:

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

Der Typalias hilft auf zwei Wegen: Er macht den Code einfacher zu schreiben _und_ er gibt uns eine konsistente Schnittstelle überall in `std::io`. Da es ein Alias ist, ist es einfach nur ein weiteres `Result<T, E>`, was bedeutet, dass wir alle Methoden verwenden können, die auf `Result<T, E>` funktionieren, sowie besondere Syntax wie den `?`-Operator.
