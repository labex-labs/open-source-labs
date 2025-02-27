# Wie man einen benutzerdefinierten `derive`-Makro schreibt

Lassen Sie uns einen Kratzerzeugnis namens `hello_macro` erstellen, der ein Trait namens `HelloMacro` mit einer assoziierten Funktion namens `hello_macro` definiert. Anstatt es unseren Benutzern zu ermöglichen, das `HelloMacro`-Trait für jede ihrer Typen zu implementieren, werden wir ein prozedurales Makro bereitstellen, sodass die Benutzer ihr Typ mit `#[derive(HelloMacro)]` annotieren können, um eine Standardimplementierung der `hello_macro`-Funktion zu erhalten. Die Standardimplementierung wird `Hello, Macro! My name is` TypeName`!` ausgeben, wobei TypeName der Name des Typs ist, für den dieses Trait definiert wurde. Mit anderen Worten, wir werden ein Kratzerzeugnis schreiben, das es einem anderen Programmierer ermöglicht, Code wie in Listing 19-30 mit unserem Kratzerzeugnis zu schreiben.

Dateiname: `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

Listing 19-30: Der Code, den ein Benutzer unseres Kratzerzeugnisses schreiben kann, wenn er unser prozedurales Makro verwendet

Dieser Code wird `Hello, Macro! My name is Pancakes!` ausgeben, wenn wir fertig sind. Der erste Schritt ist es, ein neues Bibliothekskratzerzeugnis zu erstellen, wie folgt:

```bash
cargo new hello_macro --lib
```

Als nächstes werden wir das `HelloMacro`-Trait und seine assoziierte Funktion definieren:

Dateiname: `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

Wir haben ein Trait und seine Funktion. Zu diesem Zeitpunkt könnte der Benutzer unseres Kratzerzeugnisses das Trait implementieren, um die gewünschte Funktionalität zu erreichen, wie folgt:

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

Allerdings müssten sie den Implementierungsblock für jeden Typ schreiben, den sie mit `hello_macro` verwenden möchten; wir möchten sie davor bewahren, diese Arbeit zu erledigen.

Zusätzlich können wir der `hello_macro`-Funktion noch keine Standardimplementierung geben, die den Namen des Typs ausgibt, für den das Trait implementiert wird: Rust hat keine Reflektionseigenschaften, sodass es die Typenamen zur Laufzeit nicht auflösen kann. Wir brauchen ein Makro, um Code zur Compilezeit zu generieren.

Der nächste Schritt ist es, das prozedurale Makro zu definieren. Zum Zeitpunkt der Verfassung dieses Dokuments müssen prozedurale Makros in ihrem eigenen Kratzerzeugnis liegen. Eventuell wird diese Einschränkung in Zukunft aufgehoben. Die Konvention für die Struktur von Kratzerzeugnissen und Makrokratzerzeugnissen lautet wie folgt: für ein Kratzerzeugnis namens foo wird ein benutzerdefiniertes `derive`-prozedurales Makrokratzerzeugnis `foo`\_derive genannt. Lassen Sie uns ein neues Kratzerzeugnis namens `hello_macro_derive` im Verzeichnis unseres `hello_macro`-Projekts starten:

```bash
cargo new hello_macro_derive --lib
```

Unsere beiden Kratzerzeugnisse sind eng miteinander verbunden, sodass wir das prozedurale Makrokratzerzeugnis innerhalb des Verzeichnisses unseres `hello_macro`-Kratzerzeugnisses erstellen. Wenn wir die Traitdefinition in `hello_macro` ändern, müssen wir auch die Implementierung des prozeduralen Makros in `hello_macro_derive` ändern. Die beiden Kratzerzeugnisse müssen separat veröffentlicht werden, und Programmierer, die diese Kratzerzeugnisse verwenden, müssen beide als Abhängigkeiten hinzufügen und beide in den Gültigkeitsbereich bringen. Stattdessen könnten wir das `hello_macro`-Kratzerzeugnis `hello_macro_derive` als Abhängigkeit verwenden und den Code des prozeduralen Makros erneut exportieren. Allerdings ermöglicht die von uns gewählte Projektstruktur es Programmierern, `hello_macro` zu verwenden, auch wenn sie die `derive`-Funktionalität nicht benötigen.

Wir müssen das `hello_macro_derive`-Kratzerzeugnis als prozedurales Makrokratzerzeugnis deklarieren. Wir werden auch Funktionalität aus den Kratzerzeugnissen `syn` und `quote` benötigen, wie Sie gleich sehen werden, sodass wir sie als Abhängigkeiten hinzufügen müssen. Fügen Sie dem `Cargo.toml`-Datei für `hello_macro_derive` Folgendes hinzu:

