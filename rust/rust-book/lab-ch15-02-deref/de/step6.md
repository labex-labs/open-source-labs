# Implizite Deref-Zwangsumwandlungen mit Funktionen und Methoden

_Deref-Zwangsumwandlung_ wandelt eine Referenz auf einen Typ, der das `Deref`-Trait implementiert, in eine Referenz auf einen anderen Typ um. Beispielsweise kann die Deref-Zwangsumwandlung `&String` in `&str` umwandeln, weil `String` das `Deref`-Trait so implementiert, dass es `&str` zurückgibt. Die Deref-Zwangsumwandlung ist eine Bequemlichkeit, die Rust bei Argumenten von Funktionen und Methoden vornimmt und funktioniert nur für Typen, die das `Deref`-Trait implementieren. Sie geschieht automatisch, wenn wir eine Referenz auf einen Wert eines bestimmten Typs als Argument an eine Funktion oder Methode übergeben, die nicht mit dem Parametertyp in der Funktions- oder Methodendefinition übereinstimmt. Eine Folge von Aufrufen der `deref`-Methode wandelt den von uns bereitgestellten Typ in den Typ um, den das Parameter benötigt.

Die Deref-Zwangsumwandlung wurde in Rust hinzugefügt, damit Programmierer, die Funktions- und Methodenaufrufe schreiben, nicht so viele explizite Referenzen und Dereferenzierungen mit `&` und `*` hinzufügen müssen. Die Deref-Zwangsumwandlungsfunktion ermöglicht es uns auch, mehr Code zu schreiben, der sowohl für Referenzen als auch für Smart Pointer funktioniert.

Um die Deref-Zwangsumwandlung an einem Beispiel zu sehen, verwenden wir den in Listing 15-8 definierten `MyBox<T>`-Typ sowie die in Listing 15-10 hinzugefügte Implementierung von `Deref`. Listing 15-11 zeigt die Definition einer Funktion, die einen String-Slice-Parameter hat.

Dateiname: `src/main.rs`

```rust
fn hello(name: &str) {
    println!("Hello, {name}!");
}
```

Listing 15-11: Eine `hello`-Funktion mit dem Parameter `name` vom Typ `&str`

Wir können die `hello`-Funktion mit einem String-Slice als Argument aufrufen, z. B. `hello("Rust");`. Die Deref-Zwangsumwandlung ermöglicht es, `hello` mit einer Referenz auf einen Wert vom Typ `MyBox<String>` aufzurufen, wie in Listing 15-12 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Listing 15-12: Aufrufen von `hello` mit einer Referenz auf einen `MyBox<String>`-Wert, was aufgrund der Deref-Zwangsumwandlung funktioniert

Wir rufen hier die `hello`-Funktion mit dem Argument `&m` auf, was eine Referenz auf einen `MyBox<String>`-Wert ist. Weil wir das `Deref`-Trait für `MyBox<T>` in Listing 15-10 implementiert haben, kann Rust `&MyBox<String>` in `&String` umwandeln, indem es `deref` aufruft. Die Standardbibliothek liefert eine Implementierung von `Deref` für `String`, die einen String-Slice zurückgibt, und dies ist in der API-Dokumentation für `Deref`. Rust ruft `deref` erneut auf, um das `&String` in `&str` umzuwandeln, was der Definition der `hello`-Funktion entspricht.

Wenn Rust keine Deref-Zwangsumwandlung implementieren würde, müssten wir den Code in Listing 15-13 schreiben, anstatt den Code in Listing 15-12, um `hello` mit einem Wert vom Typ `&MyBox<String>` aufzurufen.

Dateiname: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&(*m)[..]);
}
```

Listing 15-13: Der Code, den wir schreiben müssten, wenn Rust keine Deref-Zwangsumwandlung hätte

Die `(*m)` dereferenziert das `MyBox<String>` in eine `String`. Dann nehmen die `&` und `[..]` einen String-Slice der `String`, der gleich der gesamten Zeichenkette ist, um der Signatur von `hello` zu entsprechen. Dieser Code ohne Deref-Zwangsumwandlungen ist schwerer lesbar, zu schreiben und zu verstehen, da all diese Symbole beteiligt sind. Die Deref-Zwangsumwandlung ermöglicht es Rust, diese Umwandlungen für uns automatisch zu verarbeiten.

Wenn das `Deref`-Trait für die beteiligten Typen definiert ist, wird Rust die Typen analysieren und so oft wie nötig `Deref::deref` verwenden, um eine Referenz zu erhalten, die mit dem Parametertyp übereinstimmt. Die Anzahl der Mal, wie `Deref::deref` eingefügt werden muss, wird zur Compile-Zeit bestimmt, sodass es keine Laufzeitbelastung gibt, um von der Deref-Zwangsumwandlung Gebrauch zu machen!
