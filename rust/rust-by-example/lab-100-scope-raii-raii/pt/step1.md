# RAII

Variáveis em Rust fazem mais do que apenas armazenar dados na pilha (stack): elas também _possuem_ recursos, por exemplo, `Box<T>` possui memória no heap. Rust impõe RAII (Resource Acquisition Is Initialization), então sempre que um objeto sai do escopo, seu destrutor é chamado e seus recursos próprios são liberados.

Este comportamento protege contra _vazamentos de recursos_ (resource leak bugs), então você nunca mais precisará liberar memória manualmente ou se preocupar com vazamentos de memória! Aqui está uma demonstração rápida:

```rust
// raii.rs
fn create_box() {
    // Aloca um inteiro no heap
    let _box1 = Box::new(3i32);

    // `_box1` é destruído aqui, e a memória é liberada
}

fn main() {
    // Aloca um inteiro no heap
    let _box2 = Box::new(5i32);

    // Um escopo aninhado:
    {
        // Aloca um inteiro no heap
        let _box3 = Box::new(4i32);

        // `_box3` é destruído aqui, e a memória é liberada
    }

    // Criando muitas caixas só por diversão
    // Não há necessidade de liberar memória manualmente!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` é destruído aqui, e a memória é liberada
}
```

Claro, podemos verificar novamente se há erros de memória usando `valgrind`:

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc raii.rs && valgrind ./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command: ./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

Sem vazamentos aqui!

## Destrutor

A noção de um destrutor em Rust é fornecida através do trait \[`Drop`]. O destrutor é chamado quando o recurso sai do escopo. Este trait não precisa ser implementado para cada tipo, implemente-o apenas para seu tipo se você precisar de sua própria lógica de destrutor.

Execute o exemplo abaixo para ver como o trait \[`Drop`\] funciona. Quando a variável na função `main` sai do escopo, o destrutor personalizado será invocado.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop is being dropped");
    }
}

fn main() {
    let x = ToDrop;
    println!("Made a ToDrop!");
}
```
