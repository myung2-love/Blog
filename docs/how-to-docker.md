# **How to Use Docker**

이 문서는 Docker를 사용하여 API를 실행, 관리, 테스트 및 데이터 확인 방법을 안내합니다.
VS Code에서는 단축키 Ctrl+Shift+V(Windows/Linux) 또는 Cmd+Shift+V(Mac)를 사용하여 조회합니다.

---

## **목차**
1. [Docker 실행](#docker-실행)
2. [Docker 종료](#docker-종료)
3. [컨테이너 접속](#컨테이너-접속)
4. [테스트 실행](#테스트-실행)
5. [데이터 확인](#데이터-확인)
6. [가상환경 및 의존성 설치](#가상환경-및-의존성-설치)

---

## **Docker 실행**

### **1. Docker Compose로 실행**
Docker Desktop을 설치하고 아래 명령어를 실행하면 Docker Compose가 `docker-compose.yml` 파일에 정의된 서비스를 실행합니다:
```bash
docker-compose up --build
```
### **2. 백그라운드 실행**
컨테이너를 백그라운드에서 실행하려면 다음 명령어를 사용합니다:
```bash
docker-compose up -d --build
```

### **3. 실행 상태 확인**
실행 중인 컨테이너를 확인하려면:
```bash
docker ps
```
출력 예시:
```plaintext
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
8390fbafb797   blog-server    "uvicorn app.main:ap…"   30 seconds ago   Up 29 seconds   0.0.0.0:8000->8000/tcp   web-1
2a7343a07785   mysql:8.0.29   "docker-entrypoint.s…"   30 seconds ago   Up 30 seconds   3306/tcp, 33060/tcp      db-1
```

---

## **Docker 종료**
### **1. 종료**
현재 실행 중인 컨테이너를 중지하려면:

```bash
docker-compose down
```
### **2. 강제 종료**
실행 중인 컨테이너를 강제로 중지하려면:

```bash
docker stop <CONTAINER_ID>
```
### **3. 불필요한 리소스 정리**
정지된 컨테이너와 사용되지 않는 이미지를 삭제하려면:

```bash
docker system prune -a
```

---

## **컨테이너 접속**
### **1. FastAPI 컨테이너(web-1) 접속**
web-1 컨테이너 내부에 접속하려면:

```bash
docker exec -it blog-web-1 /bin/bash
```
### **2. MySQL 컨테이너(db-1) 접속**
db-1 컨테이너 내부에 접속하려면:

```bash
docker exec -it blog-db-1 /bin/bash
```

---

## **테스트 실행**
### **1. 컨테이너 내부에서 pytest 실행**
FastAPI 컨테이너 내부에 접속 후 테스트를 실행합니다:

```bash
docker exec -it blog-web-1 /bin/bash
pytest
```
### **2. 테스트 결과**
테스트가 성공하면 다음과 같은 결과가 출력됩니다:

```plaintext
============================= test session starts ==============================
platform linux -- Python 3.10.16, pytest-7.3.1
collected 2 items

app/tests/test_post.py ..                                                 [100%]

============================== 2 passed in 0.25s ===============================
```

---

## **데이터 확인**
### **1. MySQL 컨테이너 접속**
db-1 컨테이너 내부에 접속합니다:

```bash
docker exec -it blog-db-1 /bin/bash
```
### **2. MySQL CLI 실행**
MySQL CLI를 실행하여 데이터베이스를 확인합니다:

```bash
mysql -u root -p
```
비밀번호를 입력합니다(기본값: `password`).

### **3. 데이터베이스 및 테이블 확인**
데이터베이스를 선택하고 테이블 및 데이터를 확인합니다:

```sql
USE blog_db;
SHOW TABLES;
SELECT * FROM posts;
```

---

## **가상환경 및 의존성 설치**
### **1. 가상환경 생성 (선택)**
가상환경을 생성하지 않고 Docker를 사용할 수도 있습니다:

```bash
python -m venv blog
source blog/bin/activate    # Windows에서는 blog\Scripts\activate
```
### **2. Python 의존성 설치**
다음 명령어로 필요한 Python 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```