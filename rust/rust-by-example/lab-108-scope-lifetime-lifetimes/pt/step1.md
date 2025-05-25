# Lifetimes

Um _lifetime_ é uma construção do compilador (ou mais especificamente, seu _verificador de empréstimos_) usada para garantir que todos os empréstimos sejam válidos. Especificamente, o lifetime de uma variável começa quando ela é criada e termina quando ela é destruída. Embora lifetimes e escopos sejam frequentemente referenciados juntos, eles não são a mesma coisa.

Considere, por exemplo, o caso em que emprestamos uma variável via `&`. O empréstimo tem um lifetime determinado por onde ele é declarado. Como resultado, o empréstimo é válido enquanto durar antes da destruição do emprestador. No entanto, o escopo do empréstimo é determinado por onde a referência é usada.

Nos exemplos a seguir e no restante desta seção, veremos como lifetimes se relacionam com escopos, bem como como os dois diferem.

```rust
// Lifetimes são anotados abaixo com linhas que denotam a criação
// e destruição de cada variável.
// `i` tem o lifetime mais longo porque seu escopo envolve completamente
// tanto `borrow1` quanto `borrow2`. A duração de `borrow1` em comparação
// com `borrow2` é irrelevante, pois são disjuntos.
fn main() {
    let i = 3; // Lifetime para `i` começa. ────────────────┐
    //                                                     │
    { //                                                   │
        let borrow1 = &i; // `borrow1` lifetime começa. ──┐│
        //                                                ││
        println!("borrow1: {}", borrow1); //              ││
    } // `borrow1` termina. ─────────────────────────────────┘│
    //                                                     │
    //                                                     │
    { //                                                   │
        let borrow2 = &i; // `borrow2` lifetime começa. ──┐│
        //                                                ││
        println!("borrow2: {}", borrow2); //              ││
    } // `borrow2` termina. ─────────────────────────────────┘│
    //                                                     │
}   // Lifetime termina. ─────────────────────────────────────┘
```

Note que nenhum nome ou tipo é atribuído para rotular lifetimes. Isso restringe como os lifetimes serão capazes de ser usados, como veremos.
