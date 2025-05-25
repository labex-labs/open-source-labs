# Definindo Métodos

Vamos mudar a função `area` que tem uma instância de `Rectangle` como parâmetro e, em vez disso, criar um método `area` definido na struct `Rectangle`, como mostrado na Listagem 5-13.

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

1 impl Rectangle {
  2 fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
      3 rect1.area()
    );
}
```

Listagem 5-13: Definindo um método `area` na struct `Rectangle`

Para definir a função dentro do contexto de `Rectangle`, iniciamos um bloco `impl` (implementação) para `Rectangle` \[1]. Tudo dentro deste bloco `impl` será associado ao tipo `Rectangle`. Em seguida, movemos a função `area` para dentro das chaves do `impl` \[2] e mudamos o primeiro (e, neste caso, único) parâmetro para ser `self` na assinatura e em todos os lugares dentro do corpo. Em `main`, onde chamamos a função `area` e passamos `rect1` como um argumento, podemos, em vez disso, usar a _sintaxe de método_ para chamar o método `area` na nossa instância de `Rectangle` \[3]. A sintaxe do método vem depois de uma instância: adicionamos um ponto seguido pelo nome do método, parênteses e quaisquer argumentos.

Na assinatura de `area`, usamos `&self` em vez de `rectangle: &Rectangle`. O `&self` é, na verdade, uma abreviação de `self: &Self`. Dentro de um bloco `impl`, o tipo `Self` é um alias para o tipo para o qual o bloco `impl` é destinado. Os métodos devem ter um parâmetro chamado `self` do tipo `Self` para seu primeiro parâmetro, então o Rust permite que você abrevie isso com apenas o nome `self` no primeiro lugar do parâmetro. Observe que ainda precisamos usar o `&` na frente da abreviação `self` para indicar que este método empresta a instância `Self`, assim como fizemos em `rectangle: &Rectangle`. Os métodos podem assumir a propriedade de `self`, emprestar `self` imutavelmente, como fizemos aqui, ou emprestar `self` mutavelmente, assim como podem fazer com qualquer outro parâmetro.

Escolhemos `&self` aqui pela mesma razão que usamos `&Rectangle` na versão da função: não queremos assumir a propriedade e só queremos ler os dados na struct, não escrever nela. Se quiséssemos mudar a instância em que chamamos o método como parte do que o método faz, usaríamos `&mut self` como o primeiro parâmetro. Ter um método que assume a propriedade da instância usando apenas `self` como o primeiro parâmetro é raro; essa técnica é geralmente usada quando o método transforma `self` em outra coisa e você quer impedir que o chamador use a instância original após a transformação.

A principal razão para usar métodos em vez de funções, além de fornecer a sintaxe do método e não ter que repetir o tipo de `self` na assinatura de cada método, é a organização. Colocamos todas as coisas que podemos fazer com uma instância de um tipo em um bloco `impl` em vez de fazer com que futuros usuários do nosso código procurem as capacidades de `Rectangle` em vários lugares na biblioteca que fornecemos.

Observe que podemos escolher dar a um método o mesmo nome de um dos campos da struct. Por exemplo, podemos definir um método em `Rectangle` que também se chama `width`:

Nome do arquivo: `src/main.rs`

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!(
            "The rectangle has a nonzero width; it is {}",
            rect1.width
        );
    }
}
```

Aqui, estamos escolhendo fazer com que o método `width` retorne `true` se o valor no campo `width` da instância for maior que `0` e `false` se o valor for `0`: podemos usar um campo dentro de um método com o mesmo nome para qualquer finalidade. Em `main`, quando seguimos `rect1.width` com parênteses, o Rust sabe que queremos dizer o método `width`. Quando não usamos parênteses, o Rust sabe que queremos dizer o campo `width`.

Frequentemente, mas nem sempre, quando damos métodos com o mesmo nome de um campo, queremos que ele apenas retorne o valor no campo e não faça mais nada. Métodos como este são chamados de _getters_, e o Rust não os implementa automaticamente para campos de struct como algumas outras linguagens fazem. Getters são úteis porque você pode tornar o campo privado, mas o método público, e, assim, habilitar o acesso somente leitura a esse campo como parte da API pública do tipo. Discutiremos o que são público e privado e como designar um campo ou método como público ou privado no Capítulo 7.

> **Onde está o operador -\>?**
>
> Em C e C++, dois operadores diferentes são usados para chamar métodos: você usa `.` se estiver chamando um método no objeto diretamente e `->` se estiver chamando o método em um ponteiro para o objeto e precisar desreferenciar o ponteiro primeiro. Em outras palavras, se `object` é um ponteiro, `object->`something`()` é semelhante a `(*object).`something`()`.
>
> O Rust não tem um equivalente ao operador `->`; em vez disso, o Rust tem um recurso chamado _referenciamento e desreferenciamento automáticos_. Chamar métodos é um dos poucos lugares no Rust que tem esse comportamento.
>
> Veja como funciona: quando você chama um método com `object.`something`()`, o Rust adiciona automaticamente `&`, `&mut` ou `*` para que `object` corresponda à assinatura do método. Em outras palavras, o seguinte é o mesmo:
>
>     p1.distance(&p2);
>     (&p1).distance(&p2);
>
> O primeiro parece muito mais limpo. Este comportamento de referenciamento automático funciona porque os métodos têm um receptor claro --- o tipo de `self`. Dado o receptor e o nome de um método, o Rust pode descobrir definitivamente se o método está lendo (`&self`), mutando (`&mut self`) ou consumindo (`self`). O fato de o Rust tornar o empréstimo implícito para receptores de método é uma grande parte de tornar a propriedade ergonômica na prática.
