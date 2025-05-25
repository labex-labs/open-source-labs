# Salvando os Valores dos Argumentos em Variáveis

O programa atualmente é capaz de acessar os valores especificados como argumentos da linha de comando. Agora precisamos salvar os valores dos dois argumentos em variáveis para que possamos usar os valores em todo o restante do programa. Fazemos isso na Listagem 12-2.

Nome do arquivo: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Listagem 12-2: Criando variáveis para armazenar o argumento de consulta e o argumento do caminho do arquivo

Como vimos quando imprimimos o vetor, o nome do programa ocupa o primeiro valor no vetor em `args[0]`, então estamos começando os argumentos no índice 1. O primeiro argumento que `minigrep` recebe é a string que estamos procurando, então colocamos uma referência ao primeiro argumento na variável `query`. O segundo argumento será o caminho do arquivo, então colocamos uma referência ao segundo argumento na variável `file_path`.

Imprimimos temporariamente os valores dessas variáveis para provar que o código está funcionando como pretendemos. Vamos executar este programa novamente com os argumentos `test` e `sample.txt`:

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Ótimo, o programa está funcionando! Os valores dos argumentos que precisamos estão sendo salvos nas variáveis corretas. Mais tarde, adicionaremos algum tratamento de erros para lidar com certas situações potencialmente errôneas, como quando o usuário não fornece argumentos; por enquanto, ignoraremos essa situação e trabalharemos na adição de recursos de leitura de arquivos.
