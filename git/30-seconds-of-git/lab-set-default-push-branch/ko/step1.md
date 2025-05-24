# 기본 푸시 브랜치 이름 설정

변경 사항을 원격 저장소 (remote repository) 로 푸시할 때, Git 은 현재 로컬 브랜치의 이름을 원격 브랜치의 기본 이름으로 사용합니다. 하지만 때로는 변경 사항을 다른 브랜치로 푸시하고 싶을 수 있습니다. 이 경우, 변경 사항을 푸시할 때마다 원격 브랜치의 이름을 명시적으로 지정해야 합니다. 특히 여러 브랜치로 작업하는 경우, 이는 번거롭고 오류가 발생하기 쉽습니다.

이 랩을 완료하려면 GitHub 계정의 `git-playground` Git 저장소를 사용합니다. 이 저장소는 `https://github.com/labex-labs/git-playground.git`의 포크에서 가져온 것입니다. 기본 푸시 브랜치 이름을 설정하려면 아래 단계를 따르세요.

1. 다음 명령을 사용하여 저장소를 복제 (clone) 합니다:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. 저장소 디렉토리로 이동합니다:
   ```
   cd git-playground
   ```
3. 기본 푸시 브랜치 이름을 현재 로컬 브랜치의 이름으로 설정합니다:
   ```
   git config push.default current
   ```
4. 새 브랜치를 생성하고 해당 브랜치로 전환합니다:
   ```
   git checkout -b my-branch
   ```
5. 저장소에 몇 가지 변경 사항을 적용하고 커밋합니다:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. 변경 사항을 원격 저장소로 푸시합니다:
   ```
   git push -u
   ```
   Git 은 변경 사항을 원격 저장소의 `my-branch`라는 이름의 브랜치로 푸시합니다.

다음은 `git log`를 실행한 결과입니다:

```shell
ADD hello.txt
```
