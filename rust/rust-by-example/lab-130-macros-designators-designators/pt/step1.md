# Designadores

Os argumentos de uma macro são prefixados por um sinal de dólar `$` e anotados com tipo com um _designador_:

```rust
macro_rules! create_function {
    // Esta macro recebe um argumento do designador `ident` e
    // cria uma função chamada `$func_name`.
    // O designador `ident` é usado para nomes de variáveis/funções.
    ($func_name:ident) => {
        fn $func_name() {
            // A macro `stringify!` converte um `ident` em uma string.
            println!("Você chamou {:?}()",
                     stringify!($func_name));
        }
    };
}

// Crie funções chamadas `foo` e `bar` com a macro acima.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Esta macro recebe uma expressão do tipo `expr` e a imprime
    // como uma string junto com seu resultado.
    // O designador `expr` é usado para expressões.
    ($expression:expr) => {
        // `stringify!` converterá a expressão *como ela é* em uma string.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Lembre-se que blocos também são expressões!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

Estes são alguns dos designadores disponíveis:

- `block`
- `expr` é usado para expressões
- `ident` é usado para nomes de variáveis/funções
- `item`
- `literal` é usado para constantes literais
- `pat` (_padrão_)
- `path`
- `stmt` (_declaração_)
- `tt` (_árvore de tokens_)
- `ty` (_tipo_)
- `vis` (_qualificador de visibilidade_)

Para uma lista completa, consulte a \[Referência Rust\].
