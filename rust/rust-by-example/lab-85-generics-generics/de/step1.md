# Generics

_Generics_ ist das Thema der Verallgemeinerung von Typen und Funktionalitäten auf breitere Fälle. Dies ist extrem nützlich, um Code-Duplizierung auf vielen Wegen zu reduzieren, erfordert jedoch oft eine ziemlich komplexe Syntax. Namentlich erfordert es, bei der Definition von generischen Typen mit größter Sorgfalt festzulegen, über welche Typen ein generischer Typ tatsächlich als gültig angesehen wird. Die einfachste und am häufigsten verwendete Verwendung von Generics sind Typ-Parameter.

Ein Typ-Parameter wird als generisch durch die Verwendung von spitzen Klammern und Großbuchstaben angegeben, typischerweise als `<T>`. In Rust beschreibt "generisch" auch alles, was einen oder mehrere generische Typ-Parameter `<T>` akzeptiert. Jeder Typ, der als generischer Typ-Parameter angegeben ist, ist generisch, und alles andere ist konkret (nicht-generisch).

Beispielsweise definieren wir eine _generische Funktion_ namens `foo`, die ein Argument `T` beliebigen Typs annimmt:

```rust
fn foo<T>(arg: T) {... }
```

Da `T` als generischer Typ-Parameter mit `<T>` angegeben wurde, wird es hier als `(arg: T)` verwendet als generisch betrachtet. Dies ist auch dann der Fall, wenn `T` zuvor als `struct` definiert wurde.

Dieses Beispiel zeigt einige der Syntax in Aktion:

```rust
// Ein konkreter Typ `A`.
struct A;

// Beim Definieren des Typs `Single` wird der erste Gebrauch von `A` nicht durch `<A>` vorangestellt.
// Daher ist `Single` ein konkreter Typ, und `A` ist wie oben definiert.
struct Single(A);
//            ^ Hier ist der erste Gebrauch von `Single` des Typs `A`.

// Hier wird `<T>` vor dem ersten Gebrauch von `T` eingesetzt, daher ist `SingleGen` ein generischer Typ.
// Da der Typ-Parameter `T` generisch ist, kann es alles sein, einschließlich des konkreten Typs `A` oben definiert.
struct SingleGen<T>(T);

fn main() {
    // `Single` ist konkret und nimmt explizit `A` an.
    let _s = Single(A);

    // Erstellen Sie eine Variable `_char` vom Typ `SingleGen<char>`
    // und geben Sie ihr den Wert `SingleGen('a')`.
    // Hier ist der Typ-Parameter von `SingleGen` explizit angegeben.
    let _char: SingleGen<char> = SingleGen('a');

    // `SingleGen` kann auch einen Typ-Parameter implizit angegeben haben:
    let _t    = SingleGen(A); // Verwendet `A` oben definiert.
    let _i32  = SingleGen(6); // Verwendet `i32`.
    let _char = SingleGen('a'); // Verwendet `char`.
}
```
