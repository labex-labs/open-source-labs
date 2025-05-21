# 더 발전된 Python 프로그램 만들기

이제 Python 의 기본 사항을 이해했으므로, 다음 단계로 넘어가 더 발전된 Python 프로그램을 만들 차례입니다. 이 프로그램은 텍스트 문자로 구성된 간단하지만 시각적으로 흥미로운 디자인인 ASCII 아트 패턴을 생성합니다. 이 프로그램을 통해 모듈 가져오기, 함수 정의, 명령줄 인수 처리와 같은 몇 가지 중요한 Python 개념을 배우고 적용할 수 있습니다.

## ASCII 아트 프로그램 만들기

1. 먼저, WebIDE 에서 `art.py` 파일을 열어야 합니다. 이 파일은 설정 과정에서 생성되었습니다. `/home/labex/project` 디렉토리에서 찾을 수 있습니다. 이 파일을 여는 것이 ASCII 아트 프로그램을 작성하는 시작점입니다.

2. 파일이 열리면, 기존 내용이 있을 수 있습니다. 처음부터 자체 코드를 작성할 것이므로 해당 내용을 지워야 합니다. 따라서 파일의 기존 내용을 모두 삭제합니다. 그런 다음, 다음 코드를 `art.py` 파일에 복사합니다. 이 코드는 ASCII 아트 생성기의 핵심입니다.

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. 코드를 파일에 복사한 후에는 작업을 저장하는 것이 중요합니다. 키보드에서 Ctrl + S 를 눌러 이 작업을 수행할 수 있습니다. 또는 메뉴로 이동하여 File > Save 를 선택할 수 있습니다. 파일을 저장하면 코드가 저장되고 실행할 준비가 됩니다.

## 코드 이해

이 프로그램이 무엇을 하는지 자세히 살펴보겠습니다. 코드를 이해하는 것은 향후 코드를 수정하고 확장할 수 있도록 하는 데 매우 중요합니다.

- **Import 문**: `import sys` 및 `import random` 줄은 Python 의 내장 모듈을 가져오는 데 사용됩니다. `sys` 모듈은 Python 인터프리터에서 사용하거나 유지 관리하는 일부 변수와 인터프리터와 강력하게 상호 작용하는 함수에 대한 액세스를 제공합니다. `random` 모듈을 사용하면 무작위 ASCII 아트 패턴을 만드는 데 사용할 난수를 생성할 수 있습니다.
- **문자 집합**: `chars = '\|/'` 줄은 ASCII 아트를 만드는 데 사용될 문자 집합을 정의합니다. 이러한 문자는 패턴을 형성하기 위해 무작위로 선택됩니다.
- **`draw()` 함수**: 이 함수는 ASCII 아트 패턴을 생성하는 역할을 합니다. `rows`와 `columns`의 두 인수를 사용하며, 이는 패턴의 치수를 지정합니다. 함수 내부에서는 루프를 사용하여 `chars` 집합에서 문자를 무작위로 선택하여 패턴의 각 행을 만듭니다.
- **Main 블록**: `if __name__ == '__main__':` 블록은 Python 의 특수한 구조입니다. 이 블록 내의 코드가 `art.py` 파일이 직접 실행될 때만 실행되도록 합니다. 파일이 다른 Python 파일로 가져온 경우 이 코드는 실행되지 않습니다.
- **인수 처리**: `sys.argv` 변수에는 프로그램에 전달된 명령줄 인수가 포함되어 있습니다. 정확히 3 개의 인수 (스크립트 자체의 이름과 행 및 열의 수를 나타내는 두 개의 숫자) 가 제공되었는지 확인합니다. 이를 통해 사용자가 올바른 입력을 제공하는지 확인할 수 있습니다.
- **오류 처리**: `try/except` 블록은 발생할 수 있는 오류를 포착하는 데 사용됩니다. 사용자가 행과 열에 대해 정수가 아닌 값을 입력하는 등 잘못된 입력을 제공하는 경우 `try` 블록은 `ValueError`를 발생시키고 `except` 블록은 오류 메시지를 인쇄하고 프로그램을 종료합니다.

## 프로그램 실행

1. 프로그램을 실행하려면 먼저 WebIDE 에서 터미널을 열어야 합니다. 터미널은 Python 스크립트를 실행하기 위한 명령을 입력하는 곳입니다.

2. 터미널이 열리면 프로젝트 디렉토리로 이동해야 합니다. 여기에 `art.py` 파일이 있습니다. 터미널에서 다음 명령을 사용합니다.

   ```bash
   cd ~/project
   ```

   이 명령은 현재 작업 디렉토리를 프로젝트 디렉토리로 변경합니다.

3. 이제 올바른 디렉토리에 있으므로 프로그램을 실행할 수 있습니다. 다음 명령을 사용합니다.

   ```bash
   python3 art.py 5 10
   ```

   이 명령은 Python 에게 5 행 10 열로 `art.py` 스크립트를 실행하도록 지시합니다. 이 명령을 실행하면 터미널에 5×10 문자 패턴이 인쇄됩니다. 출력은 다음과 유사하게 나타납니다.

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   실제 패턴은 무작위이므로 출력은 여기에 표시된 예와 다릅니다.

4. 명령의 인수를 변경하여 다른 치수를 실험할 수 있습니다. 예를 들어, 다음 명령을 시도해 보십시오.

   ```bash
   python3 art.py 8 15
   ```

   이렇게 하면 8 행 15 열의 더 큰 패턴이 생성됩니다.

5. 오류 처리가 작동하는 것을 보려면 잘못된 인수를 제공해 보십시오. 다음 명령을 실행합니다.

   ```bash
   python3 art.py
   ```

   다음과 같은 오류 메시지가 표시됩니다.

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## 코드 실험

문자 집합을 수정하여 ASCII 아트 패턴을 더 흥미롭게 만들 수 있습니다. 방법은 다음과 같습니다.

1. 편집기에서 `art.py` 파일을 다시 엽니다. 여기에서 코드를 변경합니다.

2. 코드에서 `chars` 변수를 찾습니다. 다른 문자를 사용하도록 변경합니다. 예를 들어, 다음 코드를 사용할 수 있습니다.

   ```python
   chars = '*#@+.'
   ```

   이렇게 하면 ASCII 아트를 만드는 데 사용되는 문자 집합이 변경됩니다.

3. 변경한 후 Ctrl + S 또는 File > Save 를 사용하여 파일을 다시 저장합니다. 그런 다음 다음 명령으로 프로그램을 실행합니다.

   ```bash
   python3 art.py 5 10
   ```

   이제 새 문자를 사용하여 다른 패턴이 표시됩니다.

이 연습은 다음과 같은 몇 가지 중요한 Python 개념을 보여줍니다.

- 모듈 가져오기: Python 의 내장 모듈에서 추가 기능을 가져오는 방법.
- 함수 정의: 코드를 구성하기 위해 함수를 정의하고 사용하는 방법.
- 명령줄 인수 처리: 명령줄에서 사용자 입력을 수락하고 처리하는 방법.
- try/except를 사용한 오류 처리: 프로그램에서 오류를 적절하게 처리하는 방법.
- 문자열 조작: ASCII 아트 패턴을 형성하기 위해 문자열을 생성하고 조작하는 방법.
- 난수 생성: 고유한 패턴을 만들기 위해 난수를 생성하는 방법.
- 리스트 컴프리헨션: Python 에서 리스트를 만드는 간결한 방법으로, `draw()` 함수에서 사용됩니다.
