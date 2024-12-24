import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, get_db
from fastapi.testclient import TestClient
from app.main import app

# SQLite 공유 인메모리 데이터베이스 설정
TEST_DATABASE_URL = "sqlite:///file::memory:?cache=shared"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블 초기화
@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # 테이블 삭제 및 생성
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# 테스트용 데이터베이스 세션 제공
@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# FastAPI 의존성 오버라이딩
@pytest.fixture(scope="function", autouse=True)
def override_get_db(db_session):
    def _get_db():
        try:
            yield db_session
        finally:
            pass
    app.dependency_overrides[get_db] = _get_db