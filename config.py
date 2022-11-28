SECRET_KEY = 'alura2022'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='jogoteca'
    )