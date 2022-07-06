# GitHub

버전(커밋)을 관리한다



## 원격 저장소 만들기

로컬 저장소 > 원격 저장소



1. 해당 로컬로 이동해서 git init

​		init 하면 master 표시 나타남

2. 설정

​	visual studio code를 에디터로 활용하기

​	$ git config --global core.editor "code --wait"

3. 원격저장소 추가

​	git remote add <원격저장소> <url>

​	git remote add origin https://github.com/min486/git_test.git

4. 원격저장소 정보 확인

   git remote -v

5. 원격저장소에 push

   git push <원격저장소이름> <브랜치이름>

   git push origin master