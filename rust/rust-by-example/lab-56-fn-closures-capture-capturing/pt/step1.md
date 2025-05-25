# Captura

Closures são inerentemente flexíveis e farão o que a funcionalidade exigir para que o closure funcione sem anotação. Isso permite que a captura se adapte flexívelmente ao caso de uso, às vezes movendo e outras vezes emprestando. Os closures podem capturar variáveis:

- por referência: `&T`
- por referência mutável: `&mut T`
- por valor: `T`

Eles preferencialmente capturam variáveis por referência e só descem quando necessário.

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // Um closure para imprimir `color`, que imediatamente empresta (`&`) `color` e
    // armazena o empréstimo e o closure na variável `print`. Ele permanecerá
    // emprestado até que `print` seja usado pela última vez.
    //
    // `println!` só requer argumentos por referência imutável, portanto, não impõe nada mais restritivo.
    let print = || println!("`color`: {}", color);

    // Chame o closure usando o empréstimo.
    print();

    // `color` pode ser emprestado novamente de forma imutável, porque o closure apenas mantém
    // uma referência imutável a `color`.
    let _reborrow = &color;
    print();

    // Uma movimentação ou novo empréstimo é permitido após o uso final de `print`
    let _color_moved = color;


    let mut count = 0;
    // Um closure para incrementar `count` pode receber `&mut count` ou `count`,
    // mas `&mut count` é menos restritivo, então ele recebe isso. Imediatamente
    // empresta `count`.
    //
    // Um `mut` é necessário em `inc` porque um `&mut` é armazenado dentro. Assim,
    // chamar o closure modifica o closure, o que requer um `mut`.
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // Chame o closure usando um empréstimo mutável.
    inc();

    // O closure ainda empresta `count` de forma mutável porque é chamado mais tarde.
    // Uma tentativa de novo empréstimo resultará em um erro.
    // let _reborrow = &count;
    // ^ TODO: tente descomentar esta linha.
    inc();

    // O closure não precisa mais emprestar `&mut count`. Portanto, é
    // possível fazer um novo empréstimo sem erro
    let _count_reborrowed = &mut count;


    // Um tipo não copiável.
    let movable = Box::new(3);

    // `mem::drop` requer `T`, então isso deve ser por valor. Um tipo copiável
    // copiaria para o closure, deixando o original intocado.
    // Um não copiável deve se mover e, portanto, `movable` se move imediatamente para
    // o closure.
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` consome a variável, então isso só pode ser chamado uma vez.
    consume();
    // consume();
    // ^ TODO: Tente descomentar esta linha.
}
```

Usando `move` antes dos pipes verticais força o closure a assumir a propriedade das variáveis capturadas:

```rust
fn main() {
    // `Vec` tem semântica não copiável.
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ Descomentar a linha acima resultará em erro em tempo de compilação
    // porque o verificador de empréstimos não permite reutilizar a variável após ela
    // ter sido movida.

    // Remover `move` da assinatura do closure fará com que o closure
    // empreste a variável _haystack_ de forma imutável, portanto, _haystack_ ainda está
    // disponível e descomentar a linha acima não causará um erro.
}
```
