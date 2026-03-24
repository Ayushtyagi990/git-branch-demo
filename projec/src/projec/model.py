from sqlmodel import SQLModel, Field, Relationship

class Address(SQLModel, table  = True):
    id : int | None = Field(default  = None, primary_key = True)
    city : str | None = Field(default = None)
    state : str  | None = Field(default  = None)
    country : str | None =  Field(default = None)
    pincode : int | None = Field(default = None)
    latitude : float | None = Field(default  = None)
    longitiude : float | None = Field(default = None)


class Library(SQLModel, table  = True):
    id : int  | None = Field(default  = None, primary_key = True)
    name : str | None  = Field(default  = None)
    email : str | None = Field(default = None)
    phone : str  | None = Field(default = None)
    address_id: int | None = Field(default=None, foreign_key="address.id")
    address: Address | None = Relationship()
    total_seat : int  | None = Field(default = None)
    available_seat : int  | None = Field(default  = None)