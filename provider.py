from enum import Enum
from pydantic import BaseModel, PositiveInt, Field

# Enums
class Category(Enum):
    MERN = "MERN NestJS FullStack"
    PYTHON = "AI Python FullStack"




# DTO
class Student(BaseModel):
    id: PositiveInt
    group: str = Field(min_length=3, default="MIT")
    name: str = Field(min_length=3, max_length=20)
    age: int | None = Field(gt=20, default=None)
    category: Category = Category.PYTHON




# Database
students = {
    3: Student(id=3, group="MIT", name="Justin", age=26, category=Category.MERN),
    12: Student(id=12, group="MIT", name="David", age=28, category=Category.MERN),
    14: Student(id=14, group="MIT", name="Max", age=None, category=Category.PYTHON),
    23: Student(id=23, group="MIT", name="Justin", age=22, category=Category.PYTHON),
}