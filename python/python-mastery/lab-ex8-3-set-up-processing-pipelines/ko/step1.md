# 파일 팔로워를 사용한 코루틴 이해

코루틴이 무엇이며 파이썬에서 어떻게 작동하는지 이해하는 것부터 시작해 보겠습니다. 코루틴은 제너레이터 함수의 특수한 버전입니다. 파이썬에서 함수는 일반적으로 호출될 때마다 처음부터 시작합니다. 그러나 코루틴은 다릅니다. 코루틴은 데이터를 소비하고 생성할 수 있으며, 실행을 일시 중지하고 재개할 수 있는 기능을 가지고 있습니다. 즉, 코루틴은 특정 지점에서 작업을 일시 중지한 다음 나중에 중단된 지점부터 다시 시작할 수 있습니다.

## 기본 코루틴 파일 팔로워 생성

이 단계에서는 새로운 콘텐츠에 대해 파일을 모니터링하고 이를 처리하기 위해 코루틴을 사용하는 파일 팔로워를 생성합니다. 이는 파일의 끝을 지속적으로 표시하고 새 줄이 추가될 때 업데이트되는 Unix `tail -f` 명령과 유사합니다.

1. 코드 편집기를 열고 `/home/labex/project` 디렉토리에 `cofollow.py`라는 새 파일을 만듭니다. 여기에서 코루틴을 사용하여 파일 팔로워를 구현하기 위한 파이썬 코드를 작성합니다.

2. 다음 코드를 파일에 복사합니다.

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. 이 코드의 주요 구성 요소를 이해해 보겠습니다.

   - `follow(filename, target)`: 이 함수는 파일을 여는 역할을 합니다. 먼저 `f.seek(0, os.SEEK_END)`를 사용하여 파일 포인터를 파일의 끝으로 이동합니다. 그런 다음, 파일에서 새 줄을 지속적으로 읽으려고 시도하는 무한 루프에 들어갑니다. 새 줄이 발견되면 `send` 메서드를 사용하여 해당 줄을 대상 코루틴으로 보냅니다. 새 콘텐츠가 없으면 다시 확인하기 전에 `time.sleep(0.1)`을 사용하여 잠시 (0.1 초) 일시 중지합니다.
   - `@consumer` 데코레이터: 파이썬에서 코루틴은 데이터를 받기 시작하기 전에 "프라이밍 (primed)"되어야 합니다. 이 데코레이터가 이를 처리합니다. 코루틴에 초기 `None` 값을 자동으로 보내는데, 이는 코루틴이 실제 데이터를 받을 준비를 하기 위한 필수 첫 번째 단계입니다.
   - `printer()` 코루틴: 이것은 간단한 코루틴입니다. `yield` 키워드를 사용하여 자신에게 전송된 항목을 받는 무한 루프가 있습니다. 항목을 받으면 단순히 인쇄합니다.

4. 파일을 저장하고 터미널에서 실행합니다.

```bash
cd /home/labex/project
python3 cofollow.py
```

5. 주식 로그 파일의 내용이 인쇄되는 것을 볼 수 있으며, 파일에 새 줄이 추가될 때 계속해서 새 줄을 인쇄합니다. `Ctrl+C`를 눌러 프로그램을 중지합니다.

여기서 핵심 개념은 데이터가 `send` 메서드를 통해 `follow` 함수에서 `printer` 코루틴으로 흐른다는 것입니다. 이 데이터 "푸시 (pushing)"는 반복을 통해 데이터를 "풀 (pull)"하는 제너레이터와 반대입니다. 제너레이터에서는 일반적으로 `for` 루프를 사용하여 생성하는 값을 반복합니다. 그러나 이 코루틴 예제에서는 데이터가 코드의 한 부분에서 다른 부분으로 적극적으로 전송됩니다.
