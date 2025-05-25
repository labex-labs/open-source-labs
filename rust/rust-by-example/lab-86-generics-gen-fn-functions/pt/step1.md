# Funções

O mesmo conjunto de regras pode ser aplicado a funções: um tipo `T` torna-se genérico quando precedido por `<T>`.

O uso de funções genéricas às vezes requer a especificação explícita de parâmetros de tipo. Isto pode ser necessário se a função for chamada onde o tipo de retorno é genérico, ou se o compilador não tiver informações suficientes para inferir os parâmetros de tipo necessários.

Uma chamada de função com parâmetros de tipo especificados explicitamente tem a seguinte forma: `fun::<A, B, ...>()`.

```rust
struct A;          // Tipo concreto `A`.
struct S(A);       // Tipo concreto `S`.
struct SGen<T>(T); // Tipo genérico `SGen`.

// As funções seguintes recebem a posse da variável passada para elas e imediatamente saem do escopo, liberando a variável.

// Define uma função `reg_fn` que recebe um argumento `_s` do tipo `S`.
// Esta função não tem `<T>`, portanto não é uma função genérica.
fn reg_fn(_s: S) {}

// Define uma função `gen_spec_t` que recebe um argumento `_s` do tipo `SGen<T>`.
// Foi-lhe dado explicitamente o parâmetro de tipo `A`, mas como `A` não foi especificado como um parâmetro de tipo genérico para `gen_spec_t`, não é genérica.
fn gen_spec_t(_s: SGen<A>) {}

// Define uma função `gen_spec_i32` que recebe um argumento `_s` do tipo `SGen<i32>`.
// Foi-lhe dado explicitamente o parâmetro de tipo `i32`, que é um tipo específico.
// Como `i32` não é um tipo genérico, esta função também não é genérica.
fn gen_spec_i32(_s: SGen<i32>) {}

// Define uma função `generic` que recebe um argumento `_s` do tipo `SGen<T>`.
// Como `SGen<T>` é precedido por `<T>`, esta função é genérica em relação a `T`.
fn generic<T>(_s: SGen<T>) {}

fn main() {
    // Usando as funções não genéricas
    reg_fn(S(A));          // Tipo concreto.
    gen_spec_t(SGen(A));   // Parâmetro de tipo `A` especificado implicitamente.
    gen_spec_i32(SGen(6)); // Parâmetro de tipo `i32` especificado implicitamente.

    // Parâmetro de tipo `char` especificado explicitamente para `generic()`.
    generic::<char>(SGen('a'));

    // Parâmetro de tipo `char` especificado implicitamente para `generic()`.
    generic(SGen('c'));
}
```
