# Chaînes de caractères

Il existe deux types de chaînes de caractères en Rust : `String` et `&str`.

Une `String` est stockée comme un vecteur d'octets (`Vec<u8>`), mais est garantie toujours être une séquence UTF-8 valide. `String` est allouée sur le tas, peut grandir et n'est pas terminée par un caractère nul.

`&str` est une tranche (`&[u8]`) qui pointe toujours vers une séquence UTF-8 valide, et peut être utilisée pour examiner une `String`, tout comme `&[T]` est une vue dans `Vec<T>`.

```rust
fn main() {
    // (toutes les annotations de type sont superflues)
    // Une référence à une chaîne allouée en mémoire vive en lecture seule
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram : {}", pangram);

    // Itérer sur les mots dans l'ordre inverse, aucune nouvelle chaîne n'est allouée
    println!("Mots dans l'ordre inverse");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // Copier les caractères dans un vecteur, trier et supprimer les doublons
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // Créer une `String` vide et pouvant grandir
    let mut string = String::new();
    for c in chars {
        // Insérer un caractère à la fin de la chaîne
        string.push(c);
        // Insérer une chaîne à la fin de la chaîne
        string.push_str(", ");
    }

    // La chaîne tronquée est une tranche de la chaîne d'origine, donc aucune nouvelle
    // allocation n'est effectuée
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Caractères utilisés : {}", trimmed_str);

    // Allouer une chaîne sur le tas
    let alice = String::from("I like dogs");
    // Allouer de nouvelles ressources mémoire et stocker la chaîne modifiée là
    let bob: String = alice.replace("dog", "cat");

    println!("Alice dit : {}", alice);
    println!("Bob dit : {}", bob);
}
```

Plus de méthodes `str`/`String` peuvent être trouvées dans les modules `std::str` et `std::string`.

## Littéraux et caractères d'échappement

Il existe plusieurs manières d'écrire des littéraux de chaîne de caractères avec des caractères spéciaux. Tous donnent un `&str` similaire, il est donc préférable d'utiliser la forme la plus pratique à écrire. De même, il existe plusieurs manières d'écrire des littéraux de chaîne d'octets, qui donnent tous `&[u8; N]`.

Généralement, les caractères spéciaux sont escapés avec un caractère antislash : `\`. Ainsi, vous pouvez ajouter n'importe quel caractère à votre chaîne, même des caractères non imprimables et ceux que vous ne savez pas comment taper. Si vous voulez un antislash littéral, échappez-le avec un autre : `\\`

Les délimiteurs de littéraux de chaîne ou de caractères apparaissant dans un littéral doivent être escapés : `"\""`, `'\''`.

```rust
fn main() {
    // Vous pouvez utiliser des caractères d'échappement pour écrire des octets par leurs valeurs hexadécimales...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("Que faites-vous\x3F (\\x3F signifie?) {}", byte_escape);

    //... ou des points de code Unicode.
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Le caractère Unicode {} (U+211D) s'appelle {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        can span multiple lines.
                        The linebreak and indentation here ->\
                        <- can be escaped too!";
    println!("{}", long_string);
}
```

Parfois, il y a trop de caractères à échapper ou il est simplement beaucoup plus pratique d'écrire une chaîne telle quelle. C'est là que les littéraux de chaîne brutes entrent en jeu.

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // Si vous avez besoin de guillemets dans une chaîne brute, ajoutez une paire de #
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // Si vous avez besoin de "# dans votre chaîne, utilisez simplement plus de # dans le délimiteur.
    // Vous pouvez utiliser jusqu'à 65535 #.
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

Voulez-vous une chaîne qui n'est pas UTF-8? (Rappelez-vous, `str` et `String` doivent être des séquences UTF-8 valides). Ou peut-être que vous voulez un tableau d'octets qui est surtout du texte? Les chaînes d'octets viennent en aide!

```rust
use std::str;

fn main() {
    // Notez que ce n'est pas réellement un `&str`
    let bytestring: &[u8; 21] = b"this is a byte string";

    // Les tableaux d'octets n'ont pas le trait `Display`, donc les imprimer est un peu limité
    println!("Une chaîne d'octets : {:?}", bytestring);

    // Les chaînes d'octets peuvent avoir des caractères d'échappement d'octet...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //... mais pas d'échappements Unicode
    // let escaped = b"\u{211D} is not allowed";
    println!("Certains octets escapés : {:?}", escaped);


    // Les chaînes d'octets brutes fonctionnent comme les chaînes brutes
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // Convertir un tableau d'octets en `str` peut échouer
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("Et le même en tant que texte : '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // Les chaînes d'octets ne doivent pas être UTF-8
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" en SHIFT-JIS

    // Mais alors elles ne peuvent pas toujours être converties en `str`
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Conversion réussie : '{}'", my_str),
        Err(e) => println!("Conversion échouée : {:?}", e),
    };
}
```

Pour les conversions entre les encodages de caractères, consultez la boîte à outils `encoding`.

Une liste plus détaillée des manières d'écrire des littéraux de chaîne de caractères et des caractères d'échappement est donnée dans le chapitre 'Tokens' de la Rust Reference.
