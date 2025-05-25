# Propriedade (Ownership) e "Moves" (Movimentações)

Como as variáveis são responsáveis por liberar seus próprios recursos, **os recursos só podem ter um proprietário**. Isso também impede que os recursos sejam liberados mais de uma vez. Observe que nem todas as variáveis possuem recursos (por exemplo, \[referências]).

Ao fazer atribuições (`let x = y`) ou passar argumentos de função por valor (`foo(x)`), a _propriedade_ (ownership) dos recursos é transferida. Em termos de Rust, isso é conhecido como uma _move_ (movimentação).

Após a movimentação (move) dos recursos, o proprietário anterior não pode mais ser usado. Isso evita a criação de ponteiros pendentes (dangling pointers).

```rust
// Esta função assume a propriedade da memória alocada no heap
fn destroy_box(c: Box<i32>) {
    println!("Destruindo uma caixa que contém {}", c);

    // `c` é destruído e a memória liberada
}

fn main() {
    // Inteiro alocado na _pilha_ (stack)
    let x = 5u32;

    // *Copia* `x` para `y` - nenhum recurso é movido
    let y = x;

    // Ambos os valores podem ser usados independentemente
    println!("x é {}, e y é {}", x, y);

    // `a` é um ponteiro para um inteiro alocado no _heap_
    let a = Box::new(5i32);

    println!("a contém: {}", a);

    // *Move* `a` para `b`
    let b = a;
    // O endereço do ponteiro de `a` é copiado (não os dados) para `b`.
    // Ambos são agora ponteiros para os mesmos dados alocados no heap, mas
    // `b` agora é o proprietário.

    // Erro! `a` não pode mais acessar os dados, porque não é mais o proprietário da
    // memória do heap
    //println!("a contains: {}", a);
    // TODO ^ Tente descomentar esta linha

    // Esta função assume a propriedade da memória alocada no heap de `b`
    destroy_box(b);

    // Como a memória do heap foi liberada neste ponto, esta ação resultaria em
    // desreferenciar a memória liberada, mas é proibido pelo compilador
    // Erro! Mesma razão que o Erro anterior
    //println!("b contains: {}", b);
    // TODO ^ Tente descomentar esta linha
}
```
