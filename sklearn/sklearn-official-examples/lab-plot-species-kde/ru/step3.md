# Подготовить данные

Теперь мы подготовим данные для оценки плотности ядра. Мы извлечем информацию о широте и долготе из набора данных и преобразуем их в радианы.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # Convert lat/long to radians
```
