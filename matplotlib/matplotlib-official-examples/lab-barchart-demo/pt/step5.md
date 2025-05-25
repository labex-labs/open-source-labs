# Definir os Dados para o Gráfico

Definimos os dados para o gráfico usando as tuplas nomeadas que definimos anteriormente. Criamos uma tupla `Student` para Johnny Doe e um dicionário de tuplas `Score` para cada teste.

```python
student = Student(name='Johnny Doe', grade=2, gender='Boy')
scores_by_test = {
    'Pacer Test': Score(7, 'laps', percentile=37),
    'Flexed Arm\n Hang': Score(48, 'sec', percentile=95),
    'Mile Run': Score('12:52', 'min:sec', percentile=73),
    'Agility': Score(17, 'sec', percentile=60),
    'Push Ups': Score(14, '', percentile=16),
}
```
