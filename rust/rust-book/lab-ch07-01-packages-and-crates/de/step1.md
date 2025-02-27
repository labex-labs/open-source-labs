# Packages und Crates

Die ersten Teile des Modulsystems, das wir behandeln werden, sind Packages und Crates.

Ein _Crate_ ist die kleinste Menge an Code, die der Rust-Compiler gleichzeitig betrachtet. Auch wenn Sie `rustc` statt `cargo` ausführen und eine einzelne Quellcode-Datei übergeben (wie wir es schon in "Schreiben und Ausführen eines Rust-Programms" getan haben), betrachtet der Compiler diese Datei als ein Crate. Crates können Module enthalten, und die Module können in anderen Dateien definiert sein, die mit dem Crate kompiliert werden, wie wir in den kommenden Abschnitten sehen werden.

Ein Crate kann in einer von zwei Formen vorliegen: ein binäres Crate oder ein Bibliothekscrate. _Binäre Crates_ sind Programme, die Sie zu einem ausführbaren Programm kompilieren können, das Sie ausführen können, wie z. B. ein Befehlszeilenprogramm oder ein Server. Jeder muss eine Funktion namens `main` haben, die definiert, was passiert, wenn das ausführbare Programm ausgeführt wird. Alle Crates, die wir bisher erstellt haben, waren binäre Crates.

_Bibliothekscrates_ haben keine `main`-Funktion und kompilieren nicht zu einem ausführbaren Programm. Stattdessen definieren sie Funktionalität, die mit mehreren Projekten geteilt werden soll. Beispielsweise bietet das `rand`-Crate, das wir im zweiten Kapitel verwendet haben, Funktionalität, um Zufallszahlen zu generieren. In den meisten Fällen, wenn Rust-Entwickler "Crate" sagen, meinen sie Bibliothekscrate, und sie verwenden "Crate" synonym mit dem allgemeinen Programmierkonzept einer "Bibliothek".

Die _Crate-Wurzel_ ist eine Quellcode-Datei, von der der Rust-Compiler ausgeht und die das Wurzelmodul Ihres Crates bildet (wir werden Module im Abschnitt "Definieren von Modulen zur Kontrolle von Bereich und Privatsphäre" im Detail erklären).

Ein _Package_ ist ein Bund von einem oder mehreren Crates, der eine bestimmte Funktionalität bietet. Ein Package enthält eine `Cargo.toml`-Datei, die beschreibt, wie diese Crates gebaut werden sollen. Cargo ist tatsächlich ein Package, das das binäre Crate für das Befehlszeilenwerkzeug enthält, das Sie bisher verwendet haben, um Ihren Code zu bauen. Das Cargo-Package enthält auch ein Bibliothekscrate, auf das das binäre Crate angewiesen ist. Andere Projekte können auf das Cargo-Bibliothekscrate zurückgreifen, um dieselbe Logik zu verwenden, die das Cargo-Befehlszeilenwerkzeug verwendet.

Ein Crate kann in einer von zwei Formen vorliegen: ein binäres Crate oder ein Bibliothekscrate. Ein Package kann beliebig viele binäre Crates enthalten, aber höchstens nur ein Bibliothekscrate. Ein Package muss mindestens ein Crate enthalten, egal ob es sich um ein Bibliothekscrate oder ein binäres Crate handelt.

Lassen Sie uns durchgehen, was passiert, wenn wir ein Package erstellen. Zunächst geben wir den Befehl `cargo new my-project` ein:

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

Nachdem wir `cargo new my-project` ausgeführt haben, verwenden wir `ls`, um zu sehen, was Cargo erstellt. Im Projektverzeichnis befindet sich eine `Cargo.toml`-Datei, die uns ein Package gibt. Es gibt auch ein `src`-Verzeichnis, das `main.rs` enthält. Öffnen Sie `Cargo.toml` in Ihrem Texteditor und bemerken Sie, dass `src/main.rs` nicht erwähnt wird. Cargo folgt der Konvention, dass `src/main.rs` die Crate-Wurzel eines binären Crates mit dem gleichen Namen wie das Package ist. Ebenso weiß Cargo, dass wenn das Package-Verzeichnis `src/lib.rs` enthält, das Package ein Bibliothekscrate mit dem gleichen Namen wie das Package enthält und `src/lib.rs` seine Crate-Wurzel ist. Cargo übergibt die Crate-Wurzel-Dateien an `rustc`, um die Bibliothek oder das binäre Programm zu bauen.