Dateiname: `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

Um das prozedurale Makro zu definieren, legen Sie den Code in Listing 19-31 in Ihre `src/lib.rs`-Datei für das `hello_macro_derive`-Kratzerzeugnis. Beachten Sie, dass dieser Code nicht kompilieren wird, bis wir eine Definition für die `impl_hello_macro`-Funktion hinzufügen.

Dateiname: `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Konstruieren Sie eine Darstellung von Rust-Code als Syntaxbaum,
    // auf den wir zugreifen können
    let ast = syn::parse(input).unwrap();

    // Erstellen Sie die Traitimplementierung
    impl_hello_macro(&ast)
}
```

Listing 19-31: Code, den die meisten prozeduralen Makrokratzerzeugnisse benötigen, um Rust-Code zu verarbeiten

Beachten Sie, dass wir den Code in die `hello_macro_derive`-Funktion unterteilt haben, die für das Parsen des `TokenStream` verantwortlich ist, und die `impl_hello_macro`-Funktion, die für die Transformation des Syntaxbaums verantwortlich ist: Dies macht das Schreiben eines prozeduralen Makros komfortabler. Der Code in der äußeren Funktion (`hello_macro_derive` in diesem Fall) wird für fast jedes prozedurale Makrokratzerzeugnis, das Sie sehen oder erstellen, gleich sein. Der Code, den Sie im Körper der inneren Funktion (`impl_hello_macro` in diesem Fall) angeben, wird je nach Zweck Ihres prozeduralen Makros unterschiedlich sein.

Wir haben drei neue Kratzerzeugnisse eingeführt: `proc_macro`, `syn` (verfügbar unter *https://crates.io/crates/syn*) und `quote` (verfügbar unter *https://crates.io/crates/quote*). Das `proc_macro`-Kratzerzeugnis kommt mit Rust mit, sodass wir es nicht zu den Abhängigkeiten in `Cargo.toml` hinzufügen mussten. Das `proc_macro`-Kratzerzeugnis ist die API des Compilers, die uns ermöglicht, Rust-Code aus unserem Code zu lesen und zu manipulieren.

Das `syn`-Kratzerzeugnis analysiert Rust-Code aus einer Zeichenfolge in eine Datenstruktur, auf die wir Operationen ausführen können. Das `quote`-Kratzerzeugnis wandelt `syn`-Datenstrukturen wieder in Rust-Code um. Diese Kratzerzeugnisse machen es viel einfacher, beliebigen Rust-Code zu analysieren, den wir behandeln möchten: das Schreiben eines vollständigen Parsers für Rust-Code ist keine einfache Aufgabe.

Die `hello_macro_derive`-Funktion wird aufgerufen, wenn ein Benutzer unseres Bibliothekskratzerzeugnisses ein Typ mit `#[derive(HelloMacro)]` annotiert. Dies ist möglich, da wir die `hello_macro_derive`-Funktion hier mit `proc_macro_derive` annotiert haben und den Namen `HelloMacro` angegeben haben, der unserem Traitnamen entspricht; dies ist die Konvention, die die meisten prozeduralen Makros befolgen.

Die `hello_macro_derive`-Funktion konvertiert zunächst die `input` von einem `TokenStream` in eine Datenstruktur, auf die wir dann zugreifen und Operationen ausführen können. Hier kommt `syn` ins Spiel. Die `parse`-Funktion in `syn` nimmt einen `TokenStream` und gibt eine `DeriveInput`-Struktur zurück, die den analysierten Rust-Code repräsentiert. Listing 19-32 zeigt die relevanten Teile der `DeriveInput`-Struktur, die wir beim Parsen der Zeichenfolge `struct Pancakes;` erhalten.

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

Listing 19-32: Die `DeriveInput`-Instanz, die wir erhalten, wenn wir den Code in Listing 19-30 analysieren, der das Attribut des Makros enthält

Die Felder dieser Struktur zeigen, dass der Rust-Code, den wir analysiert haben, eine Einheitenstruktur mit dem `ident` (_Bezeichner_, also dem Namen) von `Pancakes` ist. Es gibt weitere Felder in dieser Struktur, um alle Arten von Rust-Code zu beschreiben; überprüfen Sie die `syn`-Dokumentation für `DeriveInput` unter *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* für weitere Informationen.

Bald werden wir die `impl_hello_macro`-Funktion definieren, in der wir den neuen Rust-Code erstellen, den wir hinzufügen möchten. Bevor wir dies tun, beachten Sie, dass die Ausgabe unseres `derive`-Makros ebenfalls ein `TokenStream` ist. Der zurückgegebene `TokenStream` wird zum Code hinzugefügt, den die Benutzer unseres Kratzerzeugnisses schreiben, sodass sie beim Kompilieren ihres Kratzerzeugnisses die zusätzliche Funktionalität erhalten, die wir in dem modifizierten `TokenStream` bereitstellen.

Sie haben vielleicht bemerkt, dass wir `unwrap` aufrufen, um die `hello_macro_derive`-Funktion dazu zu bringen, einen Fehler auszulösen, wenn der Aufruf der `syn::parse`-Funktion fehlschlägt. Es ist notwendig, dass unser prozedurales Makro bei Fehlern einen Fehler auslöst, da `proc_macro_derive`-Funktionen `TokenStream` statt `Result` zurückgeben müssen, um der prozeduralen Makro-API zu entsprechen. Wir haben diesen Beispiel durch die Verwendung von `unwrap` vereinfacht; in der Produktionscode sollten Sie spezifischere Fehlermeldungen übergeben, was schiefgelaufen ist, indem Sie `panic!` oder `expect` verwenden.

