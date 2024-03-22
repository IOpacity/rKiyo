from Main import sql

sql.connect()
SESSION = sql.get_session()
BASE = sql.get_base()