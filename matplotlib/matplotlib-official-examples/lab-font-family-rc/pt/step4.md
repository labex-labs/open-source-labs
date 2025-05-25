# Escolha de uma Fonte Monospace Específica

Se quisermos usar uma fonte monospace específica, podemos definir o parâmetro `font.monospace` como uma lista de nomes de fontes. O Matplotlib tentará usar a primeira fonte na lista que estiver disponível no sistema do usuário. Para fazer isso, podemos usar o seguinte código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```
