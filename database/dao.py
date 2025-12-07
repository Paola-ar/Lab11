from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rifugio import Rifugio


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def readAllConnessione(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT c.id, c.id_rifugio1, c.id_rifugio2 FROM connessione c 
                    WHERE c.anno <= %s """
                    #GROUP BY c.id_rifugio1, c.id_rifugio2"""
        cursor.execute(query,(year, ))
        for row in cursor:
            con = Connessione(row["id"], row["id_rifugio1"], row["id_rifugio2"])
            result.append(con)
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def readAllRifugi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM rifugio """
        cursor.execute(query)
        for row in cursor:
            rifugio = Rifugio(row["id"], row["nome"], row["localita"], row["altitudine"], row["capienza"], row["aperto"])
            result.append(rifugio)
        cursor.close()
        conn.close()
        return result
