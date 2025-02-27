# Funciones

El mismo conjunto de reglas se puede aplicar a las funciones: un tipo `T` se convierte en genérico cuando está precedido de `<T>`.

El uso de funciones genéricas a veces requiere especificar explícitamente los parámetros de tipo. Esto puede ser el caso si la función se llama donde el tipo de retorno es genérico, o si el compilador no tiene suficiente información para inferir los parámetros de tipo necesarios.

Una llamada a una función con parámetros de tipo especificados explícitamente se ve así: `fun::<A, B,...>()`.

```rust
struct A;          // Tipo concrete `A`.
struct S(A);       // Tipo concrete `S`.
struct SGen<T>(T); // Tipo genérico `SGen`.

// Las siguientes funciones toman posesión de la variable pasada a
// ellas y salen inmediatamente del ámbito, liberando la variable.

// Define una función `reg_fn` que toma un argumento `_s` de tipo `S`.
// Esto no tiene `<T>` por lo que esta no es una función genérica.
fn reg_fn(_s: S) {}

// Define una función `gen_spec_t` que toma un argumento `_s` de tipo `SGen<T>`.
// Se le ha dado explícitamente el parámetro de tipo `A`, pero como `A` no
// ha sido especificado como un parámetro de tipo genérico para `gen_spec_t`, no es genérica.
fn gen_spec_t(_s: SGen<A>) {}

// Define una función `gen_spec_i32` que toma un argumento `_s` de tipo `SGen<i32>`.
// Se le ha dado explícitamente el parámetro de tipo `i32`, que es un tipo específico.
// Dado que `i32` no es un tipo genérico, esta función también no es genérica.
fn gen_spec_i32(_s: SGen<i32>) {}

// Define una función `generic` que toma un argumento `_s` de tipo `SGen<T>`.
// Dado que `SGen<T>` está precedido de `<T>`, esta función es genérica en `T`.
fn generic<T>(_s: SGen<T>) {}

fn main() {
    // Usando las funciones no genéricas
    reg_fn(S(A));          // Tipo concrete.
    gen_spec_t(SGen(A));   // Parámetro de tipo `A` especificado implícitamente.
    gen_spec_i32(SGen(6)); // Parámetro de tipo `i32` especificado implícitamente.

    // Parámetro de tipo `char` especificado explícitamente para `generic()`.
    generic::<char>(SGen('a'));

    // Parámetro de tipo `char` especificado implícitamente para `generic()`.
    generic(SGen('c'));
}
```
