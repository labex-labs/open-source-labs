# Definieren eines Traits für gemeinsames Verhalten

Um das Verhalten zu implementieren, das wir für `gui` wünschen, werden wir einen Trait namens `Draw` definieren, der eine Methode namens `draw` haben wird. Dann können wir einen Vektor definieren, der ein _Trait-Objekt_ annimmt. Ein Trait-Objekt weist sowohl auf eine Instanz eines Typs, der unseren angegebenen Trait implementiert, als auch auf eine Tabelle, die zur Laufzeit verwendet wird, um Trait-Methoden auf diesem Typ aufzurufen. Wir erstellen ein Trait-Objekt, indem wir einen gewissen Zeiger wie eine `&`-Referenz oder einen `Box<T>`-Smart-Pointer angeben, dann das `dyn`-Schlüsselwort und anschließend den relevanten Trait angeben. (Wir werden im Abschnitt "Dynamically Sized Types and the Sized Trait" über den Grund sprechen, warum Trait-Objekte einen Zeiger verwenden müssen.) Wir können Trait-Objekte anstelle eines generischen oder konkreten Typs verwenden. Überall, wo wir ein Trait-Objekt verwenden, wird das Typsystem von Rust zur Compile-Zeit sicherstellen, dass jeder Wert, der in diesem Kontext verwendet wird, den Trait des Trait-Objekts implementiert. Folglich müssen wir zu Compile-Zeit nicht alle möglichen Typen kennen.

Wir haben erwähnt, dass wir in Rust von der Bezeichnung "Objekte" für Structs und Enums absehen, um sie von den Objekten anderer Sprachen zu unterscheiden. In einem Struct oder Enum sind die Daten in den Struct-Feldern und das Verhalten in `impl`-Blöcken getrennt, während in anderen Sprachen das die Daten und das Verhalten in einem kombinierten Konzept oft als Objekt bezeichnet wird. Trait-Objekte sind jedoch insofern ähnlicher wie Objekte in anderen Sprachen, als dass sie Daten und Verhalten kombinieren. Trait-Objekte unterscheiden sich jedoch von traditionellen Objekten darin, dass wir keinem Trait-Objekt Daten hinzufügen können. Trait-Objekte sind nicht so allgemein nützlich wie Objekte in anderen Sprachen: Ihr spezielles Ziel ist es, die Abstraktion über gemeinsames Verhalten zu ermöglichen.

Listing 17-3 zeigt, wie man einen Trait namens `Draw` mit einer Methode namens `draw` definiert.

Dateiname: `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Listing 17-3: Definition des `Draw`-Traits

Diese Syntax sollte uns aus unseren Diskussionen über die Definition von Traits im Kapitel 10 bekannt sein. Als nächstes kommt eine neue Syntax: Listing 17-4 definiert eine Struct namens `Screen`, die einen Vektor namens `components` enthält. Dieser Vektor ist vom Typ `Box<dyn Draw>`, was ein Trait-Objekt ist; es ist ein Ersatz für jeden Typ innerhalb eines `Box`, der den `Draw`-Trait implementiert.

Dateiname: `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Listing 17-4: Definition der `Screen`-Struct mit einem `components`-Feld, das einen Vektor von Trait-Objekten enthält, die den `Draw`-Trait implementieren

Auf der `Screen`-Struct werden wir eine Methode namens `run` definieren, die die `draw`-Methode auf jedem ihrer `components` aufruft, wie in Listing 17-5 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-5: Eine `run`-Methode auf `Screen`, die die `draw`-Methode auf jedem Komponenten aufruft

Dies funktioniert anders als die Definition eines Structs, der einen generischen Typparameter mit Trait-Bounds verwendet. Ein generischer Typparameter kann nur zu einem konkreten Typ ersetzt werden, während Trait-Objekte es ermöglichen, mehrere konkrete Typen zur Laufzeit für das Trait-Objekt einzufügen. Beispielsweise hätten wir die `Screen`-Struct wie in Listing 17-6 mit einem generischen Typ und einem Trait-Bound definieren können.

Dateiname: `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-6: Eine alternative Implementierung der `Screen`-Struct und ihrer `run`-Methode mit Generics und Trait-Bounds

Dies beschränkt uns auf eine `Screen`-Instanz, die eine Liste von Komponenten hat, die alle vom Typ `Button` oder alle vom Typ `TextField` sind. Wenn Sie nur homogene Sammlungen haben, ist die Verwendung von Generics und Trait-Bounds bevorzugt, da die Definitionen zur Compile-Zeit monomorphisiert werden, um die konkreten Typen zu verwenden.

Andererseits kann eine `Screen`-Instanz mit der Methode, die Trait-Objekte verwendet, einen `Vec<T>` enthalten, der sowohl eine `Box<Button>` als auch eine `Box<TextField>` enthält. Schauen wir uns an, wie dies funktioniert, und dann werden wir über die Auswirkungen auf die Laufzeitleistung sprechen.
