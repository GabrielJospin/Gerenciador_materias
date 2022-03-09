import re
from scr.Repository.MatterRepository import MatterRepository
from scr.entites import Matter


def codeValido(code):
    return re.fullmatch("[A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9]", code) is not None


class MatterService:

    def __init__(self):
        self.repository = MatterRepository()

    def listMatters(self):
        return self.repository.listMatters()

    def listMattersBySemester(self, semester:int):
        return self.repository.listMattersBySemester(semester)

    def getMatterByCode(self, code: str):
        if codeValido(code):
            return self.repository.getMatterByCODE(code)
        else:
            raise Exception(f'invalid code {code}')

    def insertMatter(self, matter: Matter):
        self.repository.insertMatter(matter)

    def updateMatter(self, matter: Matter):
        self.repository.updateMatter(matter)

    def deleteMatterById(self, id:int):
        self.repository.deleteMatterById(id)

    def deleteMatterByCode(self, code:str):
        if codeValido(code):
            self.repository.deleteMatterByCode(code)
        else:
            raise Exception(f'invalid code {code}')


