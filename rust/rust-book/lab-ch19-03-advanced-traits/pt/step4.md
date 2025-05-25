# Desambiguação entre Métodos com o Mesmo Nome

Nada em Rust impede que uma trait tenha um método com o mesmo nome que o método de outra trait, nem impede que você implemente ambas as traits em um tipo. Também é possível implementar um método diretamente no tipo com o mesmo nome dos métodos das traits.

Ao chamar métodos com o mesmo nome, você precisará dizer ao Rust qual você deseja usar. Considere o código na Listagem 19-16, onde definimos duas traits, `Pilot` e `Wizard`, que possuem um método chamado `fly`. Em seguida, implementamos ambas as traits em um tipo `Human` que já possui um método chamado `fly` implementado nele. Cada método `fly` faz algo diferente.

Nome do arquivo: `src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

Listagem 19-16: Duas traits são definidas para ter um método `fly` e são implementadas no tipo `Human`, e um método `fly` é implementado em `Human` diretamente.

Quando chamamos `fly` em uma instância de `Human`, o compilador assume por padrão a chamada do método que é implementado diretamente no tipo, conforme mostrado na Listagem 19-17.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Listagem 19-17: Chamando `fly` em uma instância de `Human`

A execução deste código imprimirá `*waving arms furiously*`, mostrando que Rust chamou o método `fly` implementado em `Human` diretamente.

Para chamar os métodos `fly` da trait `Pilot` ou da trait `Wizard`, precisamos usar uma sintaxe mais explícita para especificar qual método `fly` queremos. A Listagem 19-18 demonstra essa sintaxe.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Listagem 19-18: Especificando qual método `fly` da trait queremos chamar

Especificar o nome da trait antes do nome do método esclarece para o Rust qual implementação de `fly` queremos chamar. Também poderíamos escrever `Human::fly(&person)`, que é equivalente a `person.fly()` que usamos na Listagem 19-18, mas isso é um pouco mais longo para escrever se não precisarmos desambiguar.

A execução deste código imprime o seguinte:

    This is your captain speaking.
    Up!
    *waving arms furiously*

Como o método `fly` recebe um parâmetro `self`, se tivéssemos dois _tipos_ que implementam uma _trait_, Rust poderia descobrir qual implementação de uma trait usar com base no tipo de `self`.

No entanto, funções associadas que não são métodos não possuem um parâmetro `self`. Quando há vários tipos ou traits que definem funções não-método com o mesmo nome de função, Rust nem sempre sabe qual tipo você quer dizer, a menos que você use a sintaxe totalmente qualificada. Por exemplo, na Listagem 19-19, criamos uma trait para um abrigo de animais que deseja nomear todos os filhotes de cachorro como Spot. Criamos uma trait `Animal` com uma função associada não-método `baby_name`. A trait `Animal` é implementada para a struct `Dog`, na qual também fornecemos uma função associada não-método `baby_name` diretamente.

Nome do arquivo: `src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

Listagem 19-19: Uma trait com uma função associada e um tipo com uma função associada do mesmo nome que também implementa a trait

Implementamos o código para nomear todos os filhotes de cachorro como Spot na função associada `baby_name` que é definida em `Dog`. O tipo `Dog` também implementa a trait `Animal`, que descreve características que todos os animais possuem. Filhotes de cachorro são chamados de filhotes, e isso é expresso na implementação da trait `Animal` em `Dog` na função `baby_name` associada à trait `Animal`.

Em `main`, chamamos a função `Dog::baby_name`, que chama a função associada definida em `Dog` diretamente. Este código imprime o seguinte:

```rust
A baby dog is called a Spot
```

Esta saída não é o que queríamos. Queremos chamar a função `baby_name` que faz parte da trait `Animal` que implementamos em `Dog` para que o código imprima `A baby dog is called a puppy`. A técnica de especificar o nome da trait que usamos na Listagem 19-18 não ajuda aqui; se mudarmos `main` para o código na Listagem 19-20, obteremos um erro de compilação.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Listagem 19-20: Tentando chamar a função `baby_name` da trait `Animal`, mas Rust não sabe qual implementação usar

Como `Animal::baby_name` não possui um parâmetro `self`, e pode haver outros tipos que implementam a trait `Animal`, Rust não consegue descobrir qual implementação de `Animal::baby_name` queremos. Obteremos este erro do compilador:

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

Para desambiguar e dizer ao Rust que queremos usar a implementação de `Animal` para `Dog`, em vez da implementação de `Animal` para algum outro tipo, precisamos usar a sintaxe totalmente qualificada. A Listagem 19-21 demonstra como usar a sintaxe totalmente qualificada.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Listagem 19-21: Usando a sintaxe totalmente qualificada para especificar que queremos chamar a função `baby_name` da trait `Animal` conforme implementada em `Dog`

Estamos fornecendo ao Rust uma anotação de tipo dentro dos colchetes angulares, o que indica que queremos chamar o método `baby_name` da trait `Animal` conforme implementado em `Dog`, dizendo que queremos tratar o tipo `Dog` como um `Animal` para esta chamada de função. Este código agora imprimirá o que queremos:

```rust
A baby dog is called a puppy
```

Em geral, a sintaxe totalmente qualificada é definida da seguinte forma:

```rust
<Type as Trait>::function(receiver_if_method, next_arg, ...);
```

Para funções associadas que não são métodos, não haveria um `receiver`: haveria apenas a lista de outros argumentos. Você pode usar a sintaxe totalmente qualificada em todos os lugares que você chama funções ou métodos. No entanto, você pode omitir qualquer parte desta sintaxe que o Rust possa descobrir a partir de outras informações no programa. Você só precisa usar esta sintaxe mais verbosa em casos em que há várias implementações que usam o mesmo nome e o Rust precisa de ajuda para identificar qual implementação você deseja chamar.
