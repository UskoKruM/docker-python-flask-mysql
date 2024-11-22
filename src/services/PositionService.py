# Database
from src.database.db_mysql import get_connection

# Exception Handler
from src.utils.ExceptionHandler import ExceptionHandler

# Models
from src.models.PositionModel import Position


class PositionService():

    @classmethod
    def get_positions(cls) -> list[dict]:
        positions = []

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('CALL sp_listPositions()')
                resultset = cursor.fetchall()

                for row in resultset:
                    position = Position(int(row[0]), row[1], float(row[2]), bool(row[3]))
                    positions.append(position.to_json())

            connection.close()
        except Exception as ex:
            positions = None
            ExceptionHandler.log_exception(ex)

        return positions
