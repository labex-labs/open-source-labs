# Gerar Dados Aleatórios

Nesta etapa, você gerará dados aleatórios para a habilidade do lançador, ângulo de lançamento (take-off angle), impulso (thrust), sucesso e posição. Especificamente, você gerará 25 pontos de dados para cada variável, exceto para a posição, que terá 2 coordenadas para cada ponto de dados.

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```