Hier haben wir ein Package, das nur `src/main.rs` enthält, was bedeutet, dass es nur ein binäres Crate namens `my-project` enthält. Wenn ein Package `src/main.rs` und `src/lib.rs` enthält, hat es zwei Crates: ein binäres und ein Bibliothekscrate, beide mit dem gleichen Namen wie das Package. Ein Package kann mehrere binäre Crates haben, indem Sie Dateien im `src/bin`-Verzeichnis platzieren: jede Datei wird ein separates binäres Crate sein.

> **Modules Cheat Sheet**
>
> Bevor wir auf die Details von Modulen und Pfaden zugehen, geben wir hier einen schnellen Überblick darüber, wie sich Module, Pfade, das `use`-Schlüsselwort und das `pub`-Schlüsselwort im Compiler verhalten und wie die meisten Entwickler ihren Code organisieren. Wir werden in diesem Kapitel Beispiele für jede dieser Regeln durchgehen, aber hier ist ein guter Bezugspunkt, um sich daran zu erinnern, wie die Module funktionieren.
>
> - **Starten von der Crate-Wurzel**: Wenn ein Crate kompiliert wird, sucht der Compiler zunächst in der Crate-Wurzel-Datei (gewöhnlich `src/lib.rs` für ein Bibliothekscrate oder `src/main.rs` für ein binäres Crate) nach Code, der kompiliert werden soll.
> - **Deklarieren von Modulen**: In der Crate-Wurzel-Datei können Sie neue Module deklarieren; sagen Sie, Sie deklarieren ein "garden"-Modul mit `mod garden;`. Der Compiler wird den Code des Moduls an diesen Stellen suchen:
> - Inline, innerhalb geschweifter Klammern, die das Semikolon nach `mod garden` ersetzen
> - In der Datei `src/garden.rs`
> - In der Datei `src/garden/mod.rs`
> - **Deklarieren von Untermodulen**: In jeder Datei außer der Crate-Wurzel können Sie Untermodule deklarieren. Beispielsweise können Sie `mod vegetables;` in `src/garden.rs` deklarieren. Der Compiler wird den Code des Untermoduls innerhalb des Verzeichnisses suchen, das für das übergeordnete Modul benannt ist, an diesen Stellen:
> - Inline, direkt nach `mod vegetables`, innerhalb geschweifter Klammern statt des Semikolons
> - In der Datei `src/garden/vegetables.rs`
> - In der Datei `src/garden/vegetables/mod.rs`
> - **Pfade zu Code in Modulen**: Wenn ein Modul Teil Ihres Crates ist, können Sie auf den Code in diesem Modul von überall anderen im selben Crate zugreifen, solange die Privatsphäre-Regeln es erlauben, indem Sie den Pfad zum Code verwenden. Beispielsweise würde ein `Asparagus`-Typ im Garten-Getreide-Modul bei `crate::garden::vegetables::Asparagus` gefunden werden.
> - **Privat vs. öffentlich**: Der Code innerhalb eines Moduls ist standardmäßig für seine übergeordneten Module privat. Um ein Modul öffentlich zu machen, deklarieren Sie es mit `pub mod` anstelle von `mod`. Um auch die Elemente innerhalb eines öffentlichen Moduls öffentlich zu machen, verwenden Sie `pub` vor ihrer Deklaration.
> - **Das use-Schlüsselwort**: Innerhalb eines Bereichs erzeugt das `use`-Schlüsselwort Kurzschlüsse zu Elementen, um die Wiederholung langer Pfade zu reduzieren. In jedem Bereich, in dem auf `crate::garden::vegetables::Asparagus` verwiesen werden kann, können Sie einen Kurzschluss mit `use crate::garden::vegetables::Asparagus;` erstellen, und ab dann müssen Sie nur `Asparagus` schreiben, um diesen Typ im Bereich zu verwenden.
>
> Hier erstellen wir ein binäres Crate namens `backyard`, das diese Regeln veranschaulicht. Das Verzeichnis des Crates, ebenfalls benannt `backyard`, enthält diese Dateien und Verzeichnisse:
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> Die Crate-Wurzel-Datei in diesem Fall ist `src/main.rs`, und sie enthält:
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> Die Zeile `pub mod garden;` sagt dem Compiler, den Code einzubeziehen, den er in `src/garden.rs` findet, der ist:
>
> ```rust
> pub mod vegetables;
> ```
>
> Hier bedeutet `pub mod vegetables;`, dass auch der Code in `src/garden/vegetables.rs` eingeschlossen wird. Der Code ist:
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> Lassen Sie uns jetzt in die Details dieser Regeln eintauchen und sie in Aktion demonstrieren!
