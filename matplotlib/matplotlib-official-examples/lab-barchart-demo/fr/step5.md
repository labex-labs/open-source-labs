# Définition des données pour le tracé

Nous définissons les données pour le tracé en utilisant les tuples nommés que nous avons définis précédemment. Nous créons un tuple `Student` pour Johnny Doe et un dictionnaire de tuples `Score` pour chaque test.

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
