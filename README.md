# Database Generator
학부 데이터베이스, DS2 수업 등에서  학생들의 데이터베이스 생성 및 권한 부여를 위한 프로그램.

1. Astronaut 에서 mysql docker 올리기. (Docker 잘 몰라서 그냥 이전에 사용한 명령어 복붙함.

비밀번호랑 이런거는 알아서 잘.
Astronaut에 700번 포트로 열림.
~~~bash
sudo docker run --detach --name=YOUR_CONTAINER_NAME --env="MYSQL_ROOT_PASSWORD=PASSWORD" --publish 7000:3306 mysql:latest
sudo docker exec YOUR_CONTAINER_NAME bash
~~~

Docker 내릴 땐 이렇게 :
~~~bash
sudo docker stop YOUR_CONTAINER_NAME
sudo docker rm YOUR_CONTAINER_NAME
~~~

2. <code>user.txt</code> 파일에 학생들 학번을 하나씩 넣어줌. (줄바꿈으로 구분)

예를들어, 학번이 2020_21966인 학생의 학번을 <code>user.txt</code>에 넣어주면, DB2020_21966 이라는 데이터베이스에 DB2020_21966이라는 user가 DB2020_21966 이라는 password로 초기화됨.

3. <code>python create.py</code>

<code>user.txt</code> 파일을 읽어와서 사용하는 하나씩 생성함. 생성 완료된 학생의 정보는 <code>done_user.txt</code> 라는 파일이 생성되어서 거기에서 확인하면 됨.




### Logs
1. 2022.11.19 : 코드 받아서 좀 수정해서 업로드 (형준)
