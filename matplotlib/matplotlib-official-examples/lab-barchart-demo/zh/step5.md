# 定义绘图数据

我们使用之前定义的具名元组来定义绘图数据。我们为约翰尼·多伊创建一个 `Student` 元组，并为每个测试创建一个 `Score` 元组的字典。

```python
student = Student(name='Johnny Doe', grade=2, gender='Boy')
scores_by_test = {
    'Pacer Test': Score(7, 'laps', percentile=37),
    'Flexed Arm\n Hang': Score(48,'sec', percentile=95),
    'Mile Run': Score('12:52','min:sec', percentile=73),
    'Agility': Score(17,'sec', percentile=60),
    'Push Ups': Score(14, '', percentile=16),
}
```
