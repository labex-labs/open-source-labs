# Definindo um Trait para Comportamento Comum

Para implementar o comportamento que queremos que `gui` tenha, definiremos um trait chamado `Draw` que terá um método chamado `draw`. Então, podemos definir um vetor que aceita um _objeto trait_. Um objeto trait aponta tanto para uma instância de um tipo que implementa nosso trait especificado quanto para uma tabela usada para procurar métodos trait nesse tipo em tempo de execução. Criamos um objeto trait especificando algum tipo de ponteiro, como uma referência `&` ou um ponteiro inteligente `Box<T>`, em seguida, a palavra-chave `dyn` e, em seguida, especificando o trait relevante. (Falaremos sobre a razão pela qual os objetos trait devem usar um ponteiro em "Tipos de Tamanho Dinâmico e o Trait Sized".) Podemos usar objetos trait no lugar de um tipo genérico ou concreto. Onde quer que usemos um objeto trait, o sistema de tipos do Rust garantirá em tempo de compilação que qualquer valor usado nesse contexto implementará o trait do objeto trait. Consequentemente, não precisamos conhecer todos os tipos possíveis em tempo de compilação.

Mencionamos que, no Rust, nos abstemos de chamar structs e enums de "objetos" para distingui-los dos objetos de outras linguagens. Em uma struct ou enum, os dados nos campos da struct e o comportamento nos blocos `impl` são separados, enquanto em outras linguagens, os dados e o comportamento combinados em um conceito são frequentemente rotulados como um objeto. No entanto, os objetos trait _são_ mais parecidos com objetos em outras linguagens no sentido de que combinam dados e comportamento. Mas os objetos trait diferem dos objetos tradicionais porque não podemos adicionar dados a um objeto trait. Objetos trait não são tão geralmente úteis quanto objetos em outras linguagens: seu propósito específico é permitir a abstração em relação ao comportamento comum.

O Listing 17-3 mostra como definir um trait chamado `Draw` com um método chamado `draw`.

Nome do arquivo: `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Listing 17-3: Definição do trait `Draw`

Esta sintaxe deve parecer familiar de nossas discussões sobre como definir traits no Capítulo 10. Em seguida, vem alguma sintaxe nova: o Listing 17-4 define uma struct chamada `Screen` que contém um vetor chamado `components`. Este vetor é do tipo `Box<dyn Draw>`, que é um objeto trait; é um substituto para qualquer tipo dentro de um `Box` que implementa o trait `Draw`.

Nome do arquivo: `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Listing 17-4: Definição da struct `Screen` com um campo `components` contendo um vetor de objetos trait que implementam o trait `Draw`

Na struct `Screen`, definiremos um método chamado `run` que chamará o método `draw` em cada um de seus `components`, conforme mostrado no Listing 17-5.

Nome do arquivo: `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-5: Um método `run` em `Screen` que chama o método `draw` em cada componente

Isso funciona de forma diferente de definir uma struct que usa um parâmetro de tipo genérico com limites de trait. Um parâmetro de tipo genérico só pode ser substituído por um tipo concreto de cada vez, enquanto os objetos trait permitem que vários tipos concretos preencham o objeto trait em tempo de execução. Por exemplo, poderíamos ter definido a struct `Screen` usando um tipo genérico e um limite de trait, como no Listing 17-6.

Nome do arquivo: `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Listing 17-6: Uma implementação alternativa da struct `Screen` e seu método `run` usando genéricos e limites de trait

Isso nos restringe a uma instância `Screen` que tem uma lista de componentes, todos do tipo `Button` ou todos do tipo `TextField`. Se você só tiver coleções homogêneas, usar genéricos e limites de trait é preferível porque as definições serão monomorfizadas em tempo de compilação para usar os tipos concretos.

Por outro lado, com o método usando objetos trait, uma instância `Screen` pode conter um `Vec<T>` que contém um `Box<Button>`, bem como um `Box<TextField>`. Vamos ver como isso funciona e, em seguida, falaremos sobre as implicações de desempenho em tempo de execução.
