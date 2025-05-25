# Removendo Duplicação por Extração de uma Função

Genéricos (Generics) nos permitem substituir tipos específicos por um espaço reservado que representa múltiplos tipos para remover a duplicação de código. Antes de mergulharmos na sintaxe de genéricos, vamos primeiro analisar como remover a duplicação de uma forma que não envolva tipos genéricos, extraindo uma função que substitui valores específicos por um espaço reservado que representa múltiplos valores. Em seguida, aplicaremos a mesma técnica para extrair uma função genérica! Ao analisar como reconhecer código duplicado que você pode extrair em uma função, você começará a reconhecer código duplicado que pode usar genéricos.

Começaremos com o pequeno programa na Listagem 10-1 que encontra o maior número em uma lista.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listagem 10-1: Encontrando o maior número em uma lista de números

Armazenamos uma lista de inteiros na variável `number_list` \[1] e colocamos uma referência ao primeiro número da lista em uma variável chamada `largest` \[2]. Em seguida, iteramos por todos os números da lista \[3], e se o número atual for maior que o número armazenado em `largest` \[4], substituímos a referência nessa variável \[5]. No entanto, se o número atual for menor ou igual ao maior número visto até agora, a variável não muda, e o código passa para o próximo número da lista. Depois de considerar todos os números da lista, `largest` deve se referir ao maior número, que neste caso é 100.

Agora fomos encarregados de encontrar o maior número em duas listas diferentes de números. Para fazer isso, podemos optar por duplicar o código na Listagem 10-1 e usar a mesma lógica em dois lugares diferentes no programa, conforme mostrado na Listagem 10-2.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listagem 10-2: Código para encontrar o maior número em _duas_ listas de números

Embora este código funcione, duplicar código é tedioso e propenso a erros. Também precisamos lembrar de atualizar o código em vários lugares quando quisermos alterá-lo.

Para eliminar essa duplicação, criaremos uma abstração definindo uma função que opera em qualquer lista de inteiros passada em um parâmetro. Essa solução torna nosso código mais claro e nos permite expressar o conceito de encontrar o maior número em uma lista de forma abstrata.

Na Listagem 10-3, extraímos o código que encontra o maior número em uma função chamada `largest`. Em seguida, chamamos a função para encontrar o maior número nas duas listas da Listagem 10-2. Também poderíamos usar a função em qualquer outra lista de valores `i32` que possamos ter no futuro.

Nome do arquivo: `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

Listagem 10-3: Código abstrato para encontrar o maior número em duas listas

A função `largest` tem um parâmetro chamado `list`, que representa qualquer fatia concreta de valores `i32` que possamos passar para a função. Como resultado, quando chamamos a função, o código é executado nos valores específicos que passamos.

Em resumo, aqui estão as etapas que tomamos para alterar o código da Listagem 10-2 para a Listagem 10-3:

1.  Identificar código duplicado.
2.  Extrair o código duplicado para o corpo da função e especificar as entradas e os valores de retorno desse código na assinatura da função.
3.  Atualizar as duas instâncias de código duplicado para chamar a função em vez disso.

Em seguida, usaremos as mesmas etapas com genéricos para reduzir a duplicação de código. Da mesma forma que o corpo da função pode operar em uma `list` abstrata em vez de valores específicos, os genéricos permitem que o código opere em tipos abstratos.

Por exemplo, digamos que tivéssemos duas funções: uma que encontra o maior item em uma fatia de valores `i32` e outra que encontra o maior item em uma fatia de valores `char`. Como eliminaríamos essa duplicação? Vamos descobrir!
