# Flask 설정

Flask 를 시작하려면, Flask 를 설치하고 새 프로젝트를 설정해야 합니다. 아래 지침을 따르세요:

1. 터미널 또는 명령 프롬프트에서 다음 명령을 실행하여 Flask 를 설치합니다:

   ```bash
   pip install flask
   ```

2. 새 파일을 열고 `app.py`로 저장합니다.

   ```bash
   cd ~/project
   touch app.py
   ```

3. Flask 모듈을 가져오고 Flask 클래스의 인스턴스를 생성합니다:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
