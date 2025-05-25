# Strings

Existem dois tipos de strings em Rust: `String` e `&str`.

Uma `String` é armazenada como um vetor de bytes (`Vec<u8>`), mas garante sempre ser uma sequência UTF-8 válida. `String` é alocada no heap (heap allocated), expansível e não é terminada em nulo.

`&str` é uma fatia (slice) (`&[u8]`) que sempre aponta para uma sequência UTF-8 válida e pode ser usada para visualizar uma `String`, assim como `&[T]` é uma visualização de `Vec<T>`.

```rust
fn main() {
    // (todas as anotações de tipo são supérfluas)
    // Uma referência a uma string alocada em memória somente leitura
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangrama: {}", pangram);

    // Iterar sobre as palavras em ordem inversa, nenhuma nova string é alocada
    println!("Palavras em ordem inversa");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // Copiar caracteres em um vetor, ordenar e remover duplicatas
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // Criar uma `String` vazia e expansível
    let mut string = String::new();
    for c in chars {
        // Inserir um char no final da string
        string.push(c);
        // Inserir uma string no final da string
        string.push_str(", ");
    }

    // A string aparada é uma fatia da string original, portanto, nenhuma nova
    // alocação é realizada
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Caracteres usados: {}", trimmed_str);

    // Alocar uma string no heap
    let alice = String::from("I like dogs");
    // Alocar nova memória e armazenar a string modificada lá
    let bob: String = alice.replace("dog", "cat");

    println!("Alice diz: {}", alice);
    println!("Bob diz: {}", bob);
}
```

Mais métodos `str`/`String` podem ser encontrados nos módulos `std::str` e `std::string`

## Literais e escapes

Existem várias maneiras de escrever literais de string com caracteres especiais neles. Todos resultam em um `&str` semelhante, então é melhor usar a forma que for mais conveniente para escrever. Da mesma forma, existem várias maneiras de escrever literais de string de bytes, que resultam em `&[u8; N]`.

Geralmente, caracteres especiais são escapados com uma barra invertida: `\`. Desta forma, você pode adicionar qualquer caractere à sua string, mesmo aqueles que não podem ser impressos e aqueles que você não sabe como digitar. Se você quiser uma barra invertida literal, escape-a com outra: `\\`

Delimitadores de string ou literais de caractere que ocorrem dentro de um literal devem ser escapados: `"\""`, `'\''`.

```rust
fn main() {
    // Você pode usar escapes para escrever bytes por seus valores hexadecimais...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("O que você está fazendo\x3F (\\x3F significa ?) {}", byte_escape);

    // ...ou pontos de código Unicode.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Caractere Unicode {} (U+211D) é chamado de {}",
                unicode_codepoint, character_name );


    let long_string = "Literais de string
                        podem abranger várias linhas.
                        A quebra de linha e a indentação aqui ->\
                        <- também podem ser escapadas!";
    println!("{}", long_string);
}
```

Às vezes, há muitos caracteres que precisam ser escapados ou é muito mais conveniente escrever uma string como está. É aqui que os literais de string raw entram em jogo.

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // Se você precisar de aspas em uma string raw, adicione um par de #s
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // Se você precisar de "#" em sua string, basta usar mais #s no delimitador.
    // Você pode usar até 65535 #s.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

Quer uma string que não seja UTF-8? (Lembre-se, `str` e `String` devem ser UTF-8 válidos). Ou talvez você queira um array de bytes que seja principalmente texto? Strings de bytes para o resgate!

```rust
use std::str;

fn main() {
    // Observe que esta não é realmente uma `&str`
    let bytestring: &[u8; 21] = b"this is a byte string";

    // Arrays de bytes não têm o trait `Display`, então imprimi-los é um pouco limitado
    println!("Uma string de bytes: {:?}", bytestring);

    // Strings de bytes podem ter escapes de bytes...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    // ...mas sem escapes unicode
    // let escaped = b"\u{211D} is not allowed";
    println!("Alguns bytes escapados: {:?}", escaped);


    // Strings de bytes raw funcionam como strings raw
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // Converter um array de bytes para `str` pode falhar
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("E o mesmo como texto: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // Strings de bytes não precisam ser UTF-8
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" em SHIFT-JIS

    // Mas então elas nem sempre podem ser convertidas para `str`
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Conversão bem-sucedida: '{}'", my_str),
        Err(e) => println!("Conversão falhou: {:?}", e),
    };
}
```

Para conversões entre codificações de caracteres, consulte o crate `encoding`.

Uma listagem mais detalhada das maneiras de escrever literais de string e caracteres de escape é fornecida no capítulo 'Tokens' da Rust Reference.
