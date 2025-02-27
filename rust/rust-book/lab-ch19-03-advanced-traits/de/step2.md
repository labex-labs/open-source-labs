# Assoziierte Typen

_Assoziierte Typen_ verbinden einen Typ-Platzhalter mit einem Trait, sodass die Trait-Methodendefinitionen diese Platzhaltertypen in ihren Signaturen verwenden können. Der Implementierer eines Traits wird den konkreten Typ angeben, der anstelle des Platzhaltertyps für die spezifische Implementierung verwendet werden soll. Auf diese Weise können wir einen Trait definieren, der einige Typen verwendet, ohne genau zu wissen, welche diese Typen sind, bis der Trait implementiert wird.

Wir haben die meisten der fortgeschrittenen Funktionen in diesem Kapitel als selten benötigt beschrieben. Assoziierte Typen befinden sich dazwischen: Sie werden seltener verwendet als die Funktionen, die im Rest des Buches erklärt werden, aber häufiger als viele der anderen in diesem Kapitel diskutierten Funktionen.

Ein Beispiel für einen Trait mit einem assoziierten Typ ist der `Iterator`-Trait, den die Standardbibliothek bereitstellt. Der assoziierte Typ heißt `Item` und steht für den Typ der Werte, über die der Typ, der das `Iterator`-Trait implementiert, iteriert. Die Definition des `Iterator`-Traits ist wie in Listing 19-12 gezeigt.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Listing 19-12: Die Definition des `Iterator`-Traits, der einen assoziierten Typ `Item` hat

Der Typ `Item` ist ein Platzhalter, und die Definition der `next`-Methode zeigt, dass sie Werte vom Typ `Option<Self::Item>` zurückgeben wird. Implementierer des `Iterator`-Traits werden den konkreten Typ für `Item` angeben, und die `next`-Methode wird eine `Option` zurückgeben, die einen Wert dieses konkreten Typs enthält.

Assoziierte Typen können wie ein ähnliches Konzept zu Generics erscheinen, in dem letztere uns ermöglichen, eine Funktion zu definieren, ohne anzugeben, welche Typen sie verarbeiten kann. Um den Unterschied zwischen den beiden Konzepten zu untersuchen, betrachten wir eine Implementierung des `Iterator`-Traits für einen Typ namens `Counter`, der angibt, dass der `Item`-Typ `u32` ist:

Dateiname: `src/lib.rs`

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        --snip--
```

Diese Syntax scheint der von Generics vergleichbar zu sein. Warum definieren wir den `Iterator`-Trait also nicht einfach mit Generics, wie in Listing 19-13 gezeigt?

```rust
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}
```

Listing 19-13: Eine hypothetische Definition des `Iterator`-Traits mit Generics

Der Unterschied besteht darin, dass wir bei der Verwendung von Generics wie in Listing 19-13 die Typen in jeder Implementierung annotieren müssen; da wir auch `Iterator<``String``> für Counter` oder irgendeinen anderen Typ implementieren können, könnten wir für `Counter` mehrere Implementierungen von `Iterator` haben. Mit anderen Worten, wenn ein Trait einen generischen Parameter hat, kann es für einen Typ mehrfach implementiert werden, wobei die konkreten Typen der generischen Typparameter jeweils geändert werden. Wenn wir die `next`-Methode auf `Counter` verwenden, müssten wir Typ-Annotationen angeben, um anzuzeigen, welche Implementierung von `Iterator` wir verwenden möchten.

Mit assoziierten Typen müssen wir die Typen nicht annotieren, weil wir einen Trait für einen Typ nicht mehrfach implementieren können. In Listing 19-12 mit der Definition, die assoziierte Typen verwendet, können wir nur einmal wählen, was der Typ von `Item` sein wird, da es nur eine `impl Iterator for Counter` geben kann. Wir müssen nicht überall dort angeben, dass wir einen Iterator von `u32`-Werten möchten, wo wir `next` auf `Counter` aufrufen.

Assoziierte Typen werden auch zum Vertrag des Traits: Implementierer des Traits müssen einen Typ angeben, um für den assoziierten Typ-Platzhalter zu stehen. Assoziierte Typen haben oft einen Namen, der beschreibt, wie der Typ verwendet wird, und es ist eine gute Praxis, den assoziierten Typ in der API-Dokumentation zu dokumentieren.
