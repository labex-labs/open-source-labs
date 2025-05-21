# Python 의 메모리 모델 탐구

Python 의 메모리 모델은 객체가 메모리에 저장되는 방식과 참조되는 방식을 결정하는 데 중요한 역할을 합니다. 특히 대규모 데이터 세트를 처리할 때는 이 모델을 이해하는 것이 필수적입니다. 이는 Python 프로그램의 성능과 메모리 사용량에 큰 영향을 미칠 수 있기 때문입니다. 이 단계에서는 Python 에서 문자열 객체가 처리되는 방식에 중점을 두고 대규모 데이터 세트의 메모리 사용량을 최적화하는 방법을 살펴보겠습니다.

## 데이터 세트의 문자열 반복

CTA 버스 데이터에는 노선 이름과 같이 반복되는 값이 많이 포함되어 있습니다. 데이터 세트의 반복되는 값은 적절하게 처리하지 않으면 비효율적인 메모리 사용으로 이어질 수 있습니다. 이 문제의 정도를 이해하기 위해 먼저 데이터 세트에 고유한 노선 문자열이 몇 개나 있는지 살펴보겠습니다.

먼저, Python 인터프리터를 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
python3
```

Python 인터프리터가 열리면 CTA 버스 데이터를 로드하고 고유한 노선을 찾습니다. 다음은 이를 수행하는 코드입니다.

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

이 코드에서는 먼저 CSV 파일을 딕셔너리로 읽는 함수가 포함되어 있을 것으로 예상되는 `reader` 모듈을 가져옵니다. 그런 다음 `read_csv_as_dicts` 함수를 사용하여 `ctabus.csv` 파일에서 데이터를 로드합니다. 두 번째 인수 `[str, str, str, int]`는 CSV 파일의 각 열에 대한 데이터 타입을 지정합니다. 그 후, 집합 컴프리헨션을 사용하여 데이터 세트의 모든 고유한 노선 이름을 찾고 고유한 노선 이름의 수를 출력합니다.

출력은 다음과 같아야 합니다.

```
Number of unique route names: 181
```

이제 이러한 노선에 대해 몇 개의 서로 다른 문자열 객체가 생성되는지 확인해 보겠습니다. 고유한 노선 이름이 181 개뿐이지만, Python 은 데이터 세트에서 노선 이름이 나타날 때마다 새 문자열 객체를 생성할 수 있습니다. 이를 확인하기 위해 `id()` 함수를 사용하여 각 문자열 객체의 고유 식별자를 가져오겠습니다.

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

출력은 여러분을 놀라게 할 수 있습니다.

```
Number of unique route string objects: 542305
```

이는 고유한 노선 이름이 181 개뿐이지만 500,000 개 이상의 고유한 문자열 객체가 있음을 보여줍니다. 이는 Python 이 값이 동일하더라도 각 행에 대해 새 문자열 객체를 생성하기 때문에 발생합니다. 이는 특히 대규모 데이터 세트를 처리할 때 상당한 메모리 낭비로 이어질 수 있습니다.

## 메모리 절약을 위한 문자열 인터닝

Python 은 `sys.intern()` 함수를 사용하여 문자열을 "인턴"(재사용) 하는 방법을 제공합니다. 데이터 세트에 중복된 문자열이 많은 경우 문자열 인터닝을 통해 메모리를 절약할 수 있습니다. 문자열을 인터닝하면 Python 은 동일한 문자열이 이미 인터닝 풀에 있는지 확인합니다. 있는 경우 새 문자열 객체를 생성하는 대신 기존 문자열 객체에 대한 참조를 반환합니다.

간단한 예제를 통해 문자열 인터닝이 어떻게 작동하는지 살펴보겠습니다.

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

이 코드에서는 먼저 인터닝 없이 동일한 값을 가진 두 개의 문자열 변수 `a`와 `b`를 생성합니다. `is` 연산자는 두 변수가 동일한 객체를 참조하는지 확인합니다. 인터닝이 없으면 `a`와 `b`는 서로 다른 객체이므로 `a is b`는 `False`를 반환합니다. 그런 다음 `sys.intern()`을 사용하여 두 문자열을 인터닝합니다. 인터닝 후 `a`와 `b`는 인터닝 풀의 동일한 객체를 참조하므로 `a is b`는 `True`를 반환합니다.

출력은 다음과 같아야 합니다.

```
a is b (without interning): False
a is b (with interning): True
```

이제 CTA 버스 데이터를 읽을 때 문자열 인터닝을 사용하여 메모리 사용량을 줄여보겠습니다. 또한 `tracemalloc` 모듈을 사용하여 인터닝 전후의 메모리 사용량을 추적합니다.

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

이 코드에서는 먼저 `tracemalloc.start()`를 사용하여 메모리 추적을 시작합니다. 그런 다음, `sys.intern`을 첫 번째 열의 데이터 타입으로 전달하여 노선 열에 대한 인터닝으로 CTA 버스 데이터를 읽습니다. 그 후, 고유한 노선 문자열 객체의 수를 다시 확인하고 현재 및 최대 메모리 사용량을 출력합니다.

출력은 다음과 같아야 합니다.

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

인터프리터를 다시 시작하고 노선 및 날짜 문자열을 모두 인터닝하여 메모리 사용량을 더 줄일 수 있는지 시도해 보겠습니다.

```python
exit()
```

Python 을 다시 시작합니다.

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

출력은 메모리 사용량의 추가 감소를 보여야 합니다.

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

이는 Python 의 메모리 모델을 이해하고 문자열 인터닝과 같은 기술을 사용하면 특히 반복되는 값이 포함된 대규모 데이터 세트를 처리할 때 프로그램을 최적화하는 데 도움이 될 수 있음을 보여줍니다.

마지막으로, Python 인터프리터를 종료합니다.

```python
exit()
```
