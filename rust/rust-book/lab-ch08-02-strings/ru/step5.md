# Добавление в строку с помощью push_str и push

Мы можем увеличивать `String`, используя метод `push_str` для добавления строкового среза, как показано в Listing 8-15.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Listing 8-15: Добавление строкового среза к `String` с использованием метода `push_str`

После этих двух строк `s` будет содержать `foobar`. Метод `push_str` принимает строковый срез, потому что мы не обязательно хотим взять владение параметром. Например, в коде в Listing 8-16 мы хотим иметь возможность использовать `s2` после добавления его содержимого в `s1`.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

Listing 8-16: Использование строкового среза после добавления его содержимого в `String`

Если метод `push_str` принял владение `s2`, мы не смогли бы вывести его значение на последней строке. Однако этот код работает, как мы ожидаем!

Метод `push` принимает один символ в качестве параметра и добавляет его в `String`. Listing 8-17 добавляет букву _l_ в `String` с использованием метода `push`.

```rust
let mut s = String::from("lo");
s.push('l');
```

Listing 8-17: Добавление одного символа к значению `String` с использованием `push`

В результате `s` будет содержать `lol`.
