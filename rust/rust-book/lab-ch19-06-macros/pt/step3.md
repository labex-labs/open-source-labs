# Macros Declarativas com `macro_rules!` para Metaprogramação Geral

A forma mais amplamente utilizada de macros em Rust é a _macro declarativa_. Estas também são, por vezes, referidas como "macros por exemplo", "macros `macro_rules!`" ou simplesmente "macros". No seu cerne, as macros declarativas permitem que você escreva algo semelhante a uma expressão `match` do Rust. Como discutido no Capítulo 6, as expressões `match` são estruturas de controle que recebem uma expressão, comparam o valor resultante da expressão com padrões e, em seguida, executam o código associado ao padrão correspondente. As macros também comparam um valor com padrões que estão associados a um código específico: nesta situação, o valor é o código-fonte literal do Rust passado para a macro; os padrões são comparados com a estrutura desse código-fonte; e o código associado a cada padrão, quando correspondido, substitui o código passado para a macro. Tudo isso acontece durante a compilação.

Para definir uma macro, você usa a construção `macro_rules!`. Vamos explorar como usar `macro_rules!` observando como a macro `vec!` é definida. O Capítulo 8 abordou como podemos usar a macro `vec!` para criar um novo vetor com valores específicos. Por exemplo, a seguinte macro cria um novo vetor contendo três inteiros:

```rust
let v: Vec<u32> = vec![1, 2, 3];
```

Também poderíamos usar a macro `vec!` para criar um vetor de dois inteiros ou um vetor de cinco fatias de string. Não seríamos capazes de usar uma função para fazer o mesmo porque não saberíamos o número ou o tipo de valores antecipadamente.

A Listagem 19-28 mostra uma definição ligeiramente simplificada da macro `vec!`.

Nome do arquivo: `src/lib.rs`

```rust
1 #[macro_export]
2 macro_rules! vec {
  3 ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
          4 $(
              5 temp_vec.push(6 $x);
            )*
          7 temp_vec
        }
    };
}
```

Listagem 19-28: Uma versão simplificada da definição da macro `vec!`

> Nota: A definição real da macro `vec!` na biblioteca padrão inclui código para pré-alocar a quantidade correta de memória antecipadamente. Esse código é uma otimização que não incluímos aqui, para simplificar o exemplo.

A anotação `#[macro_export]` \[1] indica que esta macro deve estar disponível sempre que o crate em que a macro é definida for trazido para o escopo. Sem esta anotação, a macro não pode ser trazida para o escopo.

Em seguida, iniciamos a definição da macro com `macro_rules!` e o nome da macro que estamos definindo _sem_ o ponto de exclamação \[2]. O nome, neste caso `vec`, é seguido por chaves que denotam o corpo da definição da macro.

A estrutura no corpo `vec!` é semelhante à estrutura de uma expressão `match`. Aqui temos um braço com o padrão `( $( $x:expr ),* )`, seguido por `=>` e o bloco de código associado a este padrão \[3]. Se o padrão corresponder, o bloco de código associado será emitido. Dado que este é o único padrão nesta macro, existe apenas uma forma válida de corresponder; qualquer outro padrão resultará em um erro. Macros mais complexas terão mais de um braço.

A sintaxe de padrão válida em definições de macro é diferente da sintaxe de padrão coberta no Capítulo 18 porque os padrões de macro são correspondidos com a estrutura do código Rust, em vez de valores. Vamos analisar o que as partes do padrão na Listagem 19-28 significam; para a sintaxe completa do padrão de macro, consulte a Referência do Rust em *https://doc.rust-lang.org/reference/macros-by-example.html*.

Primeiro, usamos um conjunto de parênteses para englobar todo o padrão. Usamos um cifrão (`$`) para declarar uma variável no sistema de macro que conterá o código Rust correspondente ao padrão. O cifrão deixa claro que esta é uma variável de macro, em oposição a uma variável Rust regular. Em seguida, vem um conjunto de parênteses que captura valores que correspondem ao padrão dentro dos parênteses para uso no código de substituição. Dentro de `$()` está `$x:expr`, que corresponde a qualquer expressão Rust e dá à expressão o nome `$x`.

A vírgula que segue `$()` indica que um caractere separador de vírgula literal pode opcionalmente aparecer após o código que corresponde ao código em `$()`. O `*` especifica que o padrão corresponde a zero ou mais de tudo o que precede o `*`.

Quando chamamos esta macro com `vec![1, 2, 3];`, o padrão `$x` corresponde três vezes com as três expressões `1`, `2` e `3`.

Agora, vamos analisar o padrão no corpo do código associado a este braço: `temp_vec.push()` \[5] dentro de `$()*` em \[4] e \[7] é gerado para cada parte que corresponde a `$()` no padrão zero ou mais vezes, dependendo de quantas vezes o padrão corresponde. O `$x` \[6] é substituído por cada expressão correspondida. Quando chamamos esta macro com `vec![1, 2, 3];`, o código gerado que substitui esta chamada de macro será o seguinte:

    {
        let mut temp_vec = Vec::new();
        temp_vec.push(1);
        temp_vec.push(2);
        temp_vec.push(3);
        temp_vec
    }

Definimos uma macro que pode receber qualquer número de argumentos de qualquer tipo e pode gerar código para criar um vetor contendo os elementos especificados.

Para saber mais sobre como escrever macros, consulte a documentação online ou outros recursos, como "The Little Book of Rust Macros" em *https://veykril.github.io/tlborm* iniciado por Daniel Keep e continuado por Lukas Wirth.
