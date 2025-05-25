# `read_lines`

## Uma abordagem ingênua

Esta pode ser uma primeira tentativa razoável para uma primeira implementação de leitura de linhas de um arquivo por um iniciante.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

Como o método `lines()` retorna um iterador sobre as linhas do arquivo, também podemos realizar um mapeamento inline e coletar os resultados, gerando uma expressão mais concisa e fluente.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()  // trata erros potenciais de leitura de arquivo
        .lines()  // divide a string em um iterador de fatias de string
        .map(String::from)  // transforma cada fatia em uma string
        .collect()  // reúne-as em um vetor
}
```

Observe que, em ambos os exemplos acima, devemos converter a referência `&str` retornada por `lines()` para o tipo possuído `String`, usando `.to_string()` e `String::from`, respectivamente.

## Uma abordagem mais eficiente

Aqui, passamos a propriedade do `File` aberto para um objeto `BufReader`. `BufReader` utiliza um buffer interno para reduzir alocações intermediárias.

Também atualizamos `read_lines` para retornar um iterador em vez de alocar novos objetos `String` na memória para cada linha.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // O arquivo hosts.txt deve existir no diretório atual
    if let Ok(lines) = read_lines("./hosts.txt") {
        // Consome o iterador, retorna uma (opcional) String
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// A saída é envolvida em um Result para permitir correspondência de erros
// Retorna um iterador para o leitor das linhas do arquivo.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

A execução deste programa simplesmente imprime as linhas individualmente.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(Observe que, como `File::open` espera um argumento genérico `AsRef<Path>`, definimos nosso método genérico `read_lines()` com a mesma restrição genérica, usando a palavra-chave `where`.)

Este processo é mais eficiente do que criar um `String` na memória com todo o conteúdo do arquivo. Isso pode causar problemas de desempenho, especialmente ao trabalhar com arquivos maiores.
