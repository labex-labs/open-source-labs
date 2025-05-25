# Aninhamento e rótulos

É possível usar `break` ou `continue` em loops externos quando lidando com loops aninhados. Nestes casos, os loops devem ser anotados com algum `'rótulo`, e o rótulo deve ser passado para a instrução `break`/`continue`.

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("Entrou no loop externo");

        'inner: loop {
            println!("Entrou no loop interno");

            // Isso apenas interromperia o loop interno
            //break;

            // Isso interrompe o loop externo
            break 'outer;
        }

        println!("Este ponto nunca será alcançado");
    }

    println!("Saiu do loop externo");
}
```
