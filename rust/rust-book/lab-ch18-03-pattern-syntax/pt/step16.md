# Condicionais Extras com Match Guards

Um _match guard_ é uma condição `if` adicional, especificada após o padrão em um braço `match`, que também deve corresponder para que esse braço seja escolhido. Match guards são úteis para expressar ideias mais complexas do que um padrão sozinho permite.

A condição pode usar variáveis criadas no padrão. A Listagem 18-26 mostra um `match` onde o primeiro braço tem o padrão `Some(x)` e também tem um match guard de `if x % 2 == 0` (que será `true` se o número for par).

Nome do arquivo: `src/main.rs`

```rust
let num = Some(4);

match num {
    Some(x) if x % 2 == 0 => println!("The number {x} is even"),
    Some(x) => println!("The number {x} is odd"),
    None => (),
}
```

Listagem 18-26: Adicionando um match guard a um padrão

Este exemplo imprimirá `The number 4 is even`. Quando `num` é comparado ao padrão no primeiro braço, ele corresponde porque `Some(4)` corresponde a `Some(x)`. Então, o match guard verifica se o resto da divisão de `x` por 2 é igual a 0 e, como é, o primeiro braço é selecionado.

Se `num` fosse `Some(5)` em vez disso, o match guard no primeiro braço teria sido `false` porque o resto de 5 dividido por 2 é 1, que não é igual a 0. Rust então iria para o segundo braço, que corresponderia porque o segundo braço não tem um match guard e, portanto, corresponde a qualquer variante `Some`.

Não há como expressar a condição `if x % 2 == 0` dentro de um padrão, então o match guard nos dá a capacidade de expressar essa lógica. A desvantagem dessa expressividade adicional é que o compilador não tenta verificar a exaustividade quando expressões de match guard estão envolvidas.

Na Listagem 18-11, mencionamos que poderíamos usar match guards para resolver nosso problema de sombreamento de padrões. Lembre-se de que criamos uma nova variável dentro do padrão na expressão `match` em vez de usar a variável fora do `match`. Essa nova variável significava que não podíamos testar em relação ao valor da variável externa. A Listagem 18-27 mostra como podemos usar um match guard para corrigir esse problema.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(n) if n == y => println!("Matched, n = {n}"),
        _ => println!("Default case, x = {:?}", x),
    }

    println!("at the end: x = {:?}, y = {y}", x);
}
```

Listagem 18-27: Usando um match guard para testar a igualdade com uma variável externa

Este código agora imprimirá `Default case, x = Some(5)`. O padrão no segundo braço `match` não introduz uma nova variável `y` que sombrearia o `y` externo, o que significa que podemos usar o `y` externo no match guard. Em vez de especificar o padrão como `Some(y)`, que teria sombreado o `y` externo, especificamos `Some(n)`. Isso cria uma nova variável `n` que não sombreia nada porque não há nenhuma variável `n` fora do `match`.

O match guard `if n == y` não é um padrão e, portanto, não introduz novas variáveis. Este `y` _é_ o `y` externo, em vez de um novo `y` sombreado, e podemos procurar um valor que tenha o mesmo valor que o `y` externo, comparando `n` a `y`.

Você também pode usar o operador _or_ `|` em um match guard para especificar vários padrões; a condição do match guard se aplicará a todos os padrões. A Listagem 18-28 mostra a precedência ao combinar um padrão que usa `|` com um match guard. A parte importante deste exemplo é que o match guard `if y` se aplica a `4`, `5`, _e_ `6`, embora possa parecer que `if y` se aplica apenas a `6`.

Nome do arquivo: `src/main.rs`

```rust
let x = 4;
let y = false;

match x {
    4 | 5 | 6 if y => println!("yes"),
    _ => println!("no"),
}
```

Listagem 18-28: Combinando vários padrões com um match guard

A condição match afirma que o braço corresponde apenas se o valor de `x` for igual a `4`, `5` ou `6` _e_ se `y` for `true`. Quando este código é executado, o padrão do primeiro braço corresponde porque `x` é `4`, mas o match guard `if y` é `false`, então o primeiro braço não é escolhido. O código passa para o segundo braço, que corresponde, e este programa imprime `no`. A razão é que a condição `if` se aplica a todo o padrão `4 | 5 | 6`, não apenas ao último valor `6`. Em outras palavras, a precedência de um match guard em relação a um padrão se comporta assim:

```rust
(4 | 5 | 6) if y => ...
```

em vez disso:

```rust
4 | 5 | (6 if y) => ...
```

Após executar o código, o comportamento de precedência é evidente: se o match guard fosse aplicado apenas ao valor final na lista de valores especificados usando o operador `|`, o braço teria correspondido e o programa teria impresso `yes`.
