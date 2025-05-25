# Criar o Diagrama de Ishikawa (Fishbone Diagram)

Agora criaremos o diagrama de Ishikawa (Fishbone Diagram). Começaremos criando um objeto de figura e eixo.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Em seguida, definiremos os limites x e y para o eixo e desativaremos o eixo.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
