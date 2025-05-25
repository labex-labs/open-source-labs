# Permitindo a Transferência de Propriedade entre Threads com Send

A trait marker `Send` indica que a propriedade de valores do tipo que implementa `Send` pode ser transferida entre threads. Quase todos os tipos Rust são `Send`, mas existem algumas exceções, incluindo `Rc<T>`: este não pode ser `Send` porque se você clonasse um valor `Rc<T>` e tentasse transferir a propriedade do clone para outra thread, ambas as threads poderiam atualizar a contagem de referência ao mesmo tempo. Por esta razão, `Rc<T>` é implementado para uso em situações de thread único, onde você não deseja pagar a penalidade de desempenho thread-safe.

Portanto, o sistema de tipos e as restrições de traits do Rust garantem que você nunca possa enviar acidentalmente um valor `Rc<T>` entre threads de forma insegura. Quando tentamos fazer isso na Listagem 16-14, recebemos o erro `the trait`Send`is not implemented for`Rc\<Mutex`<i32>`{=html}\>\``. Quando mudamos para `Arc`<T>`{=html}`, que é `Send`, o código compilou.

Qualquer tipo composto inteiramente por tipos `Send` é automaticamente marcado como `Send` também. Quase todos os tipos primitivos são `Send`, exceto os ponteiros brutos (raw pointers), que discutiremos no Capítulo 19.
