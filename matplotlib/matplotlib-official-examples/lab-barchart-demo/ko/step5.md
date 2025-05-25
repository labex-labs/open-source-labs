# 플롯을 위한 데이터 정의

앞서 정의한 명명된 튜플을 사용하여 플롯에 대한 데이터를 정의합니다. Johnny Doe 에 대한 `Student` 튜플과 각 테스트에 대한 `Score` 튜플의 딕셔너리를 생성합니다.

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
