# Определение данных для графика

Мы определяем данные для графика с использованием именованных кортежей (named tuples), которые мы определили ранее. Мы создаем кортеж `Student` для Джони Доу и словарь кортежей `Score` для каждого теста.

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
