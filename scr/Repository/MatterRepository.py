import logger

from scr.connection import Mysql
from scr.entites import Matter


class MatterRepository():

    def __init__(self):
        self.connection = Mysql()

    def listMatters(self):
        logger.logger.info(f'selecting all Matters from Matter')

        return self.connection.query(f'SELECT * FROM Matter ORDER BY NAME')

    def listMattersBySemester(self, semester):
        logger.logger.info(f'selecting all Matters from semester {semester}')

        return self.connection.query(f'SELECT * FROM Matter WHERE SEMESTER = {semester} ORDER BY NAME')

    def getMatterByCODE(self, code):
        logger.logger.info(f'selecting the matter from code: {code}')

        return self.connection.query(f'SELECT * FROM Matter WHERE CODE = {code}')

    def insertMatter(self, m: Matter):
        logger.logger.info(f'insert Matter:{m}')
        return self.connection.mutation(
            f'INSERT INTO Matter(SEMESTER, NAME, CODE, TEACHER, description, color_hex, page) '
            f'VALUES({m.semester}, \'{m.name}\', \'{m.code}\', \'{m.teacher}\', \'{m.description}\', \'{m.color_hex}\', \'{m.page}\')'
        )

    def updateMatter(self, m: Matter):

        logger.logger.info(f'update Matter:{m}')
        return self.connection.mutation(
            f'UPDATE Matter SET '
            f'SEMESTER = \'{m.semester}\', NAME=\'{m.name}\', CODE=\'{m.code}\', TEACHER = \'{m.teacher}\', '
            f'description = \'{m.description}\', color_hex = \'{m.color_hex}\', page=\'{m.page}\'   '
            f' WHERE MATTER_ID = {m.matter_id}'
        )

    def deleteMatterById(self, matter_id: int):
        return self.connection.mutation(
            f'DELETE FROM Matter WHERE MATTER_ID=\'{matter_id}\' '
        )

    def deleteMatterByCode(self, code: str):
        return self.connection.mutation(
            f'DELETE FROM Matter WHERE CODE=\'{code}\' '
        )
