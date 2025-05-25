# Correspondência com Diferentes Erros

O código no Listing 9-4 fará `panic!` independentemente do motivo pelo qual `File::open` falhou. No entanto, queremos tomar ações diferentes por diferentes razões de falha. Se `File::open` falhou porque o arquivo não existe, queremos criar o arquivo e retornar o manipulador para o novo arquivo. Se `File::open` falhou por qualquer outro motivo - por exemplo, porque não tínhamos permissão para abrir o arquivo - ainda queremos que o código faça `panic!` da mesma forma que fez no Listing 9-4. Para isso, adicionamos uma expressão `match` interna, mostrada no Listing 9-5.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

Listing 9-5: Lidando com diferentes tipos de erros de diferentes maneiras

O tipo do valor que `File::open` retorna dentro da variante `Err` é `io::Error`, que é uma struct fornecida pela biblioteca padrão. Esta struct tem um método `kind` que podemos chamar para obter um valor `io::ErrorKind`. O enum `io::ErrorKind` é fornecido pela biblioteca padrão e tem variantes que representam os diferentes tipos de erros que podem resultar de uma operação `io`. A variante que queremos usar é `ErrorKind::NotFound`, que indica que o arquivo que estamos tentando abrir ainda não existe. Então, fazemos match em `greeting_file_result`, mas também temos um match interno em `error.kind()`.

A condição que queremos verificar no match interno é se o valor retornado por `error.kind()` é a variante `NotFound` do enum `ErrorKind`. Se for, tentamos criar o arquivo com `File::create`. No entanto, como `File::create` também pode falhar, precisamos de um segundo braço na expressão `match` interna. Quando o arquivo não pode ser criado, uma mensagem de erro diferente é impressa. O segundo braço do `match` externo permanece o mesmo, então o programa entra em pânico em qualquer erro além do erro de arquivo ausente.
