# Métodos que Produzem Outros Iteradores

_Adaptadores de iterador_ são métodos definidos no _trait_ `Iterator` que não consomem o iterador. Em vez disso, eles produzem iteradores diferentes, alterando algum aspecto do iterador original.

A Listagem 13-14 mostra um exemplo de chamada do método adaptador de iterador `map`, que recebe um _closure_ (fechamento) para chamar em cada item à medida que os itens são iterados. O método `map` retorna um novo iterador que produz os itens modificados. O _closure_ aqui cria um novo iterador no qual cada item do vetor será incrementado em 1.

Nome do arquivo: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

Listagem 13-14: Chamando o adaptador de iterador `map` para criar um novo iterador

No entanto, este código produz um aviso:

    warning: unused `Map` that must be used
     --> src/main.rs:4:5
      |
    4 |     v1.iter().map(|x| x + 1);
      |     ^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = note: `#[warn(unused_must_use)]` on by default
      = note: iterators are lazy and do nothing unless consumed

O código na Listagem 13-14 não faz nada; o _closure_ que especificamos nunca é chamado. O aviso nos lembra o porquê: adaptadores de iterador são _lazy_ (preguiçosos), e precisamos consumir o iterador aqui.

Para corrigir este aviso e consumir o iterador, usaremos o método `collect`, que usamos com `env::args` na Listagem 12-1. Este método consome o iterador e coleta os valores resultantes em um tipo de dado de coleção.

Na Listagem 13-15, coletamos em um vetor os resultados da iteração sobre o iterador que é retornado da chamada para `map`. Este vetor acabará contendo cada item do vetor original, incrementado em 1.

Nome do arquivo: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

Listagem 13-15: Chamando o método `map` para criar um novo iterador e, em seguida, chamando o método `collect` para consumir o novo iterador e criar um vetor

Como `map` recebe um _closure_, podemos especificar qualquer operação que quisermos realizar em cada item. Este é um ótimo exemplo de como os _closures_ permitem que você personalize algum comportamento enquanto reutiliza o comportamento de iteração que o _trait_ `Iterator` fornece.

Você pode encadear várias chamadas para adaptadores de iterador para realizar ações complexas de forma legível. Mas, como todos os iteradores são _lazy_, você precisa chamar um dos métodos de adaptador consumidor para obter resultados das chamadas para adaptadores de iterador.
