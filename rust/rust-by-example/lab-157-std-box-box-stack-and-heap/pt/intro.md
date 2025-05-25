# Introdução

Neste laboratório, o conceito de _boxing_, alocação na _stack_ (pilha) e alocação na _heap_ (heap) em Rust é explorado. Todos os valores em Rust são alocados na _stack_ por padrão, mas podem ser _boxed_ (alocados na _heap_) usando o tipo `Box<T>`. Um _box_ é um _smart pointer_ (ponteiro inteligente) para um valor alocado na _heap_, e quando ele sai do escopo, seu destrutor é chamado e a memória na _heap_ é liberada. O _boxing_ permite a criação de dupla indireção e pode ser desreferenciado usando o operador `*`. O laboratório fornece exemplos de código e explicações de como o _boxing_ funciona e como ele afeta a alocação de memória na _stack_.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
