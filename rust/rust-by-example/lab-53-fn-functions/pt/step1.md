# Funções

As funções são declaradas usando a palavra-chave `fn`. Seus argumentos são anotados com tipos, assim como as variáveis, e, se a função retorna um valor, o tipo de retorno deve ser especificado após uma seta `->`.

A expressão final dentro da função será usada como valor de retorno. Alternativamente, a instrução `return` pode ser usada para retornar um valor mais cedo dentro da função, mesmo dentro de loops ou instruções `if`.

Vamos reescrever FizzBuzz usando funções!

```rust
// Ao contrário de C/C++, não há restrição na ordem das definições de funções
fn main() {
    // Podemos usar esta função aqui, e defini-la em outro lugar mais tarde
    fizzbuzz_to(100);
}

// Função que retorna um valor booleano
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // Caso especial, retorno antecipado
    if rhs == 0 {
        return false;
    }

    // Esta é uma expressão, a palavra-chave `return` não é necessária aqui
    lhs % rhs == 0
}

// Funções que "não" retornam um valor, na verdade retornam o tipo unitário `()`
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// Quando uma função retorna `()`, o tipo de retorno pode ser omitido da
// assinatura
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
