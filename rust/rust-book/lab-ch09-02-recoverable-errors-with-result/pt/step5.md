# Propagando Erros

Quando a implementação de uma função chama algo que pode falhar, em vez de lidar com o erro dentro da própria função, você pode retornar o erro para o código chamador para que ele possa decidir o que fazer. Isso é conhecido como _propagação_ do erro e dá mais controle ao código chamador, onde pode haver mais informações ou lógica que ditam como o erro deve ser tratado do que o que você tem disponível no contexto do seu código.

Por exemplo, o Listing 9-6 mostra uma função que lê um nome de usuário de um arquivo. Se o arquivo não existir ou não puder ser lido, esta função retornará esses erros para o código que chamou a função.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

1 fn read_username_from_file() -> Result<String, io::Error> {
  2 let username_file_result = File::open("hello.txt");

  3 let mut username_file = match username_file_result {
      4 Ok(file) => file,
      5 Err(e) => return Err(e),
    };

  6 let mut username = String::new();

  7 match username_file.read_to_string(&mut username) {
      8 Ok(_) => Ok(username),
      9 Err(e) => Err(e),
    }
}
```

Listing 9-6: Uma função que retorna erros para o código chamador usando `match`

Esta função pode ser escrita de uma forma muito mais curta, mas vamos começar fazendo muito disso manualmente para explorar o tratamento de erros; no final, mostraremos a forma mais curta. Vamos olhar primeiro para o tipo de retorno da função: `Result<String, io::Error>` \[1]. Isso significa que a função está retornando um valor do tipo `Result<T, E>`, onde o parâmetro genérico `T` foi preenchido com o tipo concreto `String` e o tipo genérico `E` foi preenchido com o tipo concreto `io::Error`.

Se esta função for bem-sucedida sem nenhum problema, o código que chama esta função receberá um valor `Ok` que contém um `String`---o `username` que esta função leu do arquivo \[8]. Se esta função encontrar algum problema, o código chamador receberá um valor `Err` que contém uma instância de `io::Error` que contém mais informações sobre quais foram os problemas. Escolhemos `io::Error` como o tipo de retorno desta função porque esse é o tipo do valor de erro retornado de ambas as operações que estamos chamando no corpo desta função que podem falhar: a função `File::open` \[2] e o método `read_to_string` \[7].

O corpo da função começa chamando a função `File::open` \[2]. Em seguida, tratamos o valor `Result` com um `match` semelhante ao `match` no Listing 9-4. Se `File::open` for bem-sucedido, o manipulador do arquivo na variável de padrão `file` \[4] se torna o valor na variável mutável `username_file` \[3] e a função continua. No caso `Err`, em vez de chamar `panic!`, usamos a palavra-chave `return` para retornar antecipadamente da função inteiramente e passar o valor de erro de `File::open`, agora na variável de padrão `e`, de volta para o código chamador como o valor de erro desta função \[5].

Então, se tivermos um manipulador de arquivo em `username_file`, a função cria uma nova `String` na variável `username` \[6] e chama o método `read_to_string` no manipulador de arquivo em `username_file` para ler o conteúdo do arquivo em `username` \[7]. O método `read_to_string` também retorna um `Result` porque pode falhar, mesmo que `File::open` tenha sido bem-sucedido. Então, precisamos de outro `match` para lidar com esse `Result`: se `read_to_string` for bem-sucedido, então nossa função foi bem-sucedida e retornamos o nome de usuário do arquivo que agora está em `username` envolvido em um `Ok`. Se `read_to_string` falhar, retornamos o valor de erro da mesma forma que retornamos o valor de erro no `match` que tratou o valor de retorno de `File::open`. No entanto, não precisamos dizer explicitamente `return`, porque esta é a última expressão na função \[9].

O código que chama este código então lidará com a obtenção de um valor `Ok` que contém um nome de usuário ou um valor `Err` que contém um `io::Error`. Cabe ao código chamador decidir o que fazer com esses valores. Se o código chamador receber um valor `Err`, ele pode chamar `panic!` e travar o programa, usar um nome de usuário padrão ou procurar o nome de usuário de outro lugar que não um arquivo, por exemplo. Não temos informações suficientes sobre o que o código chamador está realmente tentando fazer, então propagamos todas as informações de sucesso ou erro para cima para que ele possa lidar adequadamente.

Este padrão de propagação de erros é tão comum em Rust que Rust fornece o operador de ponto de interrogação `?` para facilitar isso.
