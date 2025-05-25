# Valores de Retorno e Escopo

Retornar valores também pode transferir _ownership_. A Listagem 4-4 mostra um exemplo de uma função que retorna algum valor, com anotações semelhantes às da Listagem 4-3.

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership move seu retorno
                                            // valor para s1

        let s2 = String::from("hello");     // s2 entra em escopo

        let s3 = takes_and_gives_back(s2);  // s2 é movido para
                                            // takes_and_gives_back, que também
                                            // move seu valor de retorno para s3
    } // Aqui, s3 sai do escopo e é descartado. s2 foi movido, então nada
      // acontece. s1 sai do escopo e é descartado

    fn gives_ownership() -> String {             // gives_ownership moverá seu
                                                 // valor de retorno para a função
                                                 // que a chama

        let some_string = String::from("yours"); // some_string entra em escopo

        some_string                              // some_string é retornado e
                                                 // se move para fora para a
                                                 // função chamadora
    }

    // Esta função recebe uma String e retorna uma String
    fn takes_and_gives_back(a_string: String) -> String { // a_string entra em
                                                          // escopo

        a_string  // a_string é retornado e se move para fora para a função chamadora
    }

Listagem 4-4: Transferindo _ownership_ de valores de retorno

O _ownership_ de uma variável segue o mesmo padrão sempre: atribuir um valor a outra variável o move. Quando uma variável que inclui dados na _heap_ sai do escopo, o valor será limpo por `drop`, a menos que o _ownership_ dos dados tenha sido movido para outra variável.

Embora isso funcione, assumir o _ownership_ e, em seguida, retornar o _ownership_ com cada função é um pouco tedioso. E se quisermos permitir que uma função use um valor, mas não assuma o _ownership_? É bastante irritante que tudo o que passamos também precise ser passado de volta se quisermos usá-lo novamente, além de quaisquer dados resultantes do corpo da função que também possamos querer retornar.

Rust nos permite retornar múltiplos valores usando uma tupla, como mostrado na Listagem 4-5.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() retorna o comprimento de uma String

    (s, length)
}
```

Listagem 4-5: Retornando o _ownership_ de parâmetros

Mas isso é muita cerimônia e muito trabalho para um conceito que deveria ser comum. Felizmente para nós, Rust tem um recurso para usar um valor sem transferir o _ownership_, chamado _referências_.
