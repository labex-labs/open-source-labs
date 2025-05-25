# Anexando a uma String com push_str e push

Podemos aumentar uma `String` usando o método `push_str` para anexar uma fatia de string (string slice), como mostrado na Listagem 8-15.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Listagem 8-15: Anexando uma fatia de string a uma `String` usando o método `push_str`

Após estas duas linhas, `s` conterá `foobar`. O método `push_str` recebe uma fatia de string porque não queremos necessariamente assumir a propriedade do parâmetro. Por exemplo, no código na Listagem 8-16, queremos ser capazes de usar `s2` após anexar seu conteúdo a `s1`.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

Listagem 8-16: Usando uma fatia de string após anexar seu conteúdo a uma `String`

Se o método `push_str` assumisse a propriedade de `s2`, não seríamos capazes de imprimir seu valor na última linha. No entanto, este código funciona como esperaríamos!

O método `push` recebe um único caractere como parâmetro e o adiciona à `String`. A Listagem 8-17 adiciona a letra _l_ a uma `String` usando o método `push`.

```rust
let mut s = String::from("lo");
s.push('l');
```

Listagem 8-17: Adicionando um caractere a um valor `String` usando `push`

Como resultado, `s` conterá `lol`.
