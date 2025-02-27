# Fonctions

Le même ensemble de règles peut être appliqué aux fonctions : un type `T` devient générique lorsqu'il est précédé de `<T>`.

L'utilisation de fonctions génériques peut parfois nécessiter la spécification explicite des paramètres de type. Cela peut être le cas si la fonction est appelée avec un type de retour générique, ou si le compilateur n'a pas suffisamment d'informations pour déduire les paramètres de type nécessaires.

Un appel de fonction avec des paramètres de type spécifiés explicitement ressemble à ceci : `fun::<A, B,...>()`.

```rust
struct A;          // Type concret `A`.
struct S(A);       // Type concret `S`.
struct SGen<T>(T); // Type générique `SGen`.

// Les fonctions suivantes prennent toutes en compte la variable passée en
// argument et sortent immédiatement du portée, libérant la variable.

// Définissez une fonction `reg_fn` qui prend un argument `_s` de type `S`.
// Cela n'a pas de `<T>` donc ce n'est pas une fonction générique.
fn reg_fn(_s: S) {}

// Définissez une fonction `gen_spec_t` qui prend un argument `_s` de type `SGen<T>`.
// Elle a été explicitement donnée le paramètre de type `A`, mais parce que `A` n'a pas
// été spécifié comme paramètre de type générique pour `gen_spec_t`, elle n'est pas générique.
fn gen_spec_t(_s: SGen<A>) {}

// Définissez une fonction `gen_spec_i32` qui prend un argument `_s` de type `SGen<i32>`.
// Elle a été explicitement donnée le paramètre de type `i32`, qui est un type spécifique.
// Parce que `i32` n'est pas un type générique, cette fonction n'est pas non plus générique.
fn gen_spec_i32(_s: SGen<i32>) {}

// Définissez une fonction `generic` qui prend un argument `_s` de type `SGen<T>`.
// Parce que `SGen<T>` est précédé de `<T>`, cette fonction est générique sur `T`.
fn generic<T>(_s: SGen<T>) {}

fn main() {
    // Utilisation des fonctions non génériques
    reg_fn(S(A));          // Type concret.
    gen_spec_t(SGen(A));   // Paramètre de type `A` spécifié implicitement.
    gen_spec_i32(SGen(6)); // Paramètre de type `i32` spécifié implicitement.

    // Paramètre de type `char` spécifié explicitement pour `generic()`.
    generic::<char>(SGen('a'));

    // Paramètre de type `char` spécifié implicitement pour `generic()`.
    generic(SGen('c'));
}
```
