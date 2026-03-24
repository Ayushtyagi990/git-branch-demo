from sqlmodel import SQLModel, create_engine , Session

engine = create_engine(
    "mysql+pymysql://root:@127.0.0.1:3306/address_project",
    echo=True
)

def get_session():
    with Session(engine) as session:
        yield session
        
SQLModel.metadata.create_all(engine)