# 제너레이터 수명 주기 및 클로저 이해

이 단계에서는 Python 제너레이터의 수명 주기를 살펴보고 이를 적절하게 닫는 방법을 배우겠습니다. Python 의 제너레이터는 모든 값을 한 번에 계산하여 메모리에 저장하는 대신, 즉석에서 일련의 값을 생성할 수 있는 특수한 유형의 이터레이터입니다. 이는 대규모 데이터 세트 또는 무한 시퀀스를 처리할 때 매우 유용할 수 있습니다.

## `follow()` 제너레이터란 무엇인가요?

프로젝트 디렉토리의 `follow.py` 파일을 살펴보겠습니다. 이 파일에는 `follow()`라는 제너레이터 함수가 포함되어 있습니다. 제너레이터 함수는 일반 함수와 유사하게 정의되지만, `return` 키워드 대신 `yield`를 사용합니다. 제너레이터 함수가 호출되면 제너레이터 객체를 반환하며, 이 객체를 반복하여 yield 하는 값을 얻을 수 있습니다.

`follow()` 제너레이터 함수는 파일에서 지속적으로 줄을 읽고 읽는 대로 각 줄을 yield 합니다. 이는 새 줄에 대해 파일을 지속적으로 모니터링하는 Unix `tail -f` 명령과 유사합니다.

WebIDE 편집기에서 `follow.py` 파일을 엽니다.

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

이 코드에서 `with open(filename, 'r') as f` 문은 파일을 읽기 모드로 열고 블록이 종료될 때 제대로 닫히도록 합니다. `f.seek(0, os.SEEK_END)` 줄은 파일 포인터를 파일의 끝으로 이동시켜 제너레이터가 끝에서부터 읽기를 시작하도록 합니다. `while True` 루프는 파일에서 지속적으로 줄을 읽습니다. 줄이 비어 있으면 아직 새 줄이 없다는 의미이므로 프로그램은 바쁜 대기를 피하기 위해 0.1 초 동안 대기한 다음 다음 반복으로 계속 진행합니다. 줄이 비어 있지 않으면 yield 됩니다.

이 제너레이터는 무한 루프에서 실행되므로 중요한 질문이 제기됩니다. 제너레이터 사용을 중단하거나 조기에 종료하려는 경우 어떻게 될까요?

## 클로저를 처리하도록 제너레이터 수정

제너레이터가 제대로 닫히는 경우를 처리하도록 `follow.py`의 `follow()` 함수를 수정해야 합니다. 이를 위해 `GeneratorExit` 예외를 catch 하는 `try-except` 블록을 추가합니다. `GeneratorExit` 예외는 가비지 수집 또는 `close()` 메서드를 호출하여 제너레이터가 닫힐 때 발생합니다.

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

이 수정된 코드에서 `try` 블록에는 제너레이터의 주요 로직이 포함되어 있습니다. `GeneratorExit` 예외가 발생하면 `except` 블록이 이를 catch 하고 'Following Done' 메시지를 출력합니다. 이는 제너레이터가 닫힐 때 정리 작업을 수행하는 간단한 방법입니다.

이러한 변경을 수행한 후 파일을 저장합니다.

## 제너레이터 클로저 실험

이제 제너레이터가 가비지 수집되거나 명시적으로 닫힐 때 어떻게 동작하는지 확인하기 위해 몇 가지 실험을 수행해 보겠습니다.

터미널을 열고 Python 인터프리터를 실행합니다.

```bash
cd ~/project
python3
```

### 실험 1: 실행 중인 제너레이터의 가비지 수집

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

이 실험에서는 먼저 `follow.py` 파일에서 `follow` 함수를 가져옵니다. 그런 다음 `follow('stocklog.csv')`를 호출하여 제너레이터 객체 `f`를 생성합니다. `next()` 함수를 사용하여 제너레이터에서 다음 줄을 가져옵니다. 마지막으로 `del` 문을 사용하여 제너레이터 객체를 삭제합니다. 제너레이터 객체가 삭제되면 자동으로 닫히고, 이는 `GeneratorExit` 예외 처리기를 트리거하여 'Following Done' 메시지가 출력됩니다.

### 실험 2: 제너레이터 명시적으로 닫기

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

이 실험에서는 새 제너레이터 객체 `f`를 생성하고 `for` 루프를 사용하여 반복합니다. 루프 내에서 각 줄을 출력하고 해당 줄에 문자열 'IBM'이 포함되어 있는지 확인합니다. 포함되어 있으면 제너레이터에서 `close()` 메서드를 호출하여 명시적으로 닫습니다. 제너레이터가 닫히면 `GeneratorExit` 예외가 발생하고 예외 처리기가 'Following Done' 메시지를 출력합니다. 제너레이터가 닫힌 후 다시 반복하려고 하면 제너레이터가 더 이상 활성 상태가 아니므로 출력이 없습니다.

### 실험 3: 제너레이터에서 벗어나 다시 시작하기

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

이 실험에서는 제너레이터 객체 `f`를 생성하고 `for` 루프를 사용하여 반복합니다. 루프 내에서 각 줄을 출력하고 해당 줄에 문자열 'IBM'이 포함되어 있는지 확인합니다. 포함되어 있으면 `break` 문을 사용하여 루프에서 벗어납니다. 루프에서 벗어나는 것은 제너레이터를 닫지 않으므로 제너레이터는 여전히 활성 상태입니다. 그런 다음 동일한 제너레이터 객체에 대해 새 `for` 루프를 시작하여 반복을 다시 시작할 수 있습니다. 마지막으로 제너레이터 객체를 삭제하여 정리하면 `GeneratorExit` 예외 처리기가 트리거됩니다.

## 주요 내용

1. 제너레이터가 닫히면 (가비지 수집 또는 `close()` 호출을 통해) 제너레이터 내에서 `GeneratorExit` 예외가 발생합니다.
2. 제너레이터가 닫힐 때 정리 작업을 수행하기 위해 이 예외를 catch 할 수 있습니다.
3. 제너레이터의 반복에서 벗어나는 것 (`break` 사용) 은 제너레이터를 닫지 않으므로 나중에 다시 시작할 수 있습니다.

`exit()`를 입력하거나 `Ctrl+D`를 눌러 Python 인터프리터를 종료합니다.
