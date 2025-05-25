# Anotação Explícita

O verificador de empréstimo (borrow checker) usa anotações de tempo de vida explícitas para determinar por quanto tempo as referências devem ser válidas. Em casos onde os tempos de vida não são elididos (elided), Rust requer anotações explícitas para determinar qual deve ser o tempo de vida de uma referência. A sintaxe para anotar explicitamente um tempo de vida usa um apóstrofo da seguinte forma:

```rust
foo<'a>
// `foo` tem um parâmetro de tempo de vida `'a`
```

Semelhante aos closures, o uso de tempos de vida requer genéricos. Adicionalmente, esta sintaxe de tempo de vida indica que o tempo de vida de `foo` pode não exceder o de `'a`. A anotação explícita de um tipo tem a forma `&'a T` onde `'a` já foi introduzido.

Em casos com múltiplos tempos de vida, a sintaxe é semelhante:

```rust
foo<'a, 'b>
// `foo` tem parâmetros de tempo de vida `'a` e `'b`
```

Neste caso, o tempo de vida de `foo` não pode exceder o de `'a` _ou_ `'b`.

Veja o seguinte exemplo para a anotação explícita de tempo de vida em uso:

```rust
// `print_refs` recebe duas referências a `i32` que têm diferentes
// tempos de vida `'a` e `'b`. Estes dois tempos de vida devem ser ambos
// pelo menos tão longos quanto a função `print_refs`.
fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x is {} and y is {}", x, y);
}

// Uma função que não recebe argumentos, mas tem um parâmetro de tempo de vida `'a`.
fn failed_borrow<'a>() {
    let _x = 12;

    // ERROR: `_x` não vive tempo suficiente
    let y: &'a i32 = &_x;
    // Tentar usar o tempo de vida `'a` como uma anotação de tipo explícita
    // dentro da função falhará porque o tempo de vida de `&_x` é mais curto
    // do que o de `y`. Um tempo de vida curto não pode ser forçado a um mais longo.
}

fn main() {
    // Cria variáveis para serem emprestadas abaixo.
    let (four, nine) = (4, 9);

    // Empréstimos (`&`) de ambas as variáveis são passados para a função.
    print_refs(&four, &nine);
    // Qualquer entrada que é emprestada deve sobreviver ao mutuário.
    // Em outras palavras, o tempo de vida de `four` e `nine` deve
    // ser mais longo do que o de `print_refs`.

    failed_borrow();
    // `failed_borrow` não contém referências para forçar `'a` a ser
    // mais longo do que o tempo de vida da função, mas `'a` é mais longo.
    // Porque o tempo de vida nunca é restringido, ele assume o padrão de `'static`.
}
```
