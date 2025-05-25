# Formatação Simples

Nesta etapa, mostraremos como usar um formatador simples, passando uma string ou função para `~.Axis.set_major_formatter` ou `~.Axis.set_minor_formatter`. Criaremos dois gráficos, um usando um formatador de string e o outro usando um formatador de função.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Simple Formatting')

# A ``str``, usando a sintaxe da função de string de formatação, pode ser usada diretamente como um
# formatador. A variável ``x`` é o valor do tick e a variável ``pos`` é a
# posição do tick. Isso cria um StrMethodFormatter automaticamente.
setup(axs0[0], title="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# Uma função também pode ser usada diretamente como um formatador. A função deve receber
# dois argumentos: ``x`` para o valor do tick e ``pos`` para a posição do tick,
# e deve retornar uma ``str``. Isso cria um FuncFormatter automaticamente.
setup(axs0[1], title="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```
