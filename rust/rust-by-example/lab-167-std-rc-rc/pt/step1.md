# `Rc`

Quando é necessária a propriedade múltipla, `Rc` (Contagem de Referências) pode ser usado. `Rc` acompanha o número de referências, o que significa o número de proprietários do valor contido dentro de um `Rc`.

A contagem de referências de um `Rc` aumenta em 1 sempre que um `Rc` é clonado e diminui em 1 sempre que um `Rc` clonado é descartado fora do escopo. Quando a contagem de referências de um `Rc` se torna zero (o que significa que não há mais proprietários), tanto o `Rc` quanto o valor são descartados.

Clonar um `Rc` nunca executa uma cópia profunda. A clonagem cria apenas outro ponteiro para o valor encapsulado e incrementa a contagem.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Exemplos Rc".to_string();
    {
        println!("--- rc_a foi criado ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Contagem de Referências de rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a foi clonado para rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Contagem de Referências de rc_b: {}", Rc::strong_count(&rc_b));
            println!("Contagem de Referências de rc_a: {}", Rc::strong_count(&rc_a));

            // Dois `Rc`s são iguais se seus valores internos forem iguais
            println!("rc_a e rc_b são iguais: {}", rc_a.eq(&rc_b));

            // Podemos usar métodos de um valor diretamente
            println!("Comprimento do valor dentro de rc_a: {}", rc_a.len());
            println!("Valor de rc_b: {}", rc_b);

            println!("--- rc_b foi descartado fora do escopo ---");
        }

        println!("Contagem de Referências de rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a foi descartado fora do escopo ---");
    }

    // Erro! `rc_examples` já foi movido para `rc_a`
    // E quando `rc_a` é descartado, `rc_examples` é descartado junto
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Tente descomentar esta linha
}
```
