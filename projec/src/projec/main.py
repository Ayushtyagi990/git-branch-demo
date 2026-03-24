from fastapi import FastAPI, Depends,HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from .model import Address, Library
from .database import get_session

app = FastAPI()

@app.post("/Address")
def create_Address(Address : Address, session : Session = Depends(get_session)):
    session.add(Address)
    session.commit()
    session.refresh(Address)
    return Address
@app.get("/address")
def get_address(session : Session = Depends(get_session)):
    address  = session.exec(select(Address)).all()
    return address
@app.get("/address/{address_id}")
def get_address(address_id : int,session : Session  = Depends(get_session)):
    address = session.get(Address,address_id)
    return address
@app.delete("/address/{address_id}", status_code = 204)
def delete_address(address_id : int, session : Session = Depends(get_session)):
    address = session.get(Address,address_id)
    if not address:
        raise HTTPException(status_code  = 404, details = "address not found")
    session.delete(address)
    session.commit()
    return {"details" : f"address {address_id} deleted"}

@app.post("/Library")
def create_Library(Library : Library, session : Session = Depends(get_session)):
    session.add(Library)
    session.commit()
    session.refresh(Library)
    return Library

@app.get("/get-library")
def read_libraries(session: Session = Depends(get_session)):
    libraries = session.exec(
        select(Library).options(selectinload(Library.address)).where(Library.address_id == 1)
    ).all()
    result = []
    for lib in libraries:
        lib_data = lib.dict()
        print(lib_data)
        if lib.address:
            lib_data["address"] = lib.address.dict()
        result.append(lib_data)

    return result