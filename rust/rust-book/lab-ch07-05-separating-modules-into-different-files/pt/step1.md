# Separando Módulos em Arquivos Diferentes

Até agora, todos os exemplos neste capítulo definiram múltiplos módulos em um único arquivo. Quando os módulos ficam grandes, você pode querer mover suas definições para um arquivo separado para tornar o código mais fácil de navegar.

Por exemplo, vamos começar com o código na Listagem 7-17 que tinha múltiplos módulos de restaurante. Vamos extrair módulos em arquivos em vez de ter todos os módulos definidos no arquivo raiz da crate. Neste caso, o arquivo raiz da crate é `src/lib.rs`, mas este procedimento também funciona com crates binárias cujo arquivo raiz da crate é `src/main.rs`.

Primeiro, vamos extrair o módulo `front_of_house` para seu próprio arquivo. Remova o código dentro das chaves para o módulo `front_of_house`, deixando apenas a declaração `mod front_of_house;`, de modo que `src/lib.rs` contenha o código mostrado na Listagem 7-21. Observe que isso não compilará até que criemos o arquivo `src/front_of_house.rs` na Listagem 7-22.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listagem 7-21: Declarando o módulo `front_of_house` cujo corpo estará em `src/front_of_house.rs`

Em seguida, coloque o código que estava nas chaves em um novo arquivo chamado `src/front_of_house.rs`, conforme mostrado na Listagem 7-22. O compilador sabe procurar neste arquivo porque encontrou a declaração do módulo na raiz da crate com o nome `front_of_house`.

Nome do arquivo: `src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Listagem 7-22: Definições dentro do módulo `front_of_house` em `src/front_of_house.rs`

Observe que você só precisa carregar um arquivo usando uma declaração `mod` _uma vez_ em sua árvore de módulos. Uma vez que o compilador sabe que o arquivo faz parte do projeto (e sabe onde na árvore de módulos o código reside por causa de onde você colocou a instrução `mod`), outros arquivos em seu projeto devem se referir ao código do arquivo carregado usando um caminho para onde ele foi declarado, conforme coberto em "Caminhos para se Referir a um Item na Árvore de Módulos". Em outras palavras, `mod` _não_ é uma operação de "inclusão" que você pode ter visto em outras linguagens de programação.

Em seguida, vamos extrair o módulo `hosting` para seu próprio arquivo. O processo é um pouco diferente porque `hosting` é um submódulo de `front_of_house`, não do módulo raiz. Colocaremos o arquivo para `hosting` em um novo diretório que será nomeado para seus ancestrais na árvore de módulos, neste caso _src/front_of_house_.

Para começar a mover `hosting`, mudamos `src/front_of_house.rs` para conter apenas a declaração do módulo `hosting`:

Nome do arquivo: `src/front_of_house.rs`

```rust
pub mod hosting;
```

Então, criamos um diretório `src/front_of_house` e um arquivo `hosting.rs` para conter as definições feitas no módulo `hosting`:

Nome do arquivo: `src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

Se, em vez disso, colocássemos `hosting.rs` no diretório `src`, o compilador esperaria que o código `hosting.rs` estivesse em um módulo `hosting` declarado na raiz da crate, e não declarado como um filho do módulo `front_of_house`. As regras do compilador para quais arquivos verificar para o código de quais módulos significam que os diretórios e arquivos correspondem mais de perto à árvore de módulos.

> **Caminhos de Arquivos Alternativos**
>
> Até agora, cobrimos os caminhos de arquivos mais idiomáticos que o compilador Rust usa, mas Rust também suporta um estilo mais antigo de caminho de arquivo. Para um módulo chamado `front_of_house` declarado na raiz da crate, o compilador procurará o código do módulo em:
>
> - `src/front_of_house.rs` (o que cobrimos)
> - `src/front_of_house/mod.rs` (estilo mais antigo, caminho ainda suportado)
>
> Para um módulo chamado `hosting` que é um submódulo de `front_of_house`, o compilador procurará o código do módulo em:
>
> - `src/front_of_house/hosting.rs` (o que cobrimos)
> - `src/front_of_house/hosting/mod.rs` (estilo mais antigo, caminho ainda suportado)
>
> Se você usar ambos os estilos para o mesmo módulo, você receberá um erro do compilador. Usar uma mistura de ambos os estilos para diferentes módulos no mesmo projeto é permitido, mas pode ser confuso para as pessoas que navegam em seu projeto.
>
> A principal desvantagem do estilo que usa arquivos chamados `mod.rs` é que seu projeto pode acabar com muitos arquivos chamados `mod.rs`, o que pode ser confuso quando você os tem abertos em seu editor ao mesmo tempo.

Movemos o código de cada módulo para um arquivo separado, e a árvore de módulos permanece a mesma. As chamadas de função em `eat_at_restaurant` funcionarão sem qualquer modificação, mesmo que as definições vivam em arquivos diferentes. Essa técnica permite que você mova módulos para novos arquivos à medida que eles crescem em tamanho.

Observe que a instrução `pub use crate::front_of_house::hosting` em `src/lib.rs` também não mudou, nem `use` tem qualquer impacto em quais arquivos são compilados como parte da crate. A palavra-chave `mod` declara módulos, e Rust procura em um arquivo com o mesmo nome do módulo para o código que vai para esse módulo.