Jetzt, da wir den Code haben, um den annotierten Rust-Code von einem `TokenStream` in eine `DeriveInput`-Instanz umzuwandeln, generieren wir den Code, der das `HelloMacro`-Trait auf dem annotierten Typ implementiert, wie in Listing 19-33 gezeigt.

Dateiname: `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

Listing 19-33: Implementieren des `HelloMacro`-Traits mit dem analysierten Rust-Code

Wir erhalten eine `Ident`-Strukturinstanz, die den Namen (Bezeichner) des annotierten Typs enthält, indem wir `ast.ident` verwenden. Die Struktur in Listing 19-32 zeigt, dass wenn wir die `impl_hello_macro`-Funktion auf den Code in Listing 19-30 ausführen, das `ident`, das wir erhalten, das `ident`-Feld mit einem Wert von `"Pancakes"` haben wird. Somit wird die `name`-Variable in Listing 19-33 eine `Ident`-Strukturinstanz enthalten, die beim Drucken die Zeichenfolge `"Pancakes"`, den Namen der Struktur in Listing 19-30, sein wird.

Die `quote!`-Makro ermöglicht es uns, den Rust-Code zu definieren, den wir zurückgeben möchten. Der Compiler erwartet etwas anderes als das direkte Ergebnis der Ausführung des `quote!`-Makros, sodass wir es in einen `TokenStream` umwandeln müssen. Wir tun dies, indem wir die `into`-Methode aufrufen, die diese Zwischenrepräsentation konsumiert und einen Wert des erforderlichen `TokenStream`-Typs zurückgibt.

Das `quote!`-Makro bietet auch einige sehr coole Templatesmechaniken: wir können `#name` eingeben, und `quote!` wird es mit dem Wert in der Variable `name` ersetzen. Sie können sogar eine gewisse Wiederholung durchführen, ähnlich wie bei regulären Makros. Überprüfen Sie die `quote`-Kratzerzeugnis-Dokumentation unter *https://docs.rs/quote* für eine umfassende Einführung.

Wir möchten, dass unser prozedurales Makro eine Implementierung unseres `HelloMacro`-Traits für den Typ erzeugt, den der Benutzer annotiert hat, was wir mit `#name` erhalten können. Die Traitimplementierung hat die eine Funktion `hello_macro`, deren Körper die Funktionalität enthält, die wir bereitstellen möchten: das Ausgeben von `Hello, Macro! My name is` und dann dem Namen des annotierten Typs.

Das hier verwendete `stringify!`-Makro ist in Rust integriert. Es nimmt einen Rust-Ausdruck, wie z. B. `1 + 2`, und wandelt ihn zur Compilezeit in einen Stringliteral um, wie z. B. `"1 + 2"`. Dies unterscheidet sich von `format!` oder `println!`, Makros, die den Ausdruck auswerten und das Ergebnis dann in eine `String` umwandeln. Es besteht die Möglichkeit, dass der `#name`-Eingabe ein Ausdruck ist, der buchstäblich gedruckt werden soll, sodass wir `stringify!` verwenden. Die Verwendung von `stringify!` spart auch eine Allokation, indem `#name` zur Compilezeit in einen Stringliteral umgewandelt wird.

An diesem Punkt sollte `cargo build` in beiden `hello_macro` und `hello_macro_derive` erfolgreich abgeschlossen werden. Lassen Sie uns diese Kratzerzeugnisse mit dem Code in Listing 19-30 verbinden, um das prozedurale Makro in Aktion zu sehen! Erstellen Sie ein neues binäres Projekt im `project`-Verzeichnis mit `cargo new pancakes`. Wir müssen `hello_macro` und `hello_macro_derive` als Abhängigkeiten in der `Cargo.toml` des `pancakes`-Kratzerzeugnisses hinzufügen. Wenn Sie Ihre Versionen von `hello_macro` und `hello_macro_derive` auf *https://crates.io* veröffentlichen, wären sie reguläre Abhängigkeiten; wenn nicht, können Sie sie als `path`-Abhängigkeiten wie folgt angeben:

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

Legen Sie den Code in Listing 19-30 in `src/main.rs` ab, und führen Sie `cargo run` aus: es sollte `Hello, Macro! My name is Pancakes!` ausgeben. Die Implementierung des `HelloMacro`-Traits aus dem prozeduralen Makro wurde ohne dass das `pancakes`-Kratzerzeugnis es implementieren musste, hinzugefügt; das `#[derive(HelloMacro)]` hat die Traitimplementierung hinzugefügt.

Als nächstes werden wir untersuchen, wie sich die anderen Arten von prozeduralen Makros von benutzerdefinierten `derive`-Makros unterscheiden.
