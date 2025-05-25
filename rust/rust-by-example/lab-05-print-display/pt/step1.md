# Display (Exibição)

`fmt::Debug` dificilmente parece compacto e limpo, por isso é frequentemente vantajoso personalizar a aparência da saída. Isso é feito implementando manualmente `fmt::Display`, que usa o marcador de impressão `{}`. Implementá-lo se parece com isto:

```rust
// Importe (via `use`) o módulo `fmt` para torná-lo disponível.
use std::fmt;

// Defina uma estrutura para a qual `fmt::Display` será implementado. Esta é
// uma estrutura de tupla chamada `Structure` que contém um `i32`.
struct Structure(i32);

// Para usar o marcador `{}`, o trait `fmt::Display` deve ser implementado
// manualmente para o tipo.
impl fmt::Display for Structure {
    // Este trait requer `fmt` com esta assinatura exata.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Escreva estritamente o primeiro elemento no fluxo de saída fornecido:
        // `f`. Retorna `fmt::Result` que indica se a operação foi bem-sucedida
        // ou falhou. Observe que `write!` usa uma sintaxe muito semelhante a
        // `println!`.
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` pode ser mais limpo que `fmt::Debug`, mas isso apresenta um problema para a biblioteca `std`. Como os tipos ambíguos devem ser exibidos? Por exemplo, se a biblioteca `std` implementasse um único estilo para todos os `Vec<T>`, qual estilo deveria ser? Seria um destes dois?

- `Vec<path>`: `/:/etc:/home/username:/bin` (dividido por `:`)
- `Vec<number>`: `1,2,3` (dividido por `,`)

Não, porque não existe um estilo ideal para todos os tipos e a biblioteca `std` não presume ditar um. `fmt::Display` não é implementado para `Vec<T>` ou para quaisquer outros contêineres genéricos. `fmt::Debug` deve então ser usado para esses casos genéricos.

Isso não é um problema, no entanto, porque para qualquer novo tipo de _contêiner_ que _não_ seja genérico, `fmt::Display` pode ser implementado.

```rust
use std::fmt; // Importa `fmt`

// Uma estrutura que contém dois números. `Debug` será derivado para que os resultados
// possam ser contrastados com `Display`.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implementa `Display` para `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Use `self.number` para se referir a cada ponto de dados posicional.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Define uma estrutura onde os campos são nomeáveis para comparação.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// Da mesma forma, implementa `Display` para `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Personaliza para que apenas `x` e `y` sejam denotados.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Compare structures:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("The big range is {big} and the small is {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    // Error. Both `Debug` and `Display` were implemented, but `{:b}`
    // requires `fmt::Binary` to be implemented. This will not work.
    // println!("What does Point2D look like in binary: {:b}?", point);
}
```

Portanto, `fmt::Display` foi implementado, mas `fmt::Binary` não foi, e, portanto, não pode ser usado. `std::fmt` tem muitos desses `traits` e cada um requer sua própria implementação. Isso é detalhado mais em `std::fmt`.

## Atividade

Após verificar a saída do exemplo acima, use a estrutura `Point2D` como guia para adicionar uma estrutura `Complex` ao exemplo. Quando impresso da mesma forma, a saída deve ser:

```txt
Display: 3.3 + 7.2i
Debug: Complex { real: 3.3, imag: 7.2 }
```
