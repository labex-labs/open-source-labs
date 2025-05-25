# Interpretação dos Hiperparâmetros do Kernel

Agora, podemos analisar os hiperparâmetros do kernel.

```python
gaussian_process.kernel_
```

Assim, a maior parte do sinal alvo, com a média subtraída, é explicada por uma tendência de crescimento de longo prazo de ~45 ppm e uma escala de comprimento de ~52 anos. O componente periódico tem uma amplitude de ~2,6 ppm, um tempo de decaimento de ~90 anos e uma escala de comprimento de ~1,5. O tempo de decaimento longo indica que temos um componente muito próximo a uma periodicidade sazonal. O ruído correlacionado tem uma amplitude de ~0,2 ppm com uma escala de comprimento de ~0,12 anos e uma contribuição de ruído branco de ~0,04 ppm. Portanto, o nível geral de ruído é muito baixo, indicando que os dados podem ser muito bem explicados pelo modelo.
