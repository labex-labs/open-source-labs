# プロット用のデータの定義

先ほど定義した名前付きタプルを使用して、プロット用のデータを定義します。Johnny Doe の `Student` タプルと、各テストの `Score` タプルの辞書を作成します。

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
