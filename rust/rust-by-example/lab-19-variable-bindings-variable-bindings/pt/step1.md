# Ligações de Variáveis

O Rust fornece segurança de tipo através de tipagem estática. As ligações de variáveis podem ser anotadas com o tipo quando declaradas. No entanto, na maioria dos casos, o compilador será capaz de inferir o tipo da variável a partir do contexto, reduzindo significativamente a necessidade de anotações.

Valores (como literais) podem ser ligados a variáveis usando a ligação `let`.

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // copia `an_integer` para `copied_integer`
    let copied_integer = an_integer;

    println!("Um inteiro: {:?}", copied_integer);
    println!("Um booleano: {:?}", a_boolean);
    println!("Conheça o valor unitário: {:?}", unit);

    // O compilador emite avisos sobre ligações de variáveis não utilizadas; estes avisos podem ser silenciados prefixando o nome da variável com um sublinhado
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ Prefixe com um sublinhado para suprimir o aviso
    // Note que os avisos podem não ser exibidos num navegador
}
```
