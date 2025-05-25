# Lendo os Valores dos Argumentos

Para permitir que `minigrep` leia os valores dos argumentos da linha de comando que passamos para ele, precisaremos da função `std::env::args` fornecida na biblioteca padrão do Rust. Esta função retorna um iterador dos argumentos da linha de comando passados para `minigrep`. Abordaremos iteradores completamente no Capítulo 13. Por enquanto, você só precisa saber dois detalhes sobre iteradores: iteradores produzem uma série de valores, e podemos chamar o método `collect` em um iterador para transformá-lo em uma coleção, como um vetor, que contém todos os elementos que o iterador produz.

O código na Listagem 12-1 permite que seu programa `minigrep` leia quaisquer argumentos da linha de comando passados para ele e, em seguida, colete os valores em um vetor.

Nome do arquivo: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

Listagem 12-1: Coletando os argumentos da linha de comando em um vetor e imprimindo-os

Primeiro, trazemos o módulo `std::env` para o escopo com uma instrução `use` para que possamos usar sua função `args`. Observe que a função `std::env::args` está aninhada em dois níveis de módulos. Como discutimos no Capítulo 7, em casos em que a função desejada está aninhada em mais de um módulo, optamos por trazer o módulo pai para o escopo em vez da função. Ao fazer isso, podemos usar facilmente outras funções de `std::env`. Também é menos ambíguo do que adicionar `use std::env::args` e, em seguida, chamar a função apenas com `args`, porque `args` pode ser facilmente confundido com uma função que é definida no módulo atual.

> **A Função args e Unicode Inválido**
>
> Observe que `std::env::args` entrará em pânico se algum argumento contiver Unicode inválido. Se seu programa precisar aceitar argumentos contendo Unicode inválido, use `std::env::args_os` em vez disso. Essa função retorna um iterador que produz valores `OsString` em vez de valores `String`. Escolhemos usar `std::env::args` aqui por simplicidade, porque os valores `OsString` diferem por plataforma e são mais complexos de trabalhar do que os valores `String`.

Na primeira linha de `main`, chamamos `env::args` e imediatamente usamos `collect` para transformar o iterador em um vetor contendo todos os valores produzidos pelo iterador. Podemos usar a função `collect` para criar muitos tipos de coleções, então anotamos explicitamente o tipo de `args` para especificar que queremos um vetor de strings. Embora você raramente precise anotar tipos em Rust, `collect` é uma função que você frequentemente precisa anotar porque o Rust não é capaz de inferir o tipo de coleção que você deseja.

Finalmente, imprimimos o vetor usando a macro de depuração. Vamos tentar executar o código primeiro sem argumentos e depois com dois argumentos:

```bash
$ cargo run
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
]
$ cargo run -- needle haystack
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
"needle",
"haystack",
]
```

Observe que o primeiro valor no vetor é `"target/debug/minigrep"`, que é o nome do nosso binário. Isso corresponde ao comportamento da lista de argumentos em C, permitindo que os programas usem o nome pelo qual foram invocados em sua execução. É frequentemente conveniente ter acesso ao nome do programa caso você queira imprimi-lo em mensagens ou alterar o comportamento do programa com base em qual alias da linha de comando foi usado para invocar o programa. Mas, para os propósitos deste capítulo, vamos ignorá-lo e salvar apenas os dois argumentos de que precisamos.
