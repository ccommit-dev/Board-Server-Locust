# Board-Server-Locust
성능테스트 툴 (https://docs.locust.io/en/stable/index.html)

1. 로커스트 설치. pip3 install locust
2. 성능 테스트 시나리오에 따른 .py 파일 작성
3. locust -f BoardServer.py 파일 실행
4. http://localhost:8089/ 접속 후 성능 테스트 진행

사전준비
1. 게시글 카테고리 10개 생성
2. 게시글 10만개 생성
3. 게시글 검색 API 각 시나리오 테스트별 진행

목표: 서버의 지표 CPU, RAM, DISK 와 목표 TPS 확인

시나리오
1. STRESS 테스트
- 500명의 동시 사용자가 초당 50번을 호출하여 분당(5분) 사용자를 50씩 늘려 서버의 지표를 확인

2. Endurance 테스트
- 100명의 동시 사용자가 초당 100번을 호출하였을때 10분동안 서버의 지표를 확인

3. PEAK 테스트
- 100명의 동시 사용자가 초당 50번씩 호출하다 1분에 1000명으로 사용자를 한번에 늘려 서버의 지표를 확인