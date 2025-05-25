# Acessando ou Modificando uma Variável Estática Mutável

Neste livro, ainda não falamos sobre variáveis globais, que o Rust suporta, mas podem ser problemáticas com as regras de propriedade do Rust. Se duas threads estiverem acessando a mesma variável global mutável, isso pode causar uma condição de corrida de dados (data race).

No Rust, as variáveis globais são chamadas de variáveis _estáticas_. A Listagem 19-9 mostra um exemplo de declaração e uso de uma variável estática com uma fatia de string como valor.

Nome do arquivo: `src/main.rs`

```rust
static HELLO_WORLD: &str = "Hello, world!";

fn main() {
    println!("value is: {HELLO_WORLD}");
}
```

Listagem 19-9: Definindo e usando uma variável estática imutável

Variáveis estáticas são semelhantes a constantes, que discutimos em "Constantes". Os nomes das variáveis estáticas estão em `SCREAMING_SNAKE_CASE` por convenção. Variáveis estáticas só podem armazenar referências com o tempo de vida `'static`, o que significa que o compilador Rust pode descobrir o tempo de vida e não somos obrigados a anotá-lo explicitamente. Acessar uma variável estática imutável é seguro.

Uma diferença sutil entre constantes e variáveis estáticas imutáveis é que os valores em uma variável estática têm um endereço fixo na memória. Usar o valor sempre acessará os mesmos dados. As constantes, por outro lado, podem duplicar seus dados sempre que são usadas. Outra diferença é que as variáveis estáticas podem ser mutáveis. Acessar e modificar variáveis estáticas mutáveis é _unsafe_. A Listagem 19-10 mostra como declarar, acessar e modificar uma variável estática mutável chamada `COUNTER`.

Nome do arquivo: `src/main.rs`

```rust
static mut COUNTER: u32 = 0;

fn add_to_count(inc: u32) {
    unsafe {
        COUNTER += inc;
    }
}

fn main() {
    add_to_count(3);

    unsafe {
        println!("COUNTER: {COUNTER}");
    }
}
```

Listagem 19-10: Ler ou escrever em uma variável estática mutável é unsafe.

Assim como com variáveis regulares, especificamos a mutabilidade usando a palavra-chave `mut`. Qualquer código que lê ou escreve de `COUNTER` deve estar dentro de um bloco `unsafe`. Este código compila e imprime `COUNTER: 3` como esperaríamos porque é single threaded. Ter várias threads acessando `COUNTER` provavelmente resultaria em condições de corrida de dados.

Com dados mutáveis que são globalmente acessíveis, é difícil garantir que não haja condições de corrida de dados, e é por isso que o Rust considera variáveis estáticas mutáveis como unsafe. Sempre que possível, é preferível usar as técnicas de concorrência e ponteiros inteligentes thread-safe que discutimos no Capítulo 16 para que o compilador verifique se o acesso aos dados de diferentes threads é feito com segurança.
