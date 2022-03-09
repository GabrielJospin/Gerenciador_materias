import logger

from scr.connection import Constants
import mysql.connector as conn


class Mysql:

    def __init__(self):
        cons = Constants()
        self.connection = conn.connect(
            host=cons.HOST,
            database=cons.database,
            user=cons.user,
            password=cons.password
        )

        self.cursor = self.connection.cursor()

        logger.logger.info("Connection DB:", self.connection.connection_id)

    def close(self):
        self.connection.close()
        logger.logger.info("close connection")

    def mutation(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            logger.logger.info("Mutation feita com sucesso")
        except Exception as e:
            logger.logger.error("Erro na mutation", e)
            raise Exception(f'Erro na mutation {e}')

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            logger.logger.info("Query realizada com sucesso")
            return response
        except Exception as e:
            logger.logger.error("Erro na query", e)
            raise Exception(f'Erro na query {e}')
