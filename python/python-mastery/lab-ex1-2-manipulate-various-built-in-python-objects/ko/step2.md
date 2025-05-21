# Python 문자열 다루기

문자열은 Python 에서 가장 일반적으로 사용되는 데이터 타입 중 하나입니다. 문자열은 텍스트를 나타내는 데 사용되며 문자, 숫자 및 기호를 포함할 수 있습니다. 이 단계에서는 Python 에서 텍스트 데이터를 다루는 데 필수적인 기술인 다양한 문자열 연산을 살펴보겠습니다.

## 문자열 생성 및 정의

Python 에서 문자열을 사용하려면 먼저 Python 대화형 셸을 열어야 합니다. 이 셸을 사용하면 Python 코드를 한 줄씩 작성하고 실행할 수 있으며, 이는 학습 및 테스트에 매우 유용합니다. 다음 명령을 사용하여 Python 대화형 셸을 다시 엽니다.

```bash
python3
```

셸이 열리면 문자열을 정의할 수 있습니다. 이 예제에서는 주식 종목 기호가 포함된 문자열을 만들겠습니다. Python 에서 문자열은 작은따옴표 (`'`) 또는 큰따옴표 (`"`) 로 텍스트를 묶어 정의할 수 있습니다. 문자열을 정의하는 방법은 다음과 같습니다.

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

이제 `symbols`라는 문자열 변수를 만들고 값을 할당했습니다. 변수 이름을 입력하고 Enter 키를 누르면 Python 은 문자열의 값을 표시합니다.

## 문자 및 부분 문자열 접근

Python 에서 문자열은 개별 문자에 접근하기 위해 인덱싱될 수 있습니다. 인덱싱은 0 부터 시작하며, 이는 문자열의 첫 번째 문자가 인덱스 0 을 갖고, 두 번째 문자가 인덱스 1 을 갖는다는 의미입니다. 음수 인덱싱도 지원되며, -1 은 마지막 문자를, -2 는 뒤에서 두 번째 문자를 나타냅니다.

`symbols` 문자열에서 개별 문자에 어떻게 접근할 수 있는지 살펴보겠습니다.

```python
>>> symbols[0]    # 첫 번째 문자
'A'
>>> symbols[1]    # 두 번째 문자
'A'
>>> symbols[2]    # 세 번째 문자
'P'
>>> symbols[-1]   # 마지막 문자
'O'
>>> symbols[-2]   # 뒤에서 두 번째 문자
'C'
```

슬라이싱을 사용하여 부분 문자열을 추출할 수도 있습니다. 슬라이싱을 사용하면 시작 및 종료 인덱스를 지정하여 문자열의 일부를 가져올 수 있습니다. 슬라이싱 구문은 `string[start:end]`이며, 부분 문자열은 시작 인덱스부터 (포함하지 않고) 종료 인덱스까지의 문자를 포함합니다.

```python
>>> symbols[:4]    # 처음 4 개의 문자
'AAPL'
>>> symbols[-3:]   # 마지막 3 개의 문자
'SCO'
>>> symbols[5:8]   # 인덱스 5 부터 7 까지의 문자
'IBM'
```

## 문자열 불변성

Python 의 문자열은 불변 (immutable) 입니다. 즉, 문자열이 생성되면 개별 문자를 변경할 수 없습니다. 문자열의 문자를 수정하려고 하면 Python 에서 오류가 발생합니다.

`symbols` 문자열의 첫 번째 문자를 변경해 보겠습니다.

```python
>>> symbols[0] = 'a'    # 이로 인해 오류가 발생합니다.
```

다음과 같은 오류가 표시됩니다.

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

이 오류는 문자열이 불변이기 때문에 문자열의 개별 문자에 새 값을 할당할 수 없음을 나타냅니다.

## 문자열 연결

문자열을 직접 수정할 수는 없지만 연결을 통해 새 문자열을 만들 수 있습니다. 연결은 두 개 이상의 문자열을 함께 결합하는 것을 의미합니다. Python 에서는 `+` 연산자를 사용하여 문자열을 연결할 수 있습니다.

```python
>>> symbols += ' GOOG'    # 새 기호 추가
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # 새 기호 앞에 추가
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

이러한 연산은 원래 문자열을 수정하는 대신 새 문자열을 생성한다는 점을 기억하는 것이 중요합니다. 원래 문자열은 변경되지 않고 결합된 값으로 새 문자열이 생성됩니다.

## 부분 문자열 테스트

부분 문자열이 문자열 내에 존재하는지 확인하려면 `in` 연산자를 사용할 수 있습니다. `in` 연산자는 부분 문자열이 문자열에서 발견되면 `True`를 반환하고 그렇지 않으면 `False`를 반환합니다.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

'AA'가 "AAPL" 내에서 발견되었기 때문에 `True`를 반환한다는 점에 유의하십시오. 이는 더 큰 문자열 내에서 특정 텍스트를 검색하는 데 유용한 방법입니다.

## 문자열 메서드

Python 문자열에는 문자열에 대한 다양한 연산을 수행할 수 있는 수많은 내장 메서드가 있습니다. 이러한 메서드는 문자열 객체와 연결된 함수이며 점 표기법 (`string.method()`) 을 사용하여 호출할 수 있습니다.

```python
>>> symbols.lower()    # 소문자로 변환
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # 원래 문자열은 변경되지 않음
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # 결과를 새 변수에 저장
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # 부분 문자열의 시작 인덱스 찾기
13
>>> symbols[13:17]    # 해당 위치의 부분 문자열 확인
'MSFT'

>>> symbols = symbols.replace('SCO','')    # 부분 문자열 바꾸기
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

실험을 마쳤으면 다음 명령을 사용하여 Python 셸을 종료할 수 있습니다.

```python
>>> exit()
```
