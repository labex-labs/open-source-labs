# HashSet

Considere um `HashSet` como um `HashMap` onde nos importamos apenas com as chaves (um `HashSet<T>` é, na realidade, apenas um invólucro em torno de `HashMap<T, ()>`).

"Qual o objetivo disso?", você pergunta. "Eu poderia simplesmente armazenar as chaves em um `Vec`."

A característica única de um `HashSet` é que ele garante que não tenha elementos duplicados. Esse é o contrato que qualquer coleção de conjuntos cumpre. `HashSet` é apenas uma implementação. (veja também: `BTreeSet`)

Se você inserir um valor que já está presente no `HashSet` (ou seja, o novo valor é igual ao existente e ambos têm o mesmo hash), o novo valor substituirá o antigo.

Isso é ótimo quando você nunca quer mais de um de algo, ou quando quer saber se já tem algo.

Mas os conjuntos podem fazer mais do que isso.

Os conjuntos têm 4 operações principais (todas as chamadas a seguir retornam um iterador):

- `union`: obter todos os elementos únicos em ambos os conjuntos.

- `difference`: obter todos os elementos que estão no primeiro conjunto, mas não no segundo.

- `intersection`: obter todos os elementos que estão apenas em _ambos_ os conjuntos.

- `symmetric_difference`: obter todos os elementos que estão em um conjunto ou no outro, mas _não_ em ambos.

Experimente todas essas operações no exemplo a seguir:

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` retorna false se
    // já houver um valor presente.
    assert!(b.insert(4), "O valor 4 já está no conjunto B!");
    // FIXME ^ Comente esta linha

    b.insert(5);

    // Se o tipo de elemento de uma coleção implementar `Debug`,
    // então a coleção implementa `Debug`.
    // Normalmente, imprime seus elementos no formato `[elem1, elem2, ...]`
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // Imprime [1, 2, 3, 4, 5] em uma ordem arbitrária
    println!("União: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // Isso deve imprimir [1]
    println!("Diferença: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // Imprime [2, 3, 4] em uma ordem arbitrária.
    println!("Interseção: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // Imprime [1, 5]
    println!("Diferença Simétrica: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(Os exemplos foram adaptados da documentação.)
