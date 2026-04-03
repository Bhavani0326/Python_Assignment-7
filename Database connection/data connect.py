import psycopg2

connect = psycopg2.connect(dbname='postgres', user='postgres', password='demo@123', host='localhost', port='5432')

print('Connected Successfully')
