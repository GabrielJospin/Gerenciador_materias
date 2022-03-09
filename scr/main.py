from fastapi import FastAPI

from scr.entites import Matter
from scr.services import MatterService

app = FastAPI()
ms = MatterService()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/Matters")
async def matters():
    return ms.listMatters()


@app.get("/Matters/{semester}")
async def matters(semester: int):
    return ms.listMattersBySemester(semester)


@app.get("/Matter/{code}")
async def getMatter(code: str):
    return ms.getMatterByCode(code)


@app.post("/Matter")
async def insertMatter(matter: Matter):
    return ms.insertMatter(matter)


@app.put("/Matter")
async def updateMatter(matter: Matter):
    return ms.updateMatter(matter)


@app.delete("/Matter/id={id}")
async def updateById(id: int):
    return ms.deleteMatterById(id)


@app.delete("/Matter/code={code}")
async def updateById(code: str):
    return ms.deleteMatterByCode(code)
