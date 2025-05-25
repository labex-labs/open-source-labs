# _Ownership_ e Funções

A mecânica de passar um valor para uma função é semelhante à de atribuir um valor a uma variável. Passar uma variável para uma função irá mover ou copiar, assim como a atribuição faz. A Listagem 4-3 tem um exemplo com algumas anotações mostrando onde as variáveis entram e saem do escopo.

    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s entra em escopo

        takes_ownership(s);             // o valor de s se move para a função...
                                        // ... e, portanto, não é mais válido aqui

        let x = 5;                      // x entra em escopo

        makes_copy(x);                  // x se moveria para a função,
                                        // mas i32 é Copy, então tudo bem ainda
                                        // usar x depois

    } // Aqui, x sai do escopo, depois s. No entanto, como o valor de s foi movido,
      // nada de especial acontece

    fn takes_ownership(some_string: String) { // some_string entra em escopo
        println!("{some_string}");
    } // Aqui, some_string sai do escopo e `drop` é chamado. A memória de suporte
      // é liberada

    fn makes_copy(some_integer: i32) { // some_integer entra em escopo
        println!("{some_integer}");
    } // Aqui, some_integer sai do escopo. Nada de especial acontece

Listagem 4-3: Funções com _ownership_ e escopo anotados

Se tentássemos usar `s` após a chamada para `takes_ownership`, Rust lançaria um erro em tempo de compilação. Essas verificações estáticas nos protegem de erros. Tente adicionar código a `main` que use `s` e `x` para ver onde você pode usá-los e onde as regras de _ownership_ o impedem de fazê-lo.
