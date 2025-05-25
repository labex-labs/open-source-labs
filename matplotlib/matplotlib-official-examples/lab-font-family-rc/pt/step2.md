# Escolha de uma Fonte Sans-Serif Específica

Se quisermos usar uma fonte sans-serif específica, podemos definir o parâmetro `font.sans-serif` como uma lista de nomes de fontes. O Matplotlib tentará usar a primeira fonte na lista que estiver disponível no sistema do usuário. Para fazer isso, podemos usar o seguinte código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```
