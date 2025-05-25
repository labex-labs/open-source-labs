# Introdução

Neste laboratório, o conceito de coerção (coercion) em Rust é explorado, onde um tempo de vida (lifetime) mais longo pode ser coerido para um mais curto para habilitar funcionalidades dentro de um escopo específico. Isso pode ocorrer por meio de coerção inferida pelo compilador Rust ou pela declaração de uma diferença de tempo de vida usando sintaxe como `<'a: 'b, 'b>`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
