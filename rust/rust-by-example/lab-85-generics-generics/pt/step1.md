# Genéricos

_Genéricos_ é o tema da generalização de tipos e funcionalidades para casos mais amplos. Isso é extremamente útil para reduzir a duplicação de código de várias maneiras, mas pode exigir uma sintaxe mais elaborada. Especificamente, ser genérico requer um cuidado especial para especificar quais tipos são considerados válidos para um tipo genérico. O uso mais simples e comum de genéricos é para parâmetros de tipo.

Um parâmetro de tipo é especificado como genérico pelo uso de colchetes angulares e geralmente representado como `<T>`. Em Rust, "genérico" também descreve qualquer coisa que aceite um ou mais parâmetros de tipo genérico `<T>`. Qualquer tipo especificado como um parâmetro de tipo genérico é genérico, e tudo o mais é concreto (não genérico).

Por exemplo, definindo uma _função genérica_ chamada `foo` que recebe um argumento `T` de qualquer tipo:

```rust
fn foo<T>(arg: T) { ... }
```

Como `T` foi especificado como um parâmetro de tipo genérico usando `<T>`, ele é considerado genérico quando usado aqui como `(arg: T)`. Este é o caso mesmo se `T` tiver sido previamente definido como uma `struct`.

Este exemplo demonstra a sintaxe em ação:

```rust
// Um tipo concreto `A`.
struct A;

// Ao definir o tipo `Single`, o primeiro uso de `A` não é precedido por `<A>`.
// Portanto, `Single` é um tipo concreto, e `A` é definido como acima.
struct Single(A);
//            ^ Aqui está o primeiro uso de `Single` do tipo `A`.

// Aqui, `<T>` precede o primeiro uso de `T`, então `SingleGen` é um tipo genérico.
// Como o parâmetro de tipo `T` é genérico, ele pode ser qualquer coisa, incluindo
// o tipo concreto `A` definido no início.
struct SingleGen<T>(T);

fn main() {
    // `Single` é concreto e explicitamente recebe `A`.
    let _s = Single(A);

    // Crie uma variável `_char` do tipo `SingleGen<char>`
    // e atribua a ela o valor `SingleGen('a')`.
    // Aqui, `SingleGen` tem um parâmetro de tipo explicitamente especificado.
    let _char: SingleGen<char> = SingleGen('a');

    // `SingleGen` também pode ter um parâmetro de tipo implicitamente especificado:
    let _t    = SingleGen(A); // Usa `A` definido no início.
    let _i32  = SingleGen(6); // Usa `i32`.
    let _char = SingleGen('a'); // Usa `char`.
}
```
