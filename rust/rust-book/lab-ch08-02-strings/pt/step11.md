# Métodos para Iterar sobre Strings

A melhor maneira de operar em pedaços de strings é ser explícito sobre se você deseja caracteres ou bytes. Para valores escalares Unicode individuais, use o método `chars`. Chamar `chars` em "Зд" separa e retorna dois valores do tipo `char`, e você pode iterar sobre o resultado para acessar cada elemento:

    for c in "Зд".chars() {
        println!("{c}");
    }

Este código imprimirá o seguinte:

```rust
З
д
```

Alternativamente, o método `bytes` retorna cada byte bruto, o que pode ser apropriado para o seu domínio:

    for b in "Зд".bytes() {
        println!("{b}");
    }

Este código imprimirá os quatro bytes que compõem esta string:

    208
    151
    208
    180

Mas certifique-se de lembrar que valores escalares Unicode válidos podem ser compostos por mais de um byte.

Obter clusters de grafemas de strings, como no script Devanagari, é complexo, portanto, essa funcionalidade não é fornecida pela biblioteca padrão. Crates estão disponíveis em *https://crates.io* se esta for a funcionalidade que você precisa.
