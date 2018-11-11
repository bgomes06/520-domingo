from psycopg2 import connect

try:
    con = connect('host=127.0.0.1 dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    exit()


# cur.execute("insert into usuario (nome, linguagem) values ('dri', 'php')")
# con.commit()

cur.execute("update usuario set linguagem = 'C#' where nome = 'dri'")
con.commit()

cur.execute("delete from usuario where id = 3")
con.commit()

cur.execute("select * from usuario order by id;")
print(cur.fetchall())

con.rollback()
cur.close()
con.close()