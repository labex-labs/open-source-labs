# Um Atalho para Propagar Erros: O Operador `?`

O Listing 9-7 mostra uma implementação de `read_username_from_file` que tem a mesma funcionalidade que no Listing 9-6, mas esta implementação usa o operador `?`.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Listing 9-7: Uma função que retorna erros para o código chamador usando o operador `?`

O `?` colocado após um valor `Result` é definido para funcionar quase da mesma forma que as expressões `match` que definimos para lidar com os valores `Result` no Listing 9-6. Se o valor do `Result` for um `Ok`, o valor dentro do `Ok` será retornado desta expressão, e o programa continuará. Se o valor for um `Err`, o `Err` será retornado de toda a função como se tivéssemos usado a palavra-chave `return`, para que o valor do erro seja propagado para o código chamador.

Há uma diferença entre o que a expressão `match` do Listing 9-6 faz e o que o operador `?` faz: os valores de erro que têm o operador `?` chamado neles passam pela função `from`, definida no trait `From` na biblioteca padrão, que é usada para converter valores de um tipo em outro. Quando o operador `?` chama a função `from`, o tipo de erro recebido é convertido no tipo de erro definido no tipo de retorno da função atual. Isso é útil quando uma função retorna um tipo de erro para representar todas as maneiras pelas quais uma função pode falhar, mesmo que as partes possam falhar por muitos motivos diferentes.

Por exemplo, poderíamos alterar a função `read_username_from_file` no Listing 9-7 para retornar um tipo de erro personalizado chamado `OurError` que definimos. Se também definirmos `impl From<io::Error> for OurError` para construir uma instância de `OurError` a partir de um `io::Error`, então as chamadas do operador `?` no corpo de `read_username_from_file` chamarão `from` e converterão os tipos de erro sem precisar adicionar mais nenhum código à função.

No contexto do Listing 9-7, o `?` no final da chamada `File::open` retornará o valor dentro de um `Ok` para a variável `username_file`. Se ocorrer um erro, o operador `?` retornará antecipadamente de toda a função e dará qualquer valor `Err` ao código chamador. A mesma coisa se aplica ao `?` no final da chamada `read_to_string`.

O operador `?` elimina muita repetição e torna a implementação desta função mais simples. Poderíamos até encurtar este código ainda mais encadeando chamadas de método imediatamente após o `?`, como mostrado no Listing 9-8.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Listing 9-8: Encadeando chamadas de método após o operador `?`

Movemos a criação do novo `String` em `username` para o início da função; essa parte não mudou. Em vez de criar uma variável `username_file`, encadeamos a chamada para `read_to_string` diretamente no resultado de `File::open("hello.txt")?`. Ainda temos um `?` no final da chamada `read_to_string`, e ainda retornamos um valor `Ok` contendo `username` quando tanto `File::open` quanto `read_to_string` são bem-sucedidos, em vez de retornar erros. A funcionalidade é novamente a mesma do Listing 9-6 e do Listing 9-7; esta é apenas uma maneira diferente e mais ergonômica de escrevê-la.

O Listing 9-9 mostra uma maneira de tornar isso ainda mais curto usando `fs::read_to_string`.

Nome do arquivo: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Listing 9-9: Usando `fs::read_to_string` em vez de abrir e, em seguida, ler o arquivo

Ler um arquivo em uma string é uma operação bastante comum, então a biblioteca padrão fornece a função conveniente `fs::read_to_string` que abre o arquivo, cria um novo `String`, lê o conteúdo do arquivo, coloca o conteúdo nessa `String` e o retorna. Claro, usar `fs::read_to_string` não nos dá a oportunidade de explicar todo o tratamento de erros, então o fizemos da maneira mais longa primeiro.
