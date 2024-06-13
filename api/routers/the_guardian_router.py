from typing import List

from api.contracts.the_guardian_schema import TheGuardianSchema
from api.datasources.bigquery import BigQueryR

from fastapi import APIRouter, Depends

the_guardian_router = APIRouter()

@the_guardian_router.get("/content", response_model=List[TheGuardianSchema])
def filter_by_content(repository: BigQueryR = Depends(BigQueryR)):
    results = repository.get_by_word_in_content()
    return results

# @the_guardian_router.get("/content/{word}", response_model=List[TheGuardianSchema])
# def filter_by_content(word: str, repository: BigQueryR = Depends(BigQueryR)):
#     results = repository.get_by_word_in_content(word)
#     return results