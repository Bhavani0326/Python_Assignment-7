import psycopg2

connect = psycopg2.connect(dbname='postgres', user='postgres', password='Simhavani@31', host='localhost', port='5432')

print('Connected Successfully')
