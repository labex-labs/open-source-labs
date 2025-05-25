# Usando Caminhos Aninhados para Limpar Listas `use` Grandes

Se estivermos usando vários itens definidos no mesmo crate ou no mesmo módulo, listar cada item em sua própria linha pode ocupar muito espaço vertical em nossos arquivos. Por exemplo, estas duas declarações `use` que tínhamos no jogo de adivinhação na Listagem 2-4 trazem itens de `std` para o escopo:

Nome do arquivo: `src/main.rs`

```rust
--snip--
use std::cmp::Ordering;
use std::io;
--snip--
```

Em vez disso, podemos usar caminhos aninhados para trazer os mesmos itens para o escopo em uma linha. Fazemos isso especificando a parte comum do caminho, seguida por dois dois pontos, e então chaves ao redor de uma lista das partes dos caminhos que diferem, como mostrado na Listagem 7-18.

Nome do arquivo: `src/main.rs`

```rust
--snip--
use std::{cmp::Ordering, io};
--snip--
```

Listagem 7-18: Especificando um caminho aninhado para trazer vários itens com o mesmo prefixo para o escopo

Em programas maiores, trazer muitos itens para o escopo do mesmo crate ou módulo usando caminhos aninhados pode reduzir muito o número de declarações `use` separadas necessárias!

Podemos usar um caminho aninhado em qualquer nível em um caminho, o que é útil ao combinar duas declarações `use` que compartilham um subcaminho. Por exemplo, a Listagem 7-19 mostra duas declarações `use`: uma que traz `std::io` para o escopo e outra que traz `std::io::Write` para o escopo.

Nome do arquivo: `src/lib.rs`

```rust
use std::io;
use std::io::Write;
```

Listagem 7-19: Duas declarações `use` onde uma é um subcaminho da outra

A parte comum desses dois caminhos é `std::io`, e esse é o primeiro caminho completo. Para mesclar esses dois caminhos em uma declaração `use`, podemos usar `self` no caminho aninhado, como mostrado na Listagem 7-20.

Nome do arquivo: `src/lib.rs`

```rust
use std::io::{self, Write};
```

Listagem 7-20: Combinando os caminhos na Listagem 7-19 em uma declaração `use`

Esta linha traz `std::io` e `std::io::Write` para o escopo.
