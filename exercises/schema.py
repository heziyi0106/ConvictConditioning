from ninja import Schema

class SkillSchema(Schema):
    id: int
    name: str
    description: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True