# Variáveis e Dados Interagindo com _Move_

Múltiplas variáveis podem interagir com os mesmos dados de diferentes maneiras em Rust. Vamos analisar um exemplo usando um inteiro na Listagem 4-2.

```rust
let x = 5;
let y = x;
```

Listagem 4-2: Atribuindo o valor inteiro da variável `x` a `y`

Podemos provavelmente adivinhar o que isso está fazendo: "vincular o valor `5` a `x`; então, fazer uma cópia do valor em `x` e vinculá-lo a `y`." Agora temos duas variáveis, `x` e `y`, e ambas são iguais a `5`. É isso mesmo que está acontecendo, porque os inteiros são valores simples com um tamanho conhecido e fixo, e esses dois valores `5` são empurrados para a _stack_.

Agora, vamos analisar a versão `String`:

```rust
let s1 = String::from("hello");
let s2 = s1;
```

Isso parece muito semelhante, então podemos presumir que a maneira como funciona seria a mesma: ou seja, a segunda linha faria uma cópia do valor em `s1` e o vincularia a `s2`. Mas não é bem isso que acontece.

Dê uma olhada na Figura 4-1 para ver o que está acontecendo com `String` por dentro. Uma `String` é composta por três partes, mostradas à esquerda: um ponteiro para a memória que contém o conteúdo da _string_, um comprimento e uma capacidade. Este grupo de dados é armazenado na _stack_. À direita está a memória na _heap_ que contém o conteúdo.

Figura 4-1: Representação na memória de um `String` contendo o valor `"hello"` vinculado a `s1`

O comprimento é quanta memória, em bytes, o conteúdo do `String` está usando atualmente. A capacidade é a quantidade total de memória, em bytes, que o `String` recebeu do alocador. A diferença entre comprimento e capacidade é importante, mas não neste contexto, então, por enquanto, tudo bem ignorar a capacidade.

Quando atribuímos `s1` a `s2`, os dados `String` são copiados, o que significa que copiamos o ponteiro, o comprimento e a capacidade que estão na _stack_. Não copiamos os dados na _heap_ aos quais o ponteiro se refere. Em outras palavras, a representação dos dados na memória se parece com a Figura 4-2.

Figura 4-2: Representação na memória da variável `s2` que possui uma cópia do ponteiro, comprimento e capacidade de `s1`

A representação _não_ se parece com a Figura 4-3, que é como a memória se pareceria se o Rust também copiasse os dados da _heap_. Se o Rust fizesse isso, a operação `s2 = s1` poderia ser muito cara em termos de desempenho em tempo de execução se os dados na _heap_ fossem grandes.

Figura 4-3: Outra possibilidade para o que `s2 = s1` poderia fazer se o Rust também copiasse os dados da _heap_

Anteriormente, dissemos que, quando uma variável sai do escopo, o Rust chama automaticamente a função `drop` e limpa a memória da _heap_ para essa variável. Mas a Figura 4-2 mostra ambos os ponteiros de dados apontando para o mesmo local. Isso é um problema: quando `s2` e `s1` saírem do escopo, ambos tentarão liberar a mesma memória. Isso é conhecido como um erro de _dupla liberação_ e é um dos _bugs_ de segurança de memória que mencionamos anteriormente. Liberar a memória duas vezes pode levar à corrupção da memória, o que pode potencialmente levar a vulnerabilidades de segurança.

Para garantir a segurança da memória, após a linha `let s2 = s1;`, o Rust considera `s1` como não mais válido. Portanto, o Rust não precisa liberar nada quando `s1` sai do escopo. Verifique o que acontece quando você tenta usar `s1` depois que `s2` é criado; não funcionará:

```rust
let s1 = String::from("hello");
let s2 = s1;

println!("{s1}, world!");
```

Você receberá um erro como este porque o Rust impede que você use a referência invalidada:

```bash
error[E0382]: borrow of moved value: `s1`
 --> src/main.rs:5:28
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which
 does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |
5 |     println!("{s1}, world!");
  |                ^^ value borrowed here after move
```

Se você ouviu os termos _cópia rasa_ e _cópia profunda_ ao trabalhar com outras linguagens, o conceito de copiar o ponteiro, o comprimento e a capacidade sem copiar os dados provavelmente soa como fazer uma cópia rasa. Mas, como o Rust também invalida a primeira variável, em vez de ser chamada de cópia rasa, ela é conhecida como um _move_ (movimentação). Neste exemplo, diríamos que `s1` foi _movido_ para `s2`. Então, o que realmente acontece é mostrado na Figura 4-4.

Figura 4-4: Representação na memória após `s1` ter sido invalidado

Isso resolve nosso problema! Com apenas `s2` válido, quando ele sai do escopo, ele sozinho liberará a memória, e terminamos.

Além disso, há uma escolha de design que está implícita nisso: o Rust nunca criará automaticamente cópias "profundas" de seus dados. Portanto, qualquer cópia _automática_ pode ser considerada barata em termos de desempenho em tempo de execução.
