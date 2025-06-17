# Permitindo Acesso de Múltiplas Threads com Sync

A trait marker `Sync` indica que é seguro para o tipo que implementa `Sync` ser referenciado de múltiplas threads. Em outras palavras, qualquer tipo `T` é `Sync` se `&T` (uma referência imutável para `T`) é `Send`, o que significa que a referência pode ser enviada com segurança para outra thread. Semelhante a `Send`, os tipos primitivos são `Sync`, e os tipos compostos inteiramente por tipos que são `Sync` também são `Sync`.

O smart pointer `Rc<T>` também não é `Sync` pelas mesmas razões que não é `Send`. O tipo `RefCell<T>` (sobre o qual falamos no Capítulo 15) e a família de tipos relacionados `Cell<T>` não são `Sync`. A implementação da verificação de empréstimo (borrow checking) que `RefCell<T>` faz em tempo de execução não é thread-safe. O smart pointer `Mutex<T>` é `Sync` e pode ser usado para compartilhar acesso com múltiplas threads, como você viu em "Compartilhando um Mutex`<T>` Entre Múltiplas Threads".
