# Pydantic models
# THese modles can help us design the shape of the data as classes with their attributes, and each attribute has its own type
# to use these models we have to install and import that package
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id":"123",
    "signup_ts":"2022-06-01 12:22",
    "friends": [1, "2", b"3"]
}
user = User(**external_data)
print(user)

# By doing this we can create instances of the class and can add an object with all the data