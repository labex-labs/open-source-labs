# Um Caso de Uso para Mutabilidade Interior: Objetos Mock

Às vezes, durante os testes, um programador usará um tipo no lugar de outro tipo, a fim de observar um comportamento específico e afirmar que ele foi implementado corretamente. Esse tipo de espaço reservado é chamado de _test double_. Pense nisso no sentido de um dublê em cinematografia, onde uma pessoa entra e substitui um ator para fazer uma cena particularmente complicada. Os test doubles substituem outros tipos quando estamos executando testes. _Objetos mock_ são tipos específicos de test doubles que registram o que acontece durante um teste para que você possa afirmar que as ações corretas foram tomadas.

Rust não tem objetos no mesmo sentido que outras linguagens têm objetos, e Rust não tem funcionalidade de objeto mock integrada na biblioteca padrão como algumas outras linguagens têm. No entanto, você pode definitivamente criar uma struct que servirá aos mesmos propósitos que um objeto mock.

Aqui está o cenário que testaremos: criaremos uma biblioteca que rastreia um valor em relação a um valor máximo e envia mensagens com base em quão próximo do valor máximo o valor atual está. Essa biblioteca pode ser usada para controlar a cota de um usuário para o número de chamadas de API que ele pode fazer, por exemplo.

Nossa biblioteca fornecerá apenas a funcionalidade de rastrear quão próximo do máximo um valor está e quais mensagens devem ser em quais momentos. Espera-se que os aplicativos que usam nossa biblioteca forneçam o mecanismo para enviar as mensagens: o aplicativo pode colocar uma mensagem no aplicativo, enviar um e-mail, enviar uma mensagem de texto ou fazer outra coisa. A biblioteca não precisa saber esse detalhe. Tudo o que ela precisa é algo que implemente uma trait que forneceremos chamada `Messenger`. A Listagem 15-20 mostra o código da biblioteca.

Nome do arquivo: `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
                .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
                .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Listagem 15-20: Uma biblioteca para controlar quão próximo um valor está de um valor máximo e avisar quando o valor está em certos níveis

Uma parte importante deste código é que a trait `Messenger` tem um método chamado `send` que recebe uma referência imutável a `self` e o texto da mensagem \[1]. Essa trait é a interface que nosso objeto mock precisa implementar para que o mock possa ser usado da mesma forma que um objeto real. A outra parte importante é que queremos testar o comportamento do método `set_value` no `LimitTracker` \[2]. Podemos alterar o que passamos para o parâmetro `value`, mas `set_value` não retorna nada para que possamos fazer afirmações. Queremos ser capazes de dizer que, se criarmos um `LimitTracker` com algo que implementa a trait `Messenger` e um valor específico para `max`, quando passarmos números diferentes para `value`, o messenger é instruído a enviar as mensagens apropriadas.

Precisamos de um objeto mock que, em vez de enviar um e-mail ou mensagem de texto quando chamamos `send`, apenas acompanhe as mensagens que ele recebe para enviar. Podemos criar uma nova instância do objeto mock, criar um `LimitTracker` que usa o objeto mock, chamar o método `set_value` no `LimitTracker` e, em seguida, verificar se o objeto mock tem as mensagens que esperamos. A Listagem 15-21 mostra uma tentativa de implementar um objeto mock para fazer exatamente isso, mas o verificador de empréstimo não permitirá.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Listagem 15-21: Uma tentativa de implementar um `MockMessenger` que não é permitida pelo verificador de empréstimo

Este código de teste define uma struct `MockMessenger` \[1] que tem um campo `sent_messages` com um `Vec` de valores `String` \[2] para acompanhar as mensagens que ele recebe para enviar. Também definimos uma função associada `new` \[3] para tornar conveniente a criação de novos valores `MockMessenger` que começam com uma lista vazia de mensagens. Em seguida, implementamos a trait `Messenger` para `MockMessenger` \[4] para que possamos dar um `MockMessenger` a um `LimitTracker`. Na definição do método `send` \[5], pegamos a mensagem passada como um parâmetro e a armazenamos na lista `sent_messages` do `MockMessenger`.

No teste, estamos testando o que acontece quando o `LimitTracker` recebe a instrução de definir `value` para algo que é mais de 75 por cento do valor `max` \[6]. Primeiro, criamos um novo `MockMessenger`, que começará com uma lista vazia de mensagens. Em seguida, criamos um novo `LimitTracker` e damos a ele uma referência ao novo `MockMessenger` e um valor `max` de `100`. Chamamos o método `set_value` no `LimitTracker` com um valor de `80`, que é mais de 75 por cento de 100. Em seguida, afirmamos que a lista de mensagens que o `MockMessenger` está acompanhando agora deve ter uma mensagem nela.

No entanto, há um problema com este teste, como mostrado aqui:

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

Não podemos modificar o `MockMessenger` para acompanhar as mensagens porque o método `send` recebe uma referência imutável a `self`. Também não podemos aceitar a sugestão do texto do erro para usar `&mut self` em vez disso, porque então a assinatura de `send` não corresponderia à assinatura na definição da trait `Messenger` (sinta-se à vontade para tentar e ver qual mensagem de erro você recebe).

Esta é uma situação em que a mutabilidade interior pode ajudar! Armazenaremos as `sent_messages` dentro de um `RefCell<T>`, e então o método `send` poderá modificar `sent_messages` para armazenar as mensagens que vimos. A Listagem 15-22 mostra como isso se parece.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3 .borrow_mut()
                .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Listagem 15-22: Usando `RefCell<T>` para mutar um valor interno enquanto o valor externo é considerado imutável

O campo `sent_messages` agora é do tipo `RefCell<Vec<String>>` \[1] em vez de `Vec<String>`. Na função `new`, criamos uma nova instância `RefCell<Vec<String>>` em torno do vetor vazio \[2].

Para a implementação do método `send`, o primeiro parâmetro ainda é um empréstimo imutável de `self`, que corresponde à definição da trait. Chamamos `borrow_mut` no `RefCell<Vec<String>>` em `self.sent_messages` \[3] para obter uma referência mutável ao valor dentro do `RefCell<Vec<String>>`, que é o vetor. Então, podemos chamar `push` na referência mutável ao vetor para acompanhar as mensagens enviadas durante o teste.

A última alteração que temos que fazer é na afirmação: para ver quantos itens estão no vetor interno, chamamos `borrow` no `RefCell<Vec<String>>` para obter uma referência imutável ao vetor \[4].

Agora que você viu como usar `RefCell<T>`, vamos nos aprofundar em como ele funciona!
