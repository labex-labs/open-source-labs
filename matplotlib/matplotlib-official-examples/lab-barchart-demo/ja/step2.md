# データの定義

名前付きタプルを使用してデータを定義します。生徒の名前、学年、性別を持つ `Student` タプルを定義します。また、スコアの値、単位、パーセンタイルを持つ `Score` タプルも定義します。

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
