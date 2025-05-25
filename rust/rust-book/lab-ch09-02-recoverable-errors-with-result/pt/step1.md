# Erros Recuperáveis com Result

A maioria dos erros não são sérios o suficiente para exigir que o programa pare completamente. Às vezes, quando uma função falha, é por uma razão que você pode facilmente interpretar e responder. Por exemplo, se você tentar abrir um arquivo e essa operação falhar porque o arquivo não existe, você pode querer criar o arquivo em vez de terminar o processo.

Lembre-se de "Lidando com Falhas Potenciais com Result" que o enum `Result` é definido como tendo duas variantes, `Ok` e `Err`, da seguinte forma:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

`T` e `E` são parâmetros de tipo genéricos: discutiremos genéricos com mais detalhes no Capítulo 10. O que você precisa saber agora é que `T` representa o tipo do valor que será retornado em um caso de sucesso dentro da variante `Ok`, e `E` representa o tipo do erro que será retornado em um caso de falha dentro da variante `Err`. Como `Result` tem esses parâmetros de tipo genéricos, podemos usar o tipo `Result` e as funções definidas nele em muitas situações diferentes onde o valor de sucesso e o valor de erro que queremos retornar podem diferir.

Vamos chamar uma função que retorna um valor `Result` porque a função pode falhar. No Listing 9-3, tentamos abrir um arquivo.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

Listing 9-3: Abrindo um arquivo

O tipo de retorno de `File::open` é um `Result<T, E>`. O parâmetro genérico `T` foi preenchido pela implementação de `File::open` com o tipo do valor de sucesso, `std::fs::File`, que é um manipulador de arquivo. O tipo de `E` usado no valor de erro é `std::io::Error`. Este tipo de retorno significa que a chamada para `File::open` pode ter sucesso e retornar um manipulador de arquivo que podemos ler ou escrever. A chamada da função também pode falhar: por exemplo, o arquivo pode não existir, ou podemos não ter permissão para acessar o arquivo. A função `File::open` precisa ter uma maneira de nos dizer se teve sucesso ou falhou e, ao mesmo tempo, nos dar o manipulador de arquivo ou informações de erro. Essa informação é exatamente o que o enum `Result` transmite.

No caso em que `File::open` tem sucesso, o valor na variável `greeting_file_result` será uma instância de `Ok` que contém um manipulador de arquivo. No caso em que falha, o valor em `greeting_file_result` será uma instância de `Err` que contém mais informações sobre o tipo de erro que ocorreu.

Precisamos adicionar ao código no Listing 9-3 para tomar ações diferentes dependendo do valor que `File::open` retorna. O Listing 9-4 mostra uma maneira de lidar com o `Result` usando uma ferramenta básica, a expressão `match` que discutimos no Capítulo 6.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

Listing 9-4: Usando uma expressão `match` para lidar com as variantes `Result` que podem ser retornadas

Observe que, como o enum `Option`, o enum `Result` e suas variantes foram trazidos para o escopo pelo prelúdio, então não precisamos especificar `Result::` antes das variantes `Ok` e `Err` nos braços `match`.

Quando o resultado é `Ok`, este código retornará o valor `file` interno da variante `Ok`, e então atribuímos esse valor de manipulador de arquivo à variável `greeting_file`. Após o `match`, podemos usar o manipulador de arquivo para leitura ou escrita.

O outro braço do `match` lida com o caso em que recebemos um valor `Err` de `File::open`. Neste exemplo, escolhemos chamar a macro `panic!`. Se não houver um arquivo chamado _hello.txt_ em nosso diretório atual e executarmos este código, veremos a seguinte saída da macro `panic!`:

    thread 'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

Como de costume, esta saída nos diz exatamente o que deu errado.
