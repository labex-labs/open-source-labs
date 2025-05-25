# Definir a PDF da Distribuição Beta

A distribuição beta é uma distribuição de probabilidade contínua que é frequentemente usada para representar a distribuição de probabilidades. Na atualização bayesiana (Bayesian updating), usamos a distribuição beta como uma distribuição a priori (prior distribution) para representar nossas crenças sobre a probabilidade de uma hipótese antes de observar quaisquer dados. Em seguida, atualizamos a distribuição beta à medida que observamos novos dados.

Para simular a atualização bayesiana, precisamos definir uma função que calcula a função densidade de probabilidade (PDF, probability density function) da distribuição beta. Podemos usar a função `math.gamma` para calcular a função gama, que é usada na PDF da distribuição beta.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
