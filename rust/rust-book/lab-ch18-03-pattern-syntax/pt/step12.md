# Um Valor Inteiro com \_

Usamos o sublinhado como um padrão curinga (wildcard) que corresponderá a qualquer valor, mas não se vinculará ao valor. Isso é especialmente útil como o último braço em uma expressão `match`, mas também podemos usá-lo em qualquer padrão, incluindo parâmetros de função, como mostrado na Listagem 18-17.

Nome do arquivo: `src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("This code only uses the y parameter: {y}");
}

fn main() {
    foo(3, 4);
}
```

Listagem 18-17: Usando `_` em uma assinatura de função

Este código ignorará completamente o valor `3` passado como o primeiro argumento e imprimirá `This code only uses the y parameter: 4`.

Na maioria dos casos, quando você não precisa mais de um determinado parâmetro de função, você alteraria a assinatura para que ela não inclua o parâmetro não utilizado. Ignorar um parâmetro de função pode ser especialmente útil em casos em que, por exemplo, você está implementando uma trait quando precisa de uma determinada assinatura de tipo, mas o corpo da função em sua implementação não precisa de um dos parâmetros. Você então evita obter um aviso do compilador sobre parâmetros de função não utilizados, como faria se usasse um nome em vez disso.
