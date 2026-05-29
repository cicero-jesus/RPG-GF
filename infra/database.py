import psycopg2
import psycopg2.extras
import os


class InteranlServerError(Exception):
    def __init__(self, message, cause=None):
        super().__init__(message)
        self.cause = cause


def query(sql, params=None):
    client = None
    try:
        client = get_new_client()
        with client.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(sql, params)
            client.commit()
            try:
                return cur.fetchall()
            except psycopg2.ProgrammingError:
                return None  # INSERT/UPDATE/DELETE não retornam linhas
    except Exception as error:
        raise InteranlServerError("Erro de conexão no banco ou query.", cause=error)
    finally:
        if client:
            client.close()


def get_new_client():
    return psycopg2.connect(
        host=os.environ["POSTGRES_HOST"],
        port=os.environ["POSTGRES_PORT"],
        user=os.environ["POSTGRES_USER"],
        dbname=os.environ["POSTGRES_DB"],
        password=os.environ["POSTGRES_PASSWORD"],
        sslmode=os.environ.get(
            "POSTGRES_SSL", "prefer"
        ),  # disable | allow | prefer | require
    )
