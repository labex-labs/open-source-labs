# Verificando Resultados com a Macro `assert!`

A macro `assert!`, fornecida pela biblioteca padrão, é útil quando você deseja garantir que alguma condição em um teste seja avaliada como `true`. Damos à macro `assert!` um argumento que é avaliado como um booleano. Se o valor for `true`, nada acontece e o teste passa. Se o valor for `false`, a macro `assert!` chama `panic!` para fazer com que o teste falhe. Usar a macro `assert!` nos ajuda a verificar se nosso código está funcionando da maneira que pretendemos.

Na Listagem 5-15, usamos uma struct `Rectangle` e um método `can_hold`, que são repetidos aqui na Listagem 11-5. Vamos colocar este código no arquivo `src/lib.rs` e, em seguida, escrever alguns testes para ele usando a macro `assert!`.

Nome do arquivo: `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listagem 11-5: Usando a struct `Rectangle` e seu método `can_hold` do Capítulo 5

O método `can_hold` retorna um booleano, o que significa que é um caso de uso perfeito para a macro `assert!`. Na Listagem 11-6, escrevemos um teste que exercita o método `can_hold` criando uma instância `Rectangle` que tem uma largura de 8 e uma altura de 7 e afirmando que ela pode conter outra instância `Rectangle` que tem uma largura de 5 e uma altura de 1.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Listagem 11-6: Um teste para `can_hold` que verifica se um retângulo maior pode realmente conter um retângulo menor

Observe que adicionamos uma nova linha dentro do módulo `tests`: `use super::*;` \[1]. O módulo `tests` é um módulo regular que segue as regras de visibilidade usuais que abordamos em "Caminhos para se Referir a um Item na Árvore de Módulos". Como o módulo `tests` é um módulo interno, precisamos trazer o código sob teste no módulo externo para o escopo do módulo interno. Usamos um glob aqui, então tudo o que definimos no módulo externo está disponível para este módulo `tests`.

Nomeamos nosso teste `larger_can_hold_smaller` \[2] e criamos as duas instâncias `Rectangle` de que precisamos \[3]. Em seguida, chamamos a macro `assert!` e passamos a ela o resultado da chamada `larger.can_hold(&smaller)` \[4]. Espera-se que esta expressão retorne `true`, então nosso teste deve passar. Vamos descobrir!

    running 1 test
    test tests::larger_can_hold_smaller ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Ele passa! Vamos adicionar outro teste, desta vez afirmando que um retângulo menor não pode conter um retângulo maior:

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

Como o resultado correto da função `can_hold` neste caso é `false`, precisamos negar esse resultado antes de passá-lo para a macro `assert!`. Como resultado, nosso teste passará se `can_hold` retornar `false`:

    running 2 tests
    test tests::larger_can_hold_smaller ... ok
    test tests::smaller_cannot_hold_larger ... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Dois testes que passam! Agora vamos ver o que acontece com os resultados do nosso teste quando introduzimos um bug em nosso código. Vamos alterar a implementação do método `can_hold` substituindo o sinal de maior que por um sinal de menor que ao comparar as larguras:

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

A execução dos testes agora produz o seguinte:

    running 2 tests
    test tests::smaller_cannot_hold_larger ... ok
    test tests::larger_can_hold_smaller ... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread 'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Nossos testes detectaram o bug! Como `larger.width` é `8` e `smaller.width` é `5`, a comparação das larguras em `can_hold` agora retorna `false`: 8 não é menor que 5.
