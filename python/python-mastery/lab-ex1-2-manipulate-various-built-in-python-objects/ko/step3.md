# Python 리스트 다루기

리스트는 Python 의 데이터 구조 유형입니다. 데이터 구조는 데이터를 효율적으로 사용할 수 있도록 데이터를 구성하고 저장하는 방법입니다. 리스트는 숫자, 문자열 또는 다른 리스트와 같이 다양한 유형의 항목을 저장할 수 있으므로 매우 다재다능합니다. 이 단계에서는 리스트에 대한 다양한 연산을 수행하는 방법을 배우겠습니다.

## 문자열에서 리스트 생성

Python 리스트를 사용하려면 먼저 Python 대화형 세션을 열어야 합니다. 이것은 Python 코드를 즉시 작성하고 실행할 수 있는 특별한 환경과 같습니다. 이 세션을 시작하려면 터미널에 다음 명령을 입력하십시오.

```bash
python3
```

Python 대화형 세션에 들어가면 문자열에서 리스트를 만들 것입니다. 문자열은 단순히 일련의 문자입니다. 공백으로 구분된 일부 주식 기호를 포함하는 문자열을 정의합니다. 그런 다음 이 문자열을 리스트로 변환합니다. 각 주식 기호는 리스트의 요소가 됩니다.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # 공백을 기준으로 문자열 분할
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

`split()` 메서드는 공백이 있는 모든 위치에서 문자열을 부분으로 나누는 데 사용됩니다. 각 부분은 새 리스트의 요소가 됩니다.

## 리스트 요소 접근 및 수정

문자열과 마찬가지로 리스트는 인덱싱을 지원합니다. 인덱싱은 리스트의 개별 요소에 해당 위치별로 접근할 수 있음을 의미합니다. Python 에서 리스트의 첫 번째 요소는 인덱스 0 을 갖고, 두 번째 요소는 인덱스 1 을 갖는 식입니다. 음수 인덱싱을 사용하여 리스트의 끝에서 요소를 접근할 수도 있습니다. 마지막 요소는 인덱스 -1 을 갖고, 뒤에서 두 번째 요소는 인덱스 -2 를 갖는 식입니다.

문자열과 달리 리스트 요소는 수정할 수 있습니다. 즉, 리스트의 요소 값을 변경할 수 있습니다.

```python
>>> symlist[0]    # 첫 번째 요소
'HPQ'
>>> symlist[1]    # 두 번째 요소
'AAPL'
>>> symlist[-1]   # 마지막 요소
'GOOG'
>>> symlist[-2]   # 뒤에서 두 번째 요소
'YHOO'

>>> symlist[2] = 'AIG'    # 세 번째 요소 바꾸기
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## 리스트 반복

종종 리스트의 각 요소에 대해 동일한 연산을 수행해야 합니다. `for` 루프를 사용하여 이 작업을 수행할 수 있습니다. `for` 루프를 사용하면 리스트의 각 요소를 하나씩 거쳐 특정 작업을 수행할 수 있습니다.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

이 코드를 실행하면 `s =` 레이블과 함께 리스트의 각 요소가 출력되는 것을 볼 수 있습니다.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## 멤버십 확인

때로는 특정 항목이 리스트에 존재하는지 확인해야 합니다. `in` 연산자를 사용하여 이 작업을 수행할 수 있습니다. `in` 연산자는 항목이 리스트에 있으면 `True`를 반환하고 그렇지 않으면 `False`를 반환합니다.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## 요소 추가 및 제거

리스트에는 요소를 추가하고 제거할 수 있는 내장 메서드가 있습니다. `append()` 메서드는 리스트의 끝에 요소를 추가합니다. `insert()` 메서드는 리스트의 특정 위치에 요소를 삽입합니다. `remove()` 메서드는 값으로 리스트에서 요소를 제거합니다.

```python
>>> symlist.append('RHT')    # 끝에 요소 추가
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # 특정 위치에 삽입
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # 값으로 제거
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

리스트에 존재하지 않는 요소를 제거하려고 하면 Python 에서 오류가 발생합니다.

```python
>>> symlist.remove('MSFT')
```

다음과 같은 오류 메시지가 표시됩니다.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

`index()` 메서드를 사용하여 리스트에서 요소의 위치를 찾을 수도 있습니다.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # 해당 위치의 요소 확인
'YHOO'
```

## 리스트 정렬

리스트는 제자리에서 정렬될 수 있습니다. 즉, 원래 리스트가 수정됩니다. 리스트를 알파벳순 또는 역순으로 정렬할 수 있습니다.

```python
>>> symlist.sort()    # 알파벳순으로 정렬
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # 역순으로 정렬
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## 중첩 리스트

리스트는 다른 리스트를 포함하여 모든 유형의 객체를 포함할 수 있습니다. 이것을 중첩 리스트라고 합니다.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

중첩 리스트의 요소에 접근하려면 여러 인덱스를 사용합니다. 첫 번째 인덱스는 외부 리스트 요소를 선택하고, 두 번째 인덱스는 내부 리스트 요소를 선택합니다.

```python
>>> items[0]    # 첫 번째 요소 (symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # symlist 의 두 번째 요소
'RHT'
>>> items[0][1][2]    # 'RHT'의 세 번째 문자
'T'
>>> items[1]    # 두 번째 요소 (nums 리스트)
[101, 102, 103]
>>> items[1][1]    # nums 의 두 번째 요소
102
```

Python 대화형 세션에서 작업을 마쳤으면 다음을 입력하여 종료할 수 있습니다.

```python
>>> exit()
```
