# Parâmetros de Tipo Genérico Padrão e Sobrecarga de Operador

Quando usamos parâmetros de tipo genérico, podemos especificar um tipo concreto padrão para o tipo genérico. Isso elimina a necessidade de implementadores da trait especificarem um tipo concreto se o tipo padrão funcionar. Você especifica um tipo padrão ao declarar um tipo genérico com a sintaxe `<`PlaceholderType`=`ConcreteType`>`.

Um ótimo exemplo de uma situação em que essa técnica é útil é com _sobrecarga de operador_, na qual você personaliza o comportamento de um operador (como `+`) em situações particulares.

Rust não permite que você crie seus próprios operadores ou sobrecarregue operadores arbitrários. Mas você pode sobrecarregar as operações e as traits correspondentes listadas em `std::ops` implementando as traits associadas ao operador. Por exemplo, na Listagem 19-14, sobrecarregamos o operador `+` para somar duas instâncias de `Point`. Fazemos isso implementando a trait `Add` em uma struct `Point`.

Nome do arquivo: `src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Listagem 19-14: Implementando a trait `Add` para sobrecarregar o operador `+` para instâncias de `Point`

O método `add` soma os valores `x` de duas instâncias de `Point` e os valores `y` de duas instâncias de `Point` para criar um novo `Point`. A trait `Add` tem um tipo associado chamado `Output` que determina o tipo retornado do método `add`.

O tipo genérico padrão neste código está dentro da trait `Add`. Aqui está sua definição:

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

Este código deve parecer geralmente familiar: uma trait com um método e um tipo associado. A parte nova é `Rhs=Self`: esta sintaxe é chamada de _parâmetros de tipo padrão_. O parâmetro de tipo genérico `Rhs` (abreviação de "right-hand side" - lado direito) define o tipo do parâmetro `rhs` no método `add`. Se não especificarmos um tipo concreto para `Rhs` quando implementarmos a trait `Add`, o tipo de `Rhs` será definido como `Self`, que será o tipo em que estamos implementando `Add`.

Quando implementamos `Add` para `Point`, usamos o padrão para `Rhs` porque queríamos somar duas instâncias de `Point`. Vamos analisar um exemplo de implementação da trait `Add` onde queremos personalizar o tipo `Rhs` em vez de usar o padrão.

Temos duas structs, `Millimeters` e `Meters`, que contêm valores em unidades diferentes. Este encapsulamento fino de um tipo existente em outra struct é conhecido como _padrão newtype_, que descrevemos em mais detalhes em "Usando o Padrão Newtype para Implementar Traits Externas em Tipos Externos". Queremos somar valores em milímetros a valores em metros e fazer com que a implementação de `Add` faça a conversão corretamente. Podemos implementar `Add` para `Millimeters` com `Meters` como `Rhs`, conforme mostrado na Listagem 19-15.

Nome do arquivo: `src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

Listagem 19-15: Implementando a trait `Add` em `Millimeters` para somar `Millimeters` e `Meters`

Para somar `Millimeters` e `Meters`, especificamos `impl Add<Meters>` para definir o valor do parâmetro de tipo `Rhs` em vez de usar o padrão de `Self`.

Você usará parâmetros de tipo padrão de duas maneiras principais:

1.  Para estender um tipo sem quebrar o código existente
2.  Para permitir a personalização em casos específicos que a maioria dos usuários não precisará

A trait `Add` da biblioteca padrão é um exemplo do segundo propósito: geralmente, você somará dois tipos semelhantes, mas a trait `Add` oferece a capacidade de personalizar além disso. Usar um parâmetro de tipo padrão na definição da trait `Add` significa que você não precisa especificar o parâmetro extra na maioria das vezes. Em outras palavras, um pouco de código boilerplate de implementação não é necessário, tornando mais fácil usar a trait.

O primeiro propósito é semelhante ao segundo, mas ao contrário: se você deseja adicionar um parâmetro de tipo a uma trait existente, pode dar a ele um padrão para permitir a extensão da funcionalidade da trait sem quebrar o código de implementação existente.
