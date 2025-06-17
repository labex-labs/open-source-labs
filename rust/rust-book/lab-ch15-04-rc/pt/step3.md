# Clonar um Rc`<T>` Aumenta a Contagem de Referências

Vamos alterar nosso exemplo de trabalho no Listing 15-18 para que possamos ver as contagens de referência mudando à medida que criamos e descartamos referências ao `Rc<List>` em `a`.

No Listing 15-19, mudaremos `main` para que ele tenha um escopo interno em torno da lista `c`; então podemos ver como a contagem de referência muda quando `c` sai do escopo.

Nome do arquivo: `src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

Listing 15-19: Imprimindo a contagem de referência

Em cada ponto do programa onde a contagem de referência muda, imprimimos a contagem de referência, que obtemos chamando a função `Rc::strong_count`. Esta função é nomeada `strong_count` em vez de `count` porque o tipo `Rc<T>` também tem um `weak_count`; veremos para que `weak_count` é usado em "Prevenindo Ciclos de Referência Usando Weak`<T>`".

Este código imprime o seguinte:

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

Podemos ver que o `Rc<List>` em `a` tem uma contagem de referência inicial de 1; então, cada vez que chamamos `clone`, a contagem aumenta em 1. Quando `c` sai do escopo, a contagem diminui em 1. Não precisamos chamar uma função para diminuir a contagem de referência como precisamos chamar `Rc::clone` para aumentar a contagem de referência: a implementação do trait `Drop` diminui a contagem de referência automaticamente quando um valor `Rc<T>` sai do escopo.

O que não podemos ver neste exemplo é que quando `b` e então `a` saem do escopo no final de `main`, a contagem é então 0, e o `Rc<List>` é limpo completamente. Usar `Rc<T>` permite que um único valor tenha múltiplos proprietários, e a contagem garante que o valor permaneça válido enquanto qualquer um dos proprietários ainda existir.

Por meio de referências imutáveis, `Rc<T>` permite que você compartilhe dados entre várias partes do seu programa apenas para leitura. Se `Rc<T>` permitisse que você também tivesse múltiplas referências mutáveis, você poderia violar uma das regras de empréstimo discutidas no Capítulo 4: múltiplos empréstimos mutáveis para o mesmo local podem causar condições de corrida de dados e inconsistências. Mas ser capaz de mutar dados é muito útil! Na próxima seção, discutiremos o padrão de mutabilidade interna e o tipo `RefCell<T>` que você pode usar em conjunto com um `Rc<T>` para trabalhar com essa restrição de imutabilidade.
