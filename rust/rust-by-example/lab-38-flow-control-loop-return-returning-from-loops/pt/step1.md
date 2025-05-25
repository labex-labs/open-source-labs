# Retornando de loops

Um dos usos de um `loop` é tentar uma operação até que ela tenha sucesso. No entanto, se a operação retornar um valor, você pode precisar passá-lo para o restante do código: coloque-o após o `break`, e ele será retornado pela expressão `loop`.

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
