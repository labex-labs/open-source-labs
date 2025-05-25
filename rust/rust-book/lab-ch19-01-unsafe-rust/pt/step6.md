# Usando Funções `extern` para Chamar Código Externo

Às vezes, seu código Rust pode precisar interagir com código escrito em outra linguagem. Para isso, o Rust tem a palavra-chave `extern` que facilita a criação e o uso de uma _Interface de Função Estrangeira_ _(FFI)_, que é uma maneira de uma linguagem de programação definir funções e permitir que uma linguagem de programação diferente (estrangeira) chame essas funções.

A Listagem 19-8 demonstra como configurar uma integração com a função `abs` da biblioteca padrão C. Funções declaradas dentro de blocos `extern` são sempre unsafe para serem chamadas a partir do código Rust. A razão é que outras linguagens não impõem as regras e garantias do Rust, e o Rust não pode verificá-las, então a responsabilidade recai sobre o programador para garantir a segurança.

Nome do arquivo: `src/main.rs`

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!(
            "Valor absoluto de -3 de acordo com C: {}",
            abs(-3)
        );
    }
}
```

Listagem 19-8: Declarando e chamando uma função `extern` definida em outra linguagem

Dentro do bloco `extern "C"`, listamos os nomes e assinaturas de funções externas de outra linguagem que queremos chamar. A parte `"C"` define qual _Interface Binária de Aplicação_ _(ABI)_ a função externa usa: a ABI define como chamar a função no nível da assembly. A ABI `"C"` é a mais comum e segue a ABI da linguagem de programação C.

> **Chamando Funções Rust de Outras Linguagens**
>
> Também podemos usar `extern` para criar uma interface que permite que outras linguagens chamem funções Rust. Em vez de criar um bloco `extern` inteiro, adicionamos a palavra-chave `extern` e especificamos a ABI a ser usada logo antes da palavra-chave `fn` para a função relevante. Também precisamos adicionar uma anotação `#[no_mangle]` para dizer ao compilador Rust para não "mutilar" o nome desta função. _Mutilar_ (Mangling) é quando um compilador altera o nome que demos a uma função para um nome diferente que contém mais informações para outras partes do processo de compilação consumirem, mas é menos legível para humanos. Cada compilador de linguagem de programação mutila os nomes de forma ligeiramente diferente, então, para que uma função Rust possa ser nomeada por outras linguagens, devemos desabilitar a mutilação de nomes do compilador Rust.
>
> No exemplo a seguir, tornamos a função `call_from_c` acessível a partir do código C, depois que ela é compilada para uma biblioteca compartilhada e vinculada a partir de C:
>
>     #[no_mangle]
>     pub extern "C" fn call_from_c() {
>         println!("Acabei de chamar uma função Rust de C!");
>     }
>
> Este uso de `extern` não requer `unsafe`.
