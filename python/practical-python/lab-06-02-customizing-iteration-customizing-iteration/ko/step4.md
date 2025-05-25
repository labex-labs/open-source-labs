# 연습 문제 6.5: 스트리밍 데이터 소스 모니터링

제너레이터는 로그 파일이나 주식 시장 피드와 같은 실시간 데이터 소스를 모니터링하는 흥미로운 방법이 될 수 있습니다. 이 부분에서는 이 아이디어를 탐구해 보겠습니다. 시작하려면 다음 지침을 주의 깊게 따르십시오.

프로그램 `stocksim.py`는 주식 시장 데이터를 시뮬레이션하는 프로그램입니다. 출력으로, 이 프로그램은 실시간 데이터를 파일 `stocklog.csv`에 지속적으로 씁니다. 별도의 명령 창에서 `` 디렉토리로 이동하여 이 프로그램을 실행합니다.

```bash
$ python3 stocksim.py
```

Windows 를 사용 중인 경우 `stocksim.py` 프로그램을 찾아 두 번 클릭하여 실행하십시오. 이제 이 프로그램에 대해 잊어버리십시오 (그냥 실행되도록 두십시오). 다른 창을 사용하여 시뮬레이터가 작성하는 파일 `stocklog.csv`를 살펴보십시오. 몇 초마다 파일에 새로운 텍스트 줄이 추가되는 것을 볼 수 있습니다. 다시 말하지만, 이 프로그램을 백그라운드에서 실행하도록 두십시오. 몇 시간 동안 실행됩니다 (걱정할 필요가 없습니다).

위의 프로그램이 실행되면 파일을 열고, 끝으로 이동하여 새로운 출력을 감시하는 작은 프로그램을 작성해 보겠습니다. `follow.py` 파일을 만들고 이 코드를 넣으십시오.

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

프로그램을 실행하면 실시간 주식 시세를 볼 수 있습니다. 내부적으로 이 코드는 로그 파일을 감시하는 데 사용되는 Unix `tail -f` 명령과 유사합니다.

참고: 이 예제에서 `readline()` 메서드를 사용하는 것은 파일에서 줄을 읽는 일반적인 방법이 아니라는 점에서 다소 특이합니다 (일반적으로 `for` 루프를 사용합니다). 그러나 이 경우, 더 많은 데이터가 추가되었는지 확인하기 위해 파일의 끝을 반복적으로 조사하는 데 사용됩니다 (`readline()`은 새 데이터를 반환하거나 빈 문자열을 반환합니다).
