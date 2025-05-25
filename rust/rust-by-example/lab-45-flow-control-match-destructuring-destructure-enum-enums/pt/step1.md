# enums

Um `enum` é desestruturado de forma semelhante:

```rust
// `allow` necessário para silenciar avisos porque apenas
// uma variante é usada.
#[allow(dead_code)]
enum Color {
    // Estes 3 são especificados apenas pelo seu nome.
    Red,
    Blue,
    Green,
    // Estes também ligam tuplas `u32` a diferentes nomes: modelos de cores.
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    // TODO ^ Tente diferentes variantes para `color`

    println!("Qual a cor?");
    // Um `enum` pode ser desestruturado usando um `match`.
    match color {
        Color::Red   => println!("A cor é Vermelha!"),
        Color::Blue  => println!("A cor é Azul!"),
        Color::Green => println!("A cor é Verde!"),
        Color::RGB(r, g, b) =>
            println!("Vermelho: {}, verde: {}, e azul: {}!", r, g, b),
        Color::HSV(h, s, v) =>
            println!("Matiz: {}, saturação: {}, valor: {}!", h, s, v),
        Color::HSL(h, s, l) =>
            println!("Matiz: {}, saturação: {}, luminosidade: {}!", h, s, l),
        Color::CMY(c, m, y) =>
            println!("Ciano: {}, magenta: {}, amarelo: {}!", c, m, y),
        Color::CMYK(c, m, y, k) =>
            println!("Ciano: {}, magenta: {}, amarelo: {}, chave (preto): {}!",
                c, m, y, k),
        // Não é necessário outro ramo porque todas as variantes foram examinadas
    }
}
```
