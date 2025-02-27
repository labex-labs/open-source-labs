# Funktionen

Die gleichen Regeln können auf Funktionen angewendet werden: Ein Typ `T` wird generisch, wenn er mit `<T>` vorangestellt wird.

Das Verwenden generischer Funktionen erfordert manchmal die explizite Angabe von Typparametern. Dies kann der Fall sein, wenn die Funktion aufgerufen wird, wobei der Rückgabetyp generisch ist, oder wenn der Compiler nicht genug Informationen hat, um die erforderlichen Typparameter zu inferieren.

Ein Funktionsaufruf mit explizit angegebenen Typparametern sieht wie folgt aus: `fun::<A, B,...>()`

```rust
struct A;          // Konkreter Typ `A`.
struct S(A);       // Konkreter Typ `S`.
struct SGen<T>(T); // Generischer Typ `SGen`.

// Die folgenden Funktionen übernehmen alle die Besitznahme der in sie
// übergebenen Variable und gehen sofort außer Gültigkeit, was die Variable freigibt.

// Definiere eine Funktion `reg_fn`, die ein Argument `_s` vom Typ `S` annimmt.
// Dies hat kein `<T>`, also ist dies keine generische Funktion.
fn reg_fn(_s: S) {}

// Definiere eine Funktion `gen_spec_t`, die ein Argument `_s` vom Typ `SGen<T>` annimmt.
// Es wurde explizit der Typparameter `A` gegeben, aber da `A` nicht als generischer
// Typparameter für `gen_spec_t` angegeben wurde, ist es nicht generisch.
fn gen_spec_t(_s: SGen<A>) {}

// Definiere eine Funktion `gen_spec_i32`, die ein Argument `_s` vom Typ `SGen<i32>` annimmt.
// Es wurde explizit der Typparameter `i32` gegeben, was ein spezifischer Typ ist.
// Da `i32` kein generischer Typ ist, ist diese Funktion auch nicht generisch.
fn gen_spec_i32(_s: SGen<i32>) {}

// Definiere eine Funktion `generic`, die ein Argument `_s` vom Typ `SGen<T>` annimmt.
// Da `SGen<T>` mit `<T>` vorangestellt ist, ist diese Funktion generisch über `T`.
fn generic<T>(_s: SGen<T>) {}

fn main() {
    // Verwende die nicht-generischen Funktionen
    reg_fn(S(A));          // Konkreter Typ.
    gen_spec_t(SGen(A));   // Implizit angegebenen Typparameter `A`.
    gen_spec_i32(SGen(6)); // Implizit angegebenen Typparameter `i32`.

    // Explizit angegebenen Typparameter `char` für `generic()`.
    generic::<char>(SGen('a'));

    // Implizit angegebenen Typparameter `char` für `generic()`.
    generic(SGen('c'));
}
```
