from pydantic import BaseModel, Optional

class TheGuardian(BaseModel):
    article_date: Optional[str]
    title: Optional[str]
    subtitle: Optional[str]
    content: Optional[str]
    article: Optional[str]
    author: Optional[str]
    author_profile_link: Optional[str]