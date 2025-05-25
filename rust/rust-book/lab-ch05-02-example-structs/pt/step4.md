# Adicionando Funcionalidade Útil com Traits Derivados

Seria útil poder imprimir uma instância de `Rectangle` enquanto estamos depurando nosso programa e ver os valores de todos os seus campos. A Listagem 5-11 tenta usar a macro `println!` como usamos nos capítulos anteriores. No entanto, isso não funcionará.

Nome do arquivo: `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1);
}
```

Listagem 5-11: Tentando imprimir uma instância de `Rectangle`

Quando compilamos este código, recebemos um erro com esta mensagem principal:

```bash
error[E0277]: `Rectangle` doesn't implement `std::fmt::Display`
```

A macro `println!` pode fazer muitos tipos de formatação e, por padrão, as chaves dizem ao `println!` para usar a formatação conhecida como `Display`: saída destinada ao consumo direto do usuário final. Os tipos primitivos que vimos até agora implementam `Display` por padrão porque há apenas uma maneira de você querer mostrar um `1` ou qualquer outro tipo primitivo a um usuário. Mas com structs, a maneira como `println!` deve formatar a saída é menos clara porque há mais possibilidades de exibição: Você quer vírgulas ou não? Você quer imprimir as chaves? Todos os campos devem ser mostrados? Devido a essa ambiguidade, o Rust não tenta adivinhar o que queremos, e as structs não têm uma implementação fornecida de `Display` para usar com `println!` e o espaço reservado `{}`.

Se continuarmos lendo os erros, encontraremos esta nota útil:

    = help: the trait `std::fmt::Display` is not implemented for `Rectangle`
    = note: in format strings you may be able to use `{:?}` (or {:#?} for
    pretty-print) instead

Vamos tentar! A chamada da macro `println!` agora se parecerá com `println!("rect1 is {:?}", rect1);`. Colocar o especificador `:?` dentro das chaves diz ao `println!` que queremos usar um formato de saída chamado `Debug`. O trait `Debug` nos permite imprimir nossa struct de uma forma que seja útil para os desenvolvedores, para que possamos ver seu valor enquanto estamos depurando nosso código.

Compile o código com essa alteração. Droga! Ainda recebemos um erro:

```bash
error[E0277]: `Rectangle` doesn't implement `Debug`
```

Mas, novamente, o compilador nos dá uma nota útil:

```rust
= help: the trait `Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` or manually implement `Debug`
```

Rust _inclui_ funcionalidade para imprimir informações de depuração, mas temos que optar explicitamente por tornar essa funcionalidade disponível para nossa struct. Para fazer isso, adicionamos o atributo externo `#[derive(Debug)]` logo antes da definição da struct, conforme mostrado na Listagem 5-12.

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

Listagem 5-12: Adicionando o atributo para derivar o trait `Debug` e imprimindo a instância `Rectangle` usando a formatação de depuração

Agora, quando executamos o programa, não receberemos nenhum erro e veremos a seguinte saída:

```rust
rect1 is Rectangle { width: 30, height: 50 }
```

Legal! Não é a saída mais bonita, mas mostra os valores de todos os campos para esta instância, o que definitivamente ajudaria durante a depuração. Quando temos structs maiores, é útil ter uma saída que seja um pouco mais fácil de ler; nesses casos, podemos usar `{:#?}` em vez de `{:?}` na string `println!`. Neste exemplo, usar o estilo `{:#?}` produzirá a seguinte saída:

    rect1 is Rectangle {
        width: 30,
        height: 50,
    }

Outra maneira de imprimir um valor usando o formato `Debug` é usar a macro `dbg!`, que assume a propriedade de uma expressão (em oposição a `println!`, que assume uma referência), imprime o arquivo e o número da linha de onde essa chamada de macro `dbg!` ocorre em seu código, juntamente com o valor resultante dessa expressão, e retorna a propriedade do valor.

> Nota: Chamar a macro `dbg!` imprime no fluxo de console de erro padrão (`stderr`), em oposição a `println!`, que imprime no fluxo de console de saída padrão (`stdout`). Falaremos mais sobre `stderr` e `stdout` em "Escrevendo Mensagens de Erro para o Erro Padrão em Vez da Saída Padrão".

Aqui está um exemplo em que estamos interessados no valor que é atribuído ao campo `width`, bem como no valor da struct inteira em `rect1`:

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

Podemos colocar `dbg!` em torno da expressão `30 * scale` \[1] e, como `dbg!` retorna a propriedade do valor da expressão, o campo `width` receberá o mesmo valor que se não tivéssemos a chamada `dbg!` lá. Não queremos que `dbg!` assuma a propriedade de `rect1`, então usamos uma referência a `rect1` na próxima chamada \[2]. Veja como a saída deste exemplo se parece:

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

Podemos ver que a primeira parte da saída veio de \[1], onde estamos depurando a expressão `30 * scale`, e seu valor resultante é `60` (a formatação `Debug` implementada para inteiros é imprimir apenas seu valor). A chamada `dbg!` em \[2] produz o valor de `&rect1`, que é a struct `Rectangle`. Essa saída usa a formatação `Debug` bonita do tipo `Rectangle`. A macro `dbg!` pode ser realmente útil quando você está tentando descobrir o que seu código está fazendo!

Além do trait `Debug`, o Rust forneceu vários traits para usarmos com o atributo `derive` que podem adicionar comportamento útil aos nossos tipos personalizados. Esses traits e seus comportamentos estão listados no Apêndice C. Abordaremos como implementar esses traits com comportamento personalizado, bem como como criar seus próprios traits no Capítulo 10. Também existem muitos atributos além de `derive`; para obter mais informações, consulte a seção "Atributos" da Referência do Rust em *https://doc.rust-lang.org/reference/attributes.html*.

Nossa função `area` é muito específica: ela calcula apenas a área de retângulos. Seria útil vincular esse comportamento mais de perto à nossa struct `Rectangle` porque ela não funcionará com nenhum outro tipo. Vamos ver como podemos continuar a refatorar este código transformando a função `area` em um _método_ `area` definido em nosso tipo `Rectangle`.
