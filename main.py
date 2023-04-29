from fastapi import FastAPI
from rentproject.API import user, search

app = FastAPI()
app.include_router(user.router)
app.include_router(search.router)