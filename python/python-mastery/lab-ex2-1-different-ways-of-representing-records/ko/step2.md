# 다양한 저장 방법으로 메모리 사용량 측정

이 단계에서는 데이터를 저장하는 다양한 방법이 메모리 사용량에 어떤 영향을 미치는지 살펴보겠습니다. 메모리 사용량은 특히 대용량 데이터 세트를 처리할 때 프로그래밍의 중요한 측면입니다. Python 코드에서 사용되는 메모리를 측정하기 위해 Python 의 `tracemalloc` 모듈을 사용합니다. 이 모듈은 Python 에서 할당된 메모리를 추적할 수 있으므로 매우 유용합니다. 이를 사용하면 데이터 저장 방법이 얼마나 많은 메모리를 소비하는지 확인할 수 있습니다.

## 방법 1: 전체 파일을 단일 문자열로 저장

새로운 Python 파일을 만들어 보겠습니다. `/home/labex/project` 디렉토리로 이동하여 `memory_test1.py`라는 파일을 만듭니다. 텍스트 편집기를 사용하여 이 파일을 열 수 있습니다. 파일이 열리면 다음 코드를 추가합니다. 이 코드는 파일의 전체 내용을 단일 문자열로 읽고 메모리 사용량을 측정합니다.

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

코드를 추가한 후 파일을 저장합니다. 이제 이 스크립트를 실행하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
python3 /home/labex/project/memory_test1.py
```

스크립트를 실행하면 다음과 유사한 출력이 표시됩니다.

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

정확한 숫자는 시스템에 따라 다를 수 있지만 일반적으로 현재 메모리 사용량은 약 12MB 이고 최대 메모리 사용량은 약 24MB 임을 알 수 있습니다.

## 방법 2: 문자열 목록으로 저장

다음으로, 데이터를 저장하는 또 다른 방법을 테스트합니다. 동일한 `/home/labex/project` 디렉토리에 `memory_test2.py`라는 새 파일을 만듭니다. 편집기에서 이 파일을 열고 다음 코드를 추가합니다. 이 코드는 파일을 읽고 각 줄을 목록의 별도 문자열로 저장한 다음 메모리 사용량을 측정합니다.

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

파일을 저장한 다음 터미널에서 다음 명령을 사용하여 스크립트를 실행합니다.

```bash
python3 /home/labex/project/memory_test2.py
```

다음과 유사한 출력이 표시됩니다.

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

데이터를 단일 문자열로 저장하는 이전 방법과 비교하여 메모리 사용량이 크게 증가했음을 알 수 있습니다. 이는 목록의 각 줄이 별도의 Python 문자열 객체이고 각 객체에 자체 메모리 오버헤드가 있기 때문입니다.

## 메모리 차이 이해

두 가지 접근 방식 간의 메모리 사용량 차이는 Python 프로그래밍에서 객체 오버헤드 (object overhead) 라고 하는 중요한 개념을 보여줍니다. 데이터를 문자열 목록으로 저장하면 각 문자열은 별도의 Python 객체입니다. 각 객체에는 다음과 같은 추가 메모리 요구 사항이 있습니다.

1. Python 객체 헤더 (일반적으로 객체당 16 - 24 바이트). 이 헤더에는 객체의 유형 및 참조 횟수와 같은 객체에 대한 정보가 포함되어 있습니다.
2. 문자열의 문자를 저장하는 실제 문자열 표현 자체.
3. 메모리 정렬 패딩. 이는 효율적인 액세스를 위해 객체의 메모리 주소가 적절하게 정렬되도록 추가된 여유 공간입니다.

반면에 전체 파일 내용을 단일 문자열로 저장하면 객체가 하나만 있으므로 오버헤드도 하나만 있습니다. 이는 데이터의 총 크기를 고려할 때 메모리 효율성이 더 높습니다.

대용량 데이터 세트로 작업하는 프로그램을 설계할 때는 메모리 효율성과 데이터 접근성 간의 이러한 트레이드 오프를 고려해야 합니다. 때로는 문자열 목록에 저장된 데이터를 액세스하는 것이 더 편리할 수 있지만 더 많은 메모리를 사용합니다. 다른 경우에는 메모리 효율성을 우선시하고 데이터를 단일 문자열로 저장하도록 선택할 수 있습니다.
