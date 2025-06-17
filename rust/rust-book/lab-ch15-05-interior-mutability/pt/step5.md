# Acompanhando Empréstimos em Tempo de Execução com RefCell`<T>`

Ao criar referências imutáveis e mutáveis, usamos a sintaxe `&` e `&mut`, respectivamente. Com `RefCell<T>`, usamos os métodos `borrow` e `borrow_mut`, que fazem parte da API segura que pertence a `RefCell<T>`. O método `borrow` retorna o tipo de ponteiro inteligente `Ref<T>`, e `borrow_mut` retorna o tipo de ponteiro inteligente `RefMut<T>`. Ambos os tipos implementam `Deref`, então podemos tratá-los como referências regulares.

O `RefCell<T>` acompanha quantos ponteiros inteligentes `Ref<T>` e `RefMut<T>` estão atualmente ativos. Toda vez que chamamos `borrow`, o `RefCell<T>` aumenta sua contagem de quantos empréstimos imutáveis estão ativos. Quando um valor `Ref<T>` sai do escopo, a contagem de empréstimos imutáveis diminui em 1. Assim como as regras de empréstimo em tempo de compilação, `RefCell<T>` nos permite ter muitos empréstimos imutáveis ou um empréstimo mutável em qualquer ponto no tempo.

Se tentarmos violar essas regras, em vez de obter um erro do compilador como faríamos com referências, a implementação de `RefCell<T>` entrará em pânico em tempo de execução. A Listagem 15-23 mostra uma modificação da implementação de `send` na Listagem 15-22. Estamos deliberadamente tentando criar dois empréstimos mutáveis ativos para o mesmo escopo para ilustrar que `RefCell<T>` nos impede de fazer isso em tempo de execução.

Nome do arquivo: `src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

Listagem 15-23: Criando duas referências mutáveis no mesmo escopo para ver que `RefCell<T>` entrará em pânico

Criamos uma variável `one_borrow` para o ponteiro inteligente `RefMut<T>` retornado de `borrow_mut`. Em seguida, criamos outro empréstimo mutável da mesma forma na variável `two_borrow`. Isso cria duas referências mutáveis no mesmo escopo, o que não é permitido. Quando executamos os testes para nossa biblioteca, o código na Listagem 15-23 compilará sem nenhum erro, mas o teste falhará:

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Observe que o código entrou em pânico com a mensagem `already borrowed: BorrowMutError`. É assim que `RefCell<T>` lida com violações das regras de empréstimo em tempo de execução.

Optar por detectar erros de empréstimo em tempo de execução em vez de tempo de compilação, como fizemos aqui, significa que você potencialmente estaria encontrando erros em seu código mais tarde no processo de desenvolvimento: possivelmente não até que seu código fosse implantado em produção. Além disso, seu código incorreria em uma pequena penalidade de desempenho em tempo de execução como resultado de acompanhar os empréstimos em tempo de execução em vez de tempo de compilação. No entanto, usar `RefCell<T>` torna possível escrever um objeto mock que pode se modificar para acompanhar as mensagens que viu enquanto você o está usando em um contexto onde apenas valores imutáveis são permitidos. Você pode usar `RefCell<T>` apesar de suas compensações para obter mais funcionalidade do que as referências regulares fornecem.
