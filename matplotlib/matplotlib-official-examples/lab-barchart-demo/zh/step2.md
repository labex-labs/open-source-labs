# 定义数据

我们使用具名元组来定义数据。我们定义了一个 `Student` 元组，包含学生的姓名、年级和性别。我们还定义了一个 `Score` 元组，包含分数值、单位和百分位数。

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
