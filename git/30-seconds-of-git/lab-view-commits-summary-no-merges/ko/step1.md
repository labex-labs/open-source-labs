# 병합 커밋을 제외한 커밋의 간략한 요약 보기

여러 다른 개발자와 함께 프로젝트를 진행하고 있으며, 저장소에 이루어진 모든 커밋의 요약을 보고 싶습니다. 하지만, 코드에 대한 실제 변경 사항을 포함하지 않는 병합 커밋은 보고 싶지 않습니다. 병합 커밋을 제외한 모든 커밋의 요약을 어떻게 볼 수 있을까요?

이 랩에서는 `https://github.com/labex-labs/git-playground`의 저장소를 사용해 보겠습니다.

1. 저장소를 복제하고, 디렉토리로 이동하여 ID 를 구성합니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `feature1`이라는 브랜치를 생성하고 전환한 다음, `file.txt`라는 파일을 생성하고 "feature 1"을 작성합니다. 이를 스테이징 영역에 추가하고 "Add feature 1" 메시지로 커밋합니다.

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add .
git commit -m "Add feature 1"
```

3. `master` 브랜치로 다시 전환하고, `feature1` 브랜치를 병합하고, 순방향 병합을 비활성화하고, 텍스트를 변경하지 않고 저장하고 종료합니다.

```shell
git checkout master
git merge --no-ff feature1
```

4. 병합 커밋을 제외한 모든 커밋의 간략한 요약을 봅니다.

```shell
git log --oneline --no-merges
```

이렇게 하면 저장소에 이루어진 모든 커밋 목록이 출력되며, 병합 커밋은 제외됩니다. 출력 결과는 다음과 유사합니다.

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
