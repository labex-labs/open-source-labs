# Desreferenciando um Ponteiro Bruto (Raw Pointer)

Em "Referências Pendentes (Dangling References)", mencionamos que o compilador garante que as referências sejam sempre válidas. O Unsafe Rust tem dois novos tipos chamados _ponteiros brutos_ (raw pointers) que são semelhantes às referências. Assim como com as referências, os ponteiros brutos podem ser imutáveis ou mutáveis e são escritos como `*const T` e `*mut T`, respectivamente. O asterisco não é o operador de desreferenciação; faz parte do nome do tipo. No contexto de ponteiros brutos, _imutável_ significa que o ponteiro não pode ser diretamente atribuído após ser desreferenciado.

Diferente das referências e ponteiros inteligentes (smart pointers), os ponteiros brutos:

- Podem ignorar as regras de empréstimo (borrowing rules) por terem ponteiros imutáveis e mutáveis ou múltiplos ponteiros mutáveis para o mesmo local
- Não têm garantia de apontar para memória válida
- Podem ser nulos
- Não implementam nenhuma limpeza automática

Ao optar por não ter o Rust impor essas garantias, você pode abrir mão da segurança garantida em troca de maior desempenho ou da capacidade de interagir com outra linguagem ou hardware onde as garantias do Rust não se aplicam.

A Listagem 19-1 mostra como criar um ponteiro bruto imutável e um mutável a partir de referências.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;
```

Listagem 19-1: Criando ponteiros brutos a partir de referências

Observe que não incluímos a palavra-chave `unsafe` neste código. Podemos criar ponteiros brutos em código seguro; simplesmente não podemos desreferenciar ponteiros brutos fora de um bloco unsafe, como você verá em breve.

Criamos ponteiros brutos usando `as` para converter uma referência imutável e uma mutável em seus tipos de ponteiro bruto correspondentes. Como os criamos diretamente de referências garantidas como válidas, sabemos que esses ponteiros brutos específicos são válidos, mas não podemos fazer essa suposição sobre qualquer ponteiro bruto.

Para demonstrar isso, em seguida, criaremos um ponteiro bruto cuja validade não podemos ter tanta certeza. A Listagem 19-2 mostra como criar um ponteiro bruto para um local arbitrário na memória. Tentar usar memória arbitrária é indefinido: pode haver dados naquele endereço ou pode não haver, o compilador pode otimizar o código para que não haja acesso à memória, ou o programa pode terminar com uma falha de segmentação. Normalmente, não há uma boa razão para escrever código como este, mas é possível.

```rust
let address = 0x012345usize;
let r = address as *const i32;
```

Listagem 19-2: Criando um ponteiro bruto para um endereço de memória arbitrário

Lembre-se de que podemos criar ponteiros brutos em código seguro, mas não podemos _desreferenciar_ ponteiros brutos e ler os dados aos quais eles apontam. Na Listagem 19-3, usamos o operador de desreferenciação `*` em um ponteiro bruto que requer um bloco `unsafe`.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

Listagem 19-3: Desreferenciando ponteiros brutos dentro de um bloco `unsafe`

Criar um ponteiro não causa nenhum dano; é somente quando tentamos acessar o valor ao qual ele aponta que podemos acabar lidando com um valor inválido.

Observe também que nas Listagens 19-1 e 19-3, criamos ponteiros brutos `*const i32` e `*mut i32` que apontavam para o mesmo local de memória, onde `num` é armazenado. Se, em vez disso, tentássemos criar uma referência imutável e uma mutável para `num`, o código não teria compilado porque as regras de propriedade do Rust não permitem uma referência mutável ao mesmo tempo que quaisquer referências imutáveis. Com ponteiros brutos, podemos criar um ponteiro mutável e um ponteiro imutável para o mesmo local e alterar dados por meio do ponteiro mutável, potencialmente criando uma condição de corrida de dados (data race). Tenha cuidado!

Com todos esses perigos, por que você usaria ponteiros brutos? Um caso de uso importante é ao interagir com código C, como você verá em "Chamando uma Função ou Método Unsafe". Outro caso é ao construir abstrações seguras que o verificador de empréstimos não entende. Apresentaremos funções unsafe e, em seguida, analisaremos um exemplo de uma abstração segura que usa código unsafe.
