# 가장 긴 이름 찾기

타이타닉호 승객 중 가장 긴 이름을 가진 승객이 누구인지 알아봅시다. `str.len()` 메서드를 사용하여 각 이름의 길이를 구하고, `idxmax()` 메서드를 사용하여 가장 긴 이름의 인덱스를 찾습니다.

```python
# Get the length of each name
name_lengths = titanic["Name"].str.len()

# Find the index of the longest name
longest_name_index = name_lengths.idxmax()

# Get the longest name
longest_name = titanic.loc[longest_name_index, "Name"]
```
