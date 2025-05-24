# 빈 커밋 생성

Git 저장소에서 빈 커밋을 생성해야 합니다. 이는 다음과 같은 여러 시나리오에서 유용할 수 있습니다.

- 빌드 프로세스 트리거
- 자리 표시자 (placeholder) 커밋 생성
- 저장소 기록의 특정 지점 표시

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다.

1. `git clone https://github.com/labex-labs/git-playground` 명령을 사용하여 저장소를 로컬 머신으로 복제합니다.
2. `cd git-playground` 명령을 사용하여 저장소 디렉토리로 이동하고, `git config --global user.name "your-uername"` 및 `git config --global user.email "your-email"` 명령을 사용하여 환경에서 GitHub 계정을 구성합니다.
3. `git commit --allow-empty -m "Empty commit"` 명령을 사용하여 "Empty commit" 메시지와 함께 빈 커밋을 생성합니다.
4. `git log --name-status HEAD^..HEAD` 명령을 사용하여 빈 커밋이 생성되었는지 확인합니다.

다음은 `git log --name-status HEAD^..HEAD`를 실행하는 곳이며, 결과는 다음과 같습니다.

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
