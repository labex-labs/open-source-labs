# Chamando uma Função ou Método Unsafe

O segundo tipo de operação que você pode realizar em um bloco unsafe é chamar funções unsafe. Funções e métodos unsafe se parecem exatamente com funções e métodos regulares, mas eles têm um `unsafe` extra antes do restante da definição. A palavra-chave `unsafe` neste contexto indica que a função tem requisitos que precisamos cumprir quando chamamos essa função, porque o Rust não pode garantir que tenhamos atendido a esses requisitos. Ao chamar uma função unsafe dentro de um bloco `unsafe`, estamos dizendo que lemos a documentação desta função e assumimos a responsabilidade de cumprir os contratos da função.

Aqui está uma função unsafe chamada `dangerous` que não faz nada em seu corpo:

    unsafe fn dangerous() {}

    unsafe {
        dangerous();
    }

Devemos chamar a função `dangerous` dentro de um bloco `unsafe` separado. Se tentarmos chamar `dangerous` sem o bloco `unsafe`, obteremos um erro:

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

Com o bloco `unsafe`, estamos afirmando ao Rust que lemos a documentação da função, entendemos como usá-la corretamente e verificamos se estamos cumprindo o contrato da função.

Os corpos das funções unsafe são efetivamente blocos `unsafe`, então, para realizar outras operações unsafe dentro de uma função unsafe, não precisamos adicionar outro bloco `unsafe`.
