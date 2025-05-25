# Lendo um Arquivo

Agora, adicionaremos funcionalidade para ler o arquivo especificado no argumento `file_path`. Primeiro, precisamos de um arquivo de amostra para testá-lo: usaremos um arquivo com uma pequena quantidade de texto em várias linhas com algumas palavras repetidas. A Listagem 12-3 tem um poema de Emily Dickinson que funcionará bem! Crie um arquivo chamado _poem.txt_ na raiz do seu projeto e insira o poema "I'm Nobody! Who are you?"

Nome do arquivo: poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

Listagem 12-3: Um poema de Emily Dickinson é um bom caso de teste.

Com o texto no lugar, edite `src/main.rs` e adicione código para ler o arquivo, conforme mostrado na Listagem 12-4.

Nome do arquivo: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listagem 12-4: Lendo o conteúdo do arquivo especificado pelo segundo argumento

Primeiro, importamos uma parte relevante da biblioteca padrão com uma instrução `use`: precisamos de `std::fs` para lidar com arquivos \[1].

Em `main`, a nova instrução `fs::read_to_string` recebe o `file_path`, abre esse arquivo e retorna um `std::io::Result<String>` do conteúdo do arquivo \[2].

Depois disso, adicionamos novamente uma instrução `println!` temporária que imprime o valor de `contents` após a leitura do arquivo, para que possamos verificar se o programa está funcionando até agora \[3].

Vamos executar este código com qualquer string como o primeiro argumento da linha de comando (porque ainda não implementamos a parte de busca) e o arquivo _poem.txt_ como o segundo argumento:

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Ótimo! O código leu e, em seguida, imprimiu o conteúdo do arquivo. Mas o código tem algumas falhas. No momento, a função `main` tem múltiplas responsabilidades: geralmente, as funções são mais claras e fáceis de manter se cada função for responsável por apenas uma ideia. O outro problema é que não estamos lidando com erros tão bem quanto poderíamos. O programa ainda é pequeno, então essas falhas não são um grande problema, mas à medida que o programa cresce, será mais difícil corrigi-las de forma limpa. É uma boa prática começar a refatorar no início do desenvolvimento de um programa, porque é muito mais fácil refatorar pequenas quantidades de código. Faremos isso a seguir.
