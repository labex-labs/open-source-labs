# Preparar Dados

Agora, prepararemos os dados para a estimativa de densidade de kernel. Extrairemos as informações de latitude e longitude do conjunto de dados e as convertemos para radianos.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Converter lat/long para radianos
```
