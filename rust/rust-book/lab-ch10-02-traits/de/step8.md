# Clearer Trait Bounds with where Clauses

Das Verwenden zu vieler Trait Bounds hat Nachteile. Jeder Generic-Typ hat seine eigenen Trait Bounds, sodass Funktionen mit mehreren generischen Typparametern zwischen dem Funktionsnamen und seiner Parameterliste viel Trait-Bound-Information enthalten können, was die Funktionssignatur schwer lesbar macht. Aus diesem Grund hat Rust eine alternative Syntax zum Angeben von Trait Bounds innerhalb einer `where`-Klausel nach der Funktionssignatur. Anstatt also das folgende zu schreiben:

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
```

können wir eine `where`-Klausel verwenden, wie folgt:

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

Die Signatur dieser Funktion ist weniger verwirrt: Der Funktionsname, die Parameterliste und der Rückgabetyp sind dicht beieinander, ähnlich wie bei einer Funktion ohne viele Trait Bounds.
