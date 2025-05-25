# Adicionar uma nova coluna para o mês da medição

Agora, queremos adicionar uma nova coluna ao nosso DataFrame que contenha apenas o mês de cada medição. Isso pode ser alcançado usando o acessador `dt`.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
