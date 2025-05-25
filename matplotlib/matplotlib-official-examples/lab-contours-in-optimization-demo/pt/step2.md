# Configurar os Vetores e Matrizes de Levantamento

Em seguida, configure os vetores e matrizes de levantamento. Projete a carga do disco e a relação de engrenagem.

```python
nx = 101
ny = 105

# Set up survey vectors
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)
```
