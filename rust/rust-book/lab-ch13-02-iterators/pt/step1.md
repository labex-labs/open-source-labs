# Processamento de uma Série de Itens com Iteradores

O padrão de iterador permite que você execute alguma tarefa em uma sequência de itens por vez. Um iterador é responsável pela lógica de iterar sobre cada item e determinar quando a sequência foi finalizada. Quando você usa iteradores, não precisa reimplementar essa lógica por conta própria.

Em Rust, os iteradores são _lazy_ (preguiçosos), o que significa que não têm efeito até que você chame métodos que consomem o iterador para usá-lo. Por exemplo, o código na Listagem 13-10 cria um iterador sobre os itens no vetor `v1` chamando o método `iter` definido em `Vec<T>`. Este código por si só não faz nada útil.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();
```

Listagem 13-10: Criando um iterador

O iterador é armazenado na variável `v1_iter`. Depois de criarmos um iterador, podemos usá-lo de várias maneiras. Na Listagem 3-5, iteramos sobre um array usando um loop `for` para executar algum código em cada um de seus itens. Por baixo dos panos, isso implicitamente criou e depois consumiu um iterador, mas ignoramos como exatamente isso funciona até agora.

No exemplo na Listagem 13-11, separamos a criação do iterador do uso do iterador no loop `for`. Quando o loop `for` é chamado usando o iterador em `v1_iter`, cada elemento no iterador é usado em uma iteração do loop, que imprime cada valor.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();

for val in v1_iter {
    println!("Got: {val}");
}
```

Listagem 13-11: Usando um iterador em um loop `for`

Em linguagens que não possuem iteradores fornecidos por suas bibliotecas padrão, você provavelmente escreveria essa mesma funcionalidade começando uma variável no índice 0, usando essa variável para indexar no vetor para obter um valor e incrementando o valor da variável em um loop até atingir o número total de itens no vetor.

Os iteradores lidam com toda essa lógica para você, reduzindo o código repetitivo que você poderia potencialmente bagunçar. Os iteradores oferecem mais flexibilidade para usar a mesma lógica com muitos tipos diferentes de sequências, não apenas estruturas de dados que você pode indexar, como vetores. Vamos examinar como os iteradores fazem isso.
