# 소개

이번 랩에서는 컨테이너를 실행하기 위해 Docker 명령어를 사용했던 랩 1 에서 얻은 지식을 바탕으로 진행합니다. Dockerfile 로부터 사용자 정의 Docker Image 를 생성할 것입니다. Image 를 빌드한 후, 중앙 레지스트리에 푸시하여 다른 환경에 배포하기 위해 풀 (pull) 할 수 있도록 합니다. 또한, Image 레이어와 Docker 가 "copy-on-write" 및 union file system 을 통합하여 Image 를 효율적으로 저장하고 컨테이너를 실행하는 방법에 대해 간략하게 설명합니다.

이번 랩에서는 몇 가지 Docker 명령어를 사용할 것입니다. 사용 가능한 모든 명령어에 대한 전체 문서는 [공식 문서](https://docs.docker.com/)를 참조하십시오.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">83%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">100%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
