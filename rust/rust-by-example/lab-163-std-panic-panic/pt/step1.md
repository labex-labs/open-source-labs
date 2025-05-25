# `panic!`

O macro `panic!` pode ser usado para gerar um erro (`panic`) e iniciar o desempilhamento da sua pilha. Durante o desempilhamento, o tempo de execução cuidará de liberar todos os recursos _possuídos_ pela thread, chamando o destrutor de todos os seus objetos.

Como estamos a lidar com programas com apenas uma thread, `panic!` fará com que o programa reporte a mensagem de erro e termine.

```rust
// Reimplementação da divisão de inteiros (/)
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // Divisão por zero dispara um erro
        panic!("divisão por zero");
    } else {
        dividend / divisor
    }
}

// A tarefa `main`
fn main() {
    // Inteiro alocado no heap
    let _x = Box::new(0i32);

    // Esta operação irá disparar uma falha na tarefa
    division(3, 0);

    println!("Este ponto não será atingido!");

    // `_x` deverá ser destruído neste ponto
}
```

Vamos verificar se `panic!` não causa vazamentos de memória.

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
```

```shell
$ rustc panic.rs && valgrind ./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command: ./panic
==4401==
thread '<main>' panicked at 'division by zero', panic.rs:5
==4401==
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401==
==4401== All heap blocks were freed -- no leaks are possible
==4401==
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
