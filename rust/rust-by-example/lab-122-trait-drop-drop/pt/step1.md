# Drop

O trait `Drop` possui apenas um método: `drop`, que é chamado automaticamente quando um objeto sai do escopo. O principal uso do trait `Drop` é liberar os recursos que a instância implementadora possui.

`Box`, `Vec`, `String`, `File` e `Process` são alguns exemplos de tipos que implementam o trait `Drop` para liberar recursos. O trait `Drop` também pode ser implementado manualmente para qualquer tipo de dado personalizado.

O exemplo a seguir adiciona uma impressão no console à função `drop` para anunciar quando ela é chamada.

```rust
struct Droppable {
    name: &'static str,
}

// This trivial implementation of `drop` adds a print to console.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // block A
    {
        let _b = Droppable { name: "b" };

        // block B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // Variable can be manually dropped using the `drop` function
    drop(_a);
    // TODO ^ Try commenting this line

    println!("end of the main function");

    // `_a` *won't* be `drop`ed again here, because it already has been
    // (manually) `drop`ed
}
```
