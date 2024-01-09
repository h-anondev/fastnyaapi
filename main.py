from fastapi import FastAPI
from NyaaPy import sukebei
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware


# CORS everywhere

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/{q}")
def search(q: str):
    javtitle = q
    nyaa = sukebei.SukebeiNyaa()
    res = nyaa.search(javtitle, category=2, filters=0)
    data = []
    count = 0
    for i in res:
        count += 1
        data.append(i)

    return {"data": data, "count": count}
        