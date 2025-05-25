# Criando uma Abstração Segura sobre Código Unsafe

Só porque uma função contém código unsafe não significa que precisamos marcar a função inteira como unsafe. Na verdade, encapsular código unsafe em uma função segura é uma abstração comum. Como exemplo, vamos estudar a função `split_at_mut` da biblioteca padrão, que requer algum código unsafe. Vamos explorar como podemos implementá-la. Este método seguro é definido em fatias mutáveis: ele pega uma fatia e a transforma em duas, dividindo a fatia no índice fornecido como argumento. A Listagem 19-4 mostra como usar `split_at_mut`.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

Listagem 19-4: Usando a função segura `split_at_mut`

Não podemos implementar esta função usando apenas Rust seguro. Uma tentativa pode se parecer com a Listagem 19-5, que não compilará. Para simplificar, implementaremos `split_at_mut` como uma função em vez de um método e apenas para fatias de valores `i32`, em vez de para um tipo genérico `T`.

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

Listagem 19-5: Uma tentativa de implementação de `split_at_mut` usando apenas Rust seguro

Esta função primeiro obtém o comprimento total da fatia. Em seguida, ela afirma que o índice fornecido como um parâmetro está dentro da fatia, verificando se ele é menor ou igual ao comprimento. A afirmação significa que, se passarmos um índice que é maior que o comprimento para dividir a fatia, a função entrará em pânico antes de tentar usar esse índice.

Então, retornamos duas fatias mutáveis em uma tupla: uma do início da fatia original até o índice `mid` e outra de `mid` até o final da fatia.

Quando tentamos compilar o código na Listagem 19-5, obteremos um erro:

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

O verificador de empréstimos (borrow checker) do Rust não consegue entender que estamos emprestando diferentes partes da fatia; ele só sabe que estamos emprestando da mesma fatia duas vezes. Emprestar diferentes partes de uma fatia é fundamentalmente aceitável porque as duas fatias não se sobrepõem, mas o Rust não é inteligente o suficiente para saber disso. Quando sabemos que o código está correto, mas o Rust não sabe, é hora de recorrer ao código unsafe.

A Listagem 19-6 mostra como usar um bloco `unsafe`, um ponteiro bruto e algumas chamadas para funções unsafe para fazer a implementação de `split_at_mut` funcionar.

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

Listagem 19-6: Usando código unsafe na implementação da função `split_at_mut`

Lembre-se de "O Tipo Slice" que uma fatia é um ponteiro para alguns dados e o comprimento da fatia. Usamos o método `len` para obter o comprimento de uma fatia \[1] e o método `as_mut_ptr` para acessar o ponteiro bruto de uma fatia \[2]. Neste caso, como temos uma fatia mutável para valores `i32`, `as_mut_ptr` retorna um ponteiro bruto com o tipo `*mut i32`, que armazenamos na variável `ptr`.

Mantemos a afirmação de que o índice `mid` está dentro da fatia \[3]. Então, chegamos ao código unsafe \[4]: a função `slice::from_raw_parts_mut` recebe um ponteiro bruto e um comprimento, e cria uma fatia. Usamos isso para criar uma fatia que começa de `ptr` e tem `mid` itens de comprimento \[5]. Em seguida, chamamos o método `add` em `ptr` com `mid` como um argumento para obter um ponteiro bruto que começa em `mid`, e criamos uma fatia usando esse ponteiro e o número restante de itens após `mid` como o comprimento \[6].

A função `slice::from_raw_parts_mut` é unsafe porque recebe um ponteiro bruto e deve confiar que este ponteiro é válido. O método `add` em ponteiros brutos também é unsafe porque deve confiar que o local de deslocamento também é um ponteiro válido. Portanto, tivemos que colocar um bloco `unsafe` em torno de nossas chamadas para `slice::from_raw_parts_mut` e `add` para que pudéssemos chamá-los. Ao olhar para o código e adicionar a afirmação de que `mid` deve ser menor ou igual a `len`, podemos dizer que todos os ponteiros brutos usados dentro do bloco `unsafe` serão ponteiros válidos para dados dentro da fatia. Este é um uso aceitável e apropriado de `unsafe`.

Observe que não precisamos marcar a função `split_at_mut` resultante como `unsafe`, e podemos chamar esta função do Rust seguro. Criamos uma abstração segura para o código unsafe com uma implementação da função que usa código `unsafe` de uma maneira segura, porque ela cria apenas ponteiros válidos a partir dos dados que esta função tem acesso.

Em contraste, o uso de `slice::from_raw_parts_mut` na Listagem 19-7 provavelmente travará quando a fatia for usada. Este código pega um local de memória arbitrário e cria uma fatia com 10.000 itens de comprimento.

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

Listagem 19-7: Criando uma fatia a partir de um local de memória arbitrário

Não somos proprietários da memória neste local arbitrário, e não há garantia de que a fatia que este código cria contenha valores `i32` válidos. Tentar usar `values` como se fosse uma fatia válida resulta em comportamento indefinido.
