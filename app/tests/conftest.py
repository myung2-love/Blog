import pytest
from app.db import engine, Base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    # 테스트 데이터베이스 초기화
    Base.metadata.drop_all(bind=engine)  # 기존 테이블 삭제
    Base.metadata.create_all(bind=engine)  # 새로 테이블 생성

    # 테스트 데이터 삽입 방지
    session = Session()
    session.commit()
    session.close()