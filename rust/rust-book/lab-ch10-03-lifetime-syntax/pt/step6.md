# Anotações de _Lifetime_ em Assinaturas de Funções

Para usar anotações de _lifetime_ em assinaturas de funções, precisamos declarar os parâmetros genéricos de _lifetime_ dentro de colchetes angulares entre o nome da função e a lista de parâmetros, assim como fizemos com os parâmetros genéricos de _tipo_.

Queremos que a assinatura expresse a seguinte restrição: a referência retornada será válida enquanto ambos os parâmetros forem válidos. Esta é a relação entre os _lifetimes_ dos parâmetros e o valor de retorno. Vamos nomear o _lifetime_ `'a` e, em seguida, adicioná-lo a cada referência, como mostrado na Listagem 10-21.

Nome do arquivo: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listagem 10-21: A definição da função `longest` especificando que todas as referências na assinatura devem ter o mesmo _lifetime_ `'a`

Este código deve compilar e produzir o resultado desejado quando o usarmos com a função `main` na Listagem 10-19.

A assinatura da função agora diz ao Rust que, para algum _lifetime_ `'a`, a função recebe dois parâmetros, ambos _string slices_ que vivem pelo menos tanto tempo quanto o _lifetime_ `'a`. A assinatura da função também diz ao Rust que o _string slice_ retornado da função viverá pelo menos tanto tempo quanto o _lifetime_ `'a`. Na prática, isso significa que o _lifetime_ da referência retornada pela função `longest` é o mesmo que o menor dos _lifetimes_ dos valores referenciados pelos argumentos da função. Essas relações são o que queremos que o Rust use ao analisar este código.

Lembre-se, quando especificamos os parâmetros de _lifetime_ nesta assinatura de função, não estamos alterando os _lifetimes_ de nenhum valor passado ou retornado. Em vez disso, estamos especificando que o _borrow checker_ deve rejeitar quaisquer valores que não aderirem a essas restrições. Observe que a função `longest` não precisa saber exatamente quanto tempo `x` e `y` viverão, apenas que algum escopo pode ser substituído por `'a` que satisfaça esta assinatura.

Ao anotar _lifetimes_ em funções, as anotações vão na assinatura da função, não no corpo da função. As anotações de _lifetime_ se tornam parte do contrato da função, assim como os tipos na assinatura. Ter assinaturas de função contendo o contrato de _lifetime_ significa que a análise que o compilador Rust faz pode ser mais simples. Se houver um problema com a forma como uma função é anotada ou com a forma como ela é chamada, os erros do compilador podem apontar para a parte do nosso código e as restrições com mais precisão. Se, em vez disso, o compilador Rust fizesse mais inferências sobre o que pretendíamos que fossem as relações dos _lifetimes_, o compilador só poderia apontar para um uso do nosso código muitos passos distante da causa do problema.

Quando passamos referências concretas para `longest`, o _lifetime_ concreto que é substituído por `'a` é a parte do escopo de `x` que se sobrepõe ao escopo de `y`. Em outras palavras, o _lifetime_ genérico `'a` obterá o _lifetime_ concreto que é igual ao menor dos _lifetimes_ de `x` e `y`. Como anotamos a referência retornada com o mesmo parâmetro de _lifetime_ `'a`, a referência retornada também será válida para a duração do menor dos _lifetimes_ de `x` e `y`.

Vamos ver como as anotações de _lifetime_ restringem a função `longest` passando referências que têm diferentes _lifetimes_ concretos. A Listagem 10-22 é um exemplo direto.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

Listagem 10-22: Usando a função `longest` com referências a valores `String` que têm diferentes _lifetimes_ concretos

Neste exemplo, `string1` é válido até o final do escopo externo, `string2` é válido até o final do escopo interno e `result` referencia algo que é válido até o final do escopo interno. Execute este código e você verá que o _borrow checker_ aprova; ele compilará e imprimirá `The longest string is long string is long`.

Em seguida, vamos tentar um exemplo que mostra que o _lifetime_ da referência em `result` deve ser o menor _lifetime_ dos dois argumentos. Vamos mover a declaração da variável `result` para fora do escopo interno, mas deixar a atribuição do valor à variável `result` dentro do escopo com `string2`. Em seguida, moveremos o `println!` que usa `result` para fora do escopo interno, depois que o escopo interno terminar. O código na Listagem 10-23 não compilará.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

Listagem 10-23: Tentando usar `result` depois que `string2` saiu do escopo

Quando tentamos compilar este código, obtemos este erro:

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

O erro mostra que, para que `result` seja válido para a instrução `println!`, `string2` precisaria ser válido até o final do escopo externo. Rust sabe disso porque anotamos os _lifetimes_ dos parâmetros da função e os valores de retorno usando o mesmo parâmetro de _lifetime_ `'a`.

Como humanos, podemos olhar para este código e ver que `string1` é maior que `string2` e, portanto, `result` conterá uma referência a `string1`. Como `string1` ainda não saiu do escopo, uma referência a `string1` ainda será válida para a instrução `println!`. No entanto, o compilador não pode ver que a referência é válida neste caso. Dissemos ao Rust que o _lifetime_ da referência retornada pela função `longest` é o mesmo que o menor dos _lifetimes_ das referências passadas. Portanto, o _borrow checker_ proíbe o código na Listagem 10-23 por possivelmente ter uma referência inválida.

Tente projetar mais experimentos que variem os valores e _lifetimes_ das referências passadas para a função `longest` e como a referência retornada é usada. Faça hipóteses sobre se seus experimentos passarão ou não no _borrow checker_ antes de compilar; então verifique se você está certo!
