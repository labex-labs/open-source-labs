# Zugreifen auf oder Ändern einer veränderlichen statischen Variable

In diesem Buch haben wir bisher noch nicht über globale Variablen gesprochen, die Rust zwar unterstützt, aber mit den Besitzregeln von Rust problematisch sein können. Wenn zwei Threads auf die gleiche veränderliche globale Variable zugreifen, kann dies einen Datenkonflikt verursachen.

In Rust werden globale Variablen als _statische_ Variablen bezeichnet. Listing 19-9 zeigt ein Beispiel für die Deklaration und Verwendung einer statischen Variable mit einem String-Slice als Wert.

Dateiname: `src/main.rs`

```rust
static HELLO_WORLD: &str = "Hello, world!";

fn main() {
    println!("value is: {HELLO_WORLD}");
}
```

Listing 19-9: Definieren und Verwenden einer unveränderlichen statischen Variable

Statische Variablen ähneln Konstanten, über die wir in "Konstanten" gesprochen haben. Die Namen von statischen Variablen folgen der Konvention `SCREAMING_SNAKE_CASE`. Statische Variablen können nur Referenzen mit der Lebensdauer `'static` speichern, was bedeutet, dass der Rust-Compiler die Lebensdauer ermitteln kann und wir nicht explizit annotieren müssen. Das Zugreifen auf eine unveränderliche statische Variable ist sicher.

Ein subtiler Unterschied zwischen Konstanten und unveränderlichen statischen Variablen ist, dass die Werte in einer statischen Variable eine feste Adresse im Speicher haben. Das Verwenden des Werts wird immer auf die gleichen Daten zugreifen. Konstanten hingegen sind erlaubt, ihre Daten jedes Mal zu duplizieren, wenn sie verwendet werden. Ein weiterer Unterschied ist, dass statische Variablen veränderlich sein können. Das Zugreifen auf und das Ändern von veränderlichen statischen Variablen ist _unsicher_. Listing 19-10 zeigt, wie man eine veränderliche statische Variable namens `COUNTER` deklariert, zugreift und modifiziert.

Dateiname: `src/main.rs`

```rust
static mut COUNTER: u32 = 0;

fn add_to_count(inc: u32) {
    unsafe {
        COUNTER += inc;
    }
}

fn main() {
    add_to_count(3);

    unsafe {
        println!("COUNTER: {COUNTER}");
    }
}
```

Listing 19-10: Das Lesen aus oder Schreiben in eine veränderliche statische Variable ist unsicher.

Wie bei regulären Variablen verwenden wir das `mut`-Schlüsselwort, um Veränderbarkeit anzugeben. Jeder Code, der von `COUNTER` liest oder schreibt, muss innerhalb eines `unsafe`-Blocks sein. Dieser Code kompiliert und druckt wie erwartet `COUNTER: 3`, da es ein einzelner Thread ist. Wenn mehrere Threads auf `COUNTER` zugreifen, würde wahrscheinlich ein Datenkonflikt auftreten.

Bei veränderlichen Daten, die global zugänglich sind, ist es schwierig, sicherzustellen, dass es keine Datenkonflikte gibt, weshalb Rust veränderliche statische Variablen als unsicher betrachtet. Wo möglich, ist es besser, die in Kapitel 16 diskutierten Konkurrenztechniken und thread-sicheren Smart-Pointer zu verwenden, damit der Compiler überprüft, dass der Datenzugang von verschiedenen Threads sicher erfolgt.
