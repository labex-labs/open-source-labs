# Trait Bound Syntax

Die `impl Trait`-Syntax funktioniert für einfache Fälle, ist aber tatsächlich syntaktischer Zucker für eine längere Form, die als _Trait Bound_ bekannt ist; es sieht so aus:

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

Diese längere Form ist der Beispiel in der vorherigen Section äquivalent, ist aber ausführlicher. Wir setzen Trait Bounds mit der Deklaration des generischen Typparameters nach einem Doppelpunkt und innerhalb von spitzen Klammern.

Die `impl Trait`-Syntax ist praktisch und führt in einfachen Fällen zu kürzerem Code, während die vollständige Trait Bound-Syntax in anderen Fällen mehr Komplexität ausdrücken kann. Beispielsweise können wir zwei Parameter haben, die `Summary` implementieren. Dies sieht mit der `impl Trait`-Syntax so aus:

```rust
pub fn notify(item1: &impl Summary, item2: &impl Summary) {
```

Das Verwenden von `impl Trait` ist geeignet, wenn wir möchten, dass diese Funktion `item1` und `item2` verschiedene Typen haben lässt (solange beide Typen `Summary` implementieren). Wenn wir jedoch beide Parameter zwingen, den gleichen Typ zu haben, müssen wir einen Trait Bound verwenden, wie folgt:

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
```

Der generische Typ `T`, der als Typ der `item1`- und `item2`-Parameter angegeben wird, beschränkt die Funktion so, dass der konkrete Typ des Werts, der als Argument für `item1` und `item2` übergeben wird, der gleiche sein muss.
