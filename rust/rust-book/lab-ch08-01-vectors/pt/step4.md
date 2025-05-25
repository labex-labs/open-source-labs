# Lendo Elementos de Vetores

Existem duas maneiras de referenciar um valor armazenado em um vetor: por indexação ou usando o método `get`. Nos exemplos a seguir, anotamos os tipos dos valores que são retornados dessas funções para maior clareza.

A Listagem 8-4 mostra ambos os métodos de acesso a um valor em um vetor, com sintaxe de indexação e o método `get`.

```rust
let v = vec![1, 2, 3, 4, 5];

1 let third: &i32 = &v[2];
println!("The third element is {third}");

2 let third: Option<&i32> = v.get(2);
match third  {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

Listagem 8-4: Usando a sintaxe de indexação e o método `get` para acessar um item em um vetor

Observe alguns detalhes aqui. Usamos o valor do índice `2` para obter o terceiro elemento \[1] porque os vetores são indexados por número, começando em zero. Usar `&` e `[]` nos dá uma referência ao elemento no valor do índice. Quando usamos o método `get` com o índice passado como um argumento \[2], obtemos um `Option<&T>` que podemos usar com `match`.

O Rust fornece essas duas maneiras de referenciar um elemento para que você possa escolher como o programa se comporta quando tenta usar um valor de índice fora do intervalo de elementos existentes. Como exemplo, vamos ver o que acontece quando temos um vetor de cinco elementos e, em seguida, tentamos acessar um elemento no índice 100 com cada técnica, como mostrado na Listagem 8-5.

```rust
let v = vec![1, 2, 3, 4, 5];

let does_not_exist = &v[100];
let does_not_exist = v.get(100);
```

Listagem 8-5: Tentando acessar o elemento no índice 100 em um vetor contendo cinco elementos

Quando executamos este código, o primeiro método `[]` fará com que o programa entre em pânico porque referencia um elemento inexistente. Este método é melhor usado quando você deseja que seu programa trave se houver uma tentativa de acessar um elemento além do final do vetor.

Quando o método `get` recebe um índice que está fora do vetor, ele retorna `None` sem entrar em pânico. Você usaria este método se o acesso a um elemento além do intervalo do vetor pudesse acontecer ocasionalmente em circunstâncias normais. Seu código terá então lógica para lidar com `Some(&element)` ou `None`, como discutido no Capítulo 6. Por exemplo, o índice pode vir de uma pessoa digitando um número. Se eles digitarem acidentalmente um número muito grande e o programa receber um valor `None`, você poderá dizer ao usuário quantos itens estão no vetor atual e dar a eles outra chance de inserir um valor válido. Isso seria mais amigável do que travar o programa devido a um erro de digitação!

Quando o programa tem uma referência válida, o verificador de empréstimo (borrow checker) impõe as regras de propriedade e empréstimo (cobertas no Capítulo 4) para garantir que essa referência e quaisquer outras referências ao conteúdo do vetor permaneçam válidas. Lembre-se da regra que afirma que você não pode ter referências mutáveis e imutáveis no mesmo escopo. Essa regra se aplica na Listagem 8-6, onde mantemos uma referência imutável ao primeiro elemento em um vetor e tentamos adicionar um elemento ao final. Este programa não funcionará se também tentarmos nos referir a esse elemento mais tarde na função.

```rust
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);

println!("The first element is: {first}");
```

Listagem 8-6: Tentando adicionar um elemento a um vetor enquanto mantém uma referência a um item

A compilação deste código resultará neste erro:

```bash
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:5
  |
4 |     let first = &v[0];
  |                  - immutable borrow occurs here
5 |
6 |     v.push(6);
  |     ^^^^^^^^^ mutable borrow occurs here
7 |
8 |     println!("The first element is: {first}");
  |                                      ----- immutable borrow later used here
```

O código na Listagem 8-6 pode parecer que deveria funcionar: por que uma referência ao primeiro elemento se importaria com as alterações no final do vetor? Este erro se deve à forma como os vetores funcionam: como os vetores colocam os valores próximos uns dos outros na memória, adicionar um novo elemento ao final do vetor pode exigir a alocação de nova memória e a cópia dos elementos antigos para o novo espaço, se não houver espaço suficiente para colocar todos os elementos próximos uns dos outros onde o vetor está atualmente armazenado. Nesse caso, a referência ao primeiro elemento estaria apontando para a memória desalocada. As regras de empréstimo impedem que os programas acabem nessa situação.

> Nota: Para obter mais informações sobre os detalhes de implementação do tipo `Vec<T>`, consulte "The Rustonomicon" em *https://doc.rust-lang.org/nomicon/vec/vec.html*.
