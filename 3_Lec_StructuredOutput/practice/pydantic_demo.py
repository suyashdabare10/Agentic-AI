from pydantic import BaseModel,EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name : str
    age: int
    height:Optional[int] = None
    email:EmailStr
    cgpa: float = Field(gt=0, lt=10, default=0)


new_student = {'name':'suyash', 'age':'45', 'email':'hydra@gmail.com', }

student = Student(**new_student)

print(student)

