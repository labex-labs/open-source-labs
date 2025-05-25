# Inferência e Anotação de Tipos de Closure

Existem mais diferenças entre funções e closures. Closures geralmente não exigem que você anote os tipos dos parâmetros ou o valor de retorno como as funções `fn` fazem. Anotações de tipo são necessárias em funções porque os tipos fazem parte de uma interface explícita exposta aos seus usuários. Definir essa interface rigidamente é importante para garantir que todos concordem sobre quais tipos de valores uma função usa e retorna. Closures, por outro lado, não são usadas em uma interface exposta como esta: elas são armazenadas em variáveis e usadas sem nomeá-las e expô-las aos usuários de nossa biblioteca.

Closures são tipicamente curtas e relevantes apenas dentro de um contexto restrito, em vez de em qualquer cenário arbitrário. Dentro desses contextos limitados, o compilador pode inferir os tipos dos parâmetros e o tipo de retorno, de forma semelhante a como ele é capaz de inferir os tipos da maioria das variáveis (existem casos raros em que o compilador também precisa de anotações de tipo de closure).

Assim como com variáveis, podemos adicionar anotações de tipo se quisermos aumentar a explicitude e a clareza, à custa de sermos mais verbosos do que o estritamente necessário. Anotar os tipos para uma closure seria semelhante à definição mostrada na Listagem 13-2. Neste exemplo, estamos definindo uma closure e armazenando-a em uma variável, em vez de definir a closure no local onde a passamos como um argumento, como fizemos na Listagem 13-1.

Nome do arquivo: `src/main.rs`

```rust
let expensive_closure = |num: u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

Listagem 13-2: Adicionando anotações de tipo opcionais dos tipos de parâmetro e valor de retorno na closure

Com as anotações de tipo adicionadas, a sintaxe de closures se assemelha mais à sintaxe de funções. Aqui, definimos uma função que adiciona 1 ao seu parâmetro e uma closure que tem o mesmo comportamento, para comparação. Adicionamos alguns espaços para alinhar as partes relevantes. Isso ilustra como a sintaxe de closure é semelhante à sintaxe de função, exceto pelo uso de pipes e a quantidade de sintaxe que é opcional:

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

A primeira linha mostra uma definição de função e a segunda linha mostra uma definição de closure totalmente anotada. Na terceira linha, removemos as anotações de tipo da definição da closure. Na quarta linha, removemos as chaves, que são opcionais porque o corpo da closure tem apenas uma expressão. Estas são todas as definições válidas que produzirão o mesmo comportamento quando forem chamadas. As linhas `add_one_v3` e `add_one_v4` exigem que as closures sejam avaliadas para poder compilar, porque os tipos serão inferidos de seu uso. Isso é semelhante a `let v = Vec::new();` precisando de anotações de tipo ou valores de algum tipo para serem inseridos no `Vec` para que o Rust possa inferir o tipo.

Para definições de closure, o compilador inferirá um tipo concreto para cada um de seus parâmetros e para seu valor de retorno. Por exemplo, a Listagem 13-3 mostra a definição de uma closure curta que apenas retorna o valor que recebe como um parâmetro. Essa closure não é muito útil, exceto para os propósitos deste exemplo. Observe que não adicionamos nenhuma anotação de tipo à definição. Como não há anotações de tipo, podemos chamar a closure com qualquer tipo, o que fizemos aqui com `String` na primeira vez. Se tentarmos chamar `example_closure` com um inteiro, receberemos um erro.

Nome do arquivo: `src/main.rs`

```rust
let example_closure = |x| x;

let s = example_closure(String::from("hello"));
let n = example_closure(5);
```

Listagem 13-3: Tentando chamar uma closure cujos tipos são inferidos com dois tipos diferentes

O compilador nos dá este erro:

```bash
error[E0308]: mismatched types
 --> src/main.rs:5:29
  |
5 |     let n = example_closure(5);
  |                             ^- help: try using a conversion method:
`.to_string()`
  |                             |
  |                             expected struct `String`, found integer
```

Na primeira vez que chamamos `example_closure` com o valor `String`, o compilador infere que o tipo de `x` e o tipo de retorno da closure são `String`. Esses tipos são então bloqueados na closure em `example_closure`, e recebemos um erro de tipo quando tentamos usar um tipo diferente com a mesma closure.
