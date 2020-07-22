import os

from sqlalchemy import create_engine

DB_URI = ''.join([
    'oracle+cx_oracle://',
    f'{os.environ["DB_USER"]}:',
    f'{os.environ["DB_PASSWORD"]}@',
    f'{os.environ["DB_HOST"]}:',
    f'{os.environ["DB_PORT"]}/',
    f'{os.environ["DB_NAME"]}'
])

engine = create_engine(DB_URI)
