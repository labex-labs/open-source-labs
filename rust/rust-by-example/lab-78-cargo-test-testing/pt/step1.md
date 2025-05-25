# Testes

Como sabemos, os testes são essenciais para qualquer software! Rust possui suporte de primeira classe para testes unitários e de integração ([consulte este capítulo](https://doc.rust-lang.org/book/ch11-00-testing.html) no TRPL).

A partir dos capítulos de testes vinculados acima, vemos como escrever testes unitários e testes de integração. Organizacionalmente, podemos colocar testes unitários nos módulos que testam e testes de integração em seu próprio diretório `tests/`:

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

Cada arquivo em `tests` é um teste de integração separado ([veja aqui](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)), ou seja, um teste que visa testar sua biblioteca como se estivesse sendo chamada de um crate dependente.

O capítulo de Testes detalha os três estilos de teste diferentes: Unitário, Documentação e Integração.

O `cargo` fornece naturalmente uma maneira fácil de executar todos os seus testes!

```shell
$ cargo test
```

Você deve ver uma saída como esta:

```shell
[objeto Objeto]
```

Você também pode executar testes cujos nomes correspondem a um padrão:

```shell
$ cargo test test_foo
```

```shell
[objeto Objeto]
```

Um aviso importante: o Cargo pode executar vários testes simultaneamente, portanto, certifique-se de que eles não entrem em conflito uns com os outros.

Um exemplo de como essa concorrência pode causar problemas é se dois testes escreverem em um arquivo, como abaixo:

```rust
#[cfg(test)]
mod tests {
    // Importar os módulos necessários
    use std::fs::OpenOptions;
    use std::io::Write;

    // Este teste escreve em um arquivo
    #[test]
    fn test_file() {
        // Abre o arquivo ferris.txt ou cria um se ele não existir.
        let mut file = OpenOptions::new()
            .append(true)
            .create(true)
            .open("ferris.txt")
            .expect("Falha ao abrir ferris.txt");

        // Imprime "Ferris" 5 vezes.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
                .expect("Não foi possível escrever em ferris.txt");
        }
    }

    // Este teste tenta escrever no mesmo arquivo
    #[test]
    fn test_file_also() {
        // Abre o arquivo ferris.txt ou cria um se ele não existir.
        let mut file = OpenOptions::new()
            .append(true)
            .create(true)
            .open("ferris.txt")
            .expect("Falha ao abrir ferris.txt");

        // Imprime "Corro" 5 vezes.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
                .expect("Não foi possível escrever em ferris.txt");
        }
    }
}
```

Embora a intenção seja obter o seguinte:

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

O que realmente é colocado em `ferris.txt` é isto:

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
