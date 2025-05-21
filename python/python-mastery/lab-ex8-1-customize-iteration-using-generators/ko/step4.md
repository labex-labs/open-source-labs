# 스트리밍 데이터를 위한 제너레이터 생성하기

프로그래밍에서 제너레이터는 특히 스트리밍 데이터 소스를 모니터링하는 것과 같은 실제 문제에 대처할 때 강력한 도구입니다. 이 섹션에서는 제너레이터에 대해 배운 내용을 이러한 실용적인 시나리오에 적용하는 방법을 배우겠습니다. 로그 파일을 주시하고 파일에 추가되는 새 줄을 제공하는 제너레이터를 만들 것입니다.

## 데이터 소스 설정하기

제너레이터를 만들기 전에 데이터 소스를 설정해야 합니다. 이 경우 주식 시장 데이터를 생성하는 시뮬레이션 프로그램을 사용합니다.

먼저 WebIDE 에서 새 터미널을 열어야 합니다. 여기에서 시뮬레이션을 시작하는 명령을 실행합니다.

터미널을 연 후 주식 시뮬레이션 프로그램을 실행합니다. 입력해야 하는 명령은 다음과 같습니다.

```bash
cd ~/project
python3 stocksim.py
```

첫 번째 명령 `cd ~/project`는 현재 디렉토리를 홈 디렉토리의 `project` 디렉토리로 변경합니다. 두 번째 명령 `python3 stocksim.py`는 주식 시뮬레이션 프로그램을 실행합니다. 이 프로그램은 주식 시장 데이터를 생성하고 현재 디렉토리의 `stocklog.csv`라는 파일에 씁니다. 모니터링 코드를 작업하는 동안 이 프로그램이 백그라운드에서 실행되도록 합니다.

## 간단한 파일 모니터 만들기

이제 데이터 소스가 설정되었으므로 `stocklog.csv` 파일을 모니터링하는 프로그램을 만들어 보겠습니다. 이 프로그램은 음수 가격 변동을 표시합니다.

1. 먼저 WebIDE 에서 `follow.py`라는 새 파일을 만듭니다. 이렇게 하려면 터미널에서 다음 명령을 사용하여 디렉토리를 `project` 디렉토리로 변경해야 합니다.

```bash
cd ~/project
```

2. 다음으로 다음 코드를 `follow.py` 파일에 추가합니다. 이 코드는 `stocklog.csv` 파일을 열고 파일 포인터를 파일 끝으로 이동한 다음 새 줄을 지속적으로 확인합니다. 새 줄이 발견되고 음수 가격 변동을 나타내는 경우 주식 이름, 가격 및 변동을 출력합니다.

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. 코드를 추가한 후 파일을 저장합니다. 그런 다음 터미널에서 다음 명령을 사용하여 프로그램을 실행합니다.

```bash
python3 follow.py
```

음수 가격 변동이 있는 주식을 보여주는 출력이 표시됩니다. 다음과 같이 표시될 수 있습니다.

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

프로그램을 중지하려면 터미널에서 `Ctrl+C`를 누릅니다.

## 제너레이터 함수로 변환하기

이전 코드가 작동하지만 제너레이터 함수로 변환하여 더 재사용 가능하고 모듈식으로 만들 수 있습니다. 제너레이터 함수는 일시 중지 및 재개할 수 있으며 한 번에 하나의 값을 yield 하는 특수한 유형의 함수입니다.

1. `follow.py` 파일을 다시 열고 제너레이터 함수를 사용하도록 수정합니다. 업데이트된 코드는 다음과 같습니다.

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

`follow` 함수는 이제 제너레이터 함수입니다. 파일을 열고 끝으로 이동한 다음 새 줄을 지속적으로 확인합니다. 새 줄이 발견되면 해당 줄을 yield 합니다.

2. 파일을 저장하고 다음 명령을 사용하여 다시 실행합니다.

```bash
python3 follow.py
```

출력은 이전과 동일해야 합니다. 그러나 이제 파일 모니터링 로직이 `follow` 제너레이터 함수에 깔끔하게 캡슐화됩니다. 즉, 이 함수를 파일을 모니터링해야 하는 다른 프로그램에서 재사용할 수 있습니다.

## 제너레이터의 강력함 이해하기

파일 읽기 코드를 제너레이터 함수로 변환하여 훨씬 더 유연하고 재사용 가능하게 만들었습니다. `follow()` 함수는 주식 데이터뿐만 아니라 파일을 모니터링해야 하는 모든 프로그램에서 사용할 수 있습니다.

예를 들어, 서버 로그, 애플리케이션 로그 또는 시간이 지남에 따라 업데이트되는 다른 파일을 모니터링하는 데 사용할 수 있습니다. 이는 제너레이터가 스트리밍 데이터 소스를 깨끗하고 모듈식 방식으로 처리하는 훌륭한 방법임을 보여줍니다.
