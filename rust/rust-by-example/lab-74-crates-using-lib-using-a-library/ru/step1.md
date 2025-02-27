# Использование библиотеки

Чтобы связать коробку (`crate`) с этой новой библиотекой, вы можете использовать флаг `--extern` `rustc`. Все ее элементы будут импортированы в модуль с именем, совпадающим с именем библиотеки. Этот модуль обычно ведет себя так же, как и любой другой модуль.

```rust
// extern crate rary; // Возможно, потребуется для Rust 2015 версии или более ранних

fn main() {
    rary::public_function();

    // Ошибка! `private_function` является приватной
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# Где library.rlib - это путь к скомпилированной библиотеке, предполагается, что она
# находится в той же директории здесь:
$ rustc executable.rs --extern rary=library.rlib &&./executable
вызвана `public_function()` из rary
вызван `indirect_access()` из rary, который
> вызвал `private_function()` из rary
```
