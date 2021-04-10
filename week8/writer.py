import mysql.connector as mysql


def add_new(cell):
    cnx = mysql.connect(host="db", user="root", passwd="root", db="db")
    cursor = cnx.cursor()
    query = "INSERT INTO cell_cursor   VALUES(%s, %s, %s) ;"
    cursor.execute(query, cell)
    cnx.commit()
    # What if more requests is made at once ? Which of them we get?
    id = cursor.lastrowid
    cursor.close()
    cnx.close()
    print(id)
    try:
        # inspect this....
        x = cnx.msql_insert_id()

        print(x)
    except Exception as e:
        print(e)

    if id > 0:
        return (id,cell[1],cell[2])
    else:
        raise Exception("Insertion failed")


def get_all():
    cnx = mysql.connect(host="db", user="root", passwd="root", db="db")
    cursor = cnx.cursor()
    query = "SELECT * FROM cell_cursor;"
    cursor.execute(query)
    all_phones = cursor.fetchall()

    cnx.commit()
    cursor.close()
    cnx.close()

    return all_phones


def save_cellphones(cellphones):
    cnx = mysql.connect(host="db", user="root", passwd="root", db="db")
    cursor = cnx.cursor()
    drop_query = "DROP TABLE IF EXISTS cell_cursor;"
    table_query = "create table cell_cursor( cell_id int not null auto_increment, name varchar(100) not null, price int, primary key(cell_id));"

    cursor.execute(drop_query)
    cursor.execute(table_query)

    # Insted of looping thrugh the list, append to the query string
    insert_query = "INSERT INTO cell_cursor VALUES(%(cell_id)s,%(name)s,%(price)s)"
    for c in cellphones:
        c["cell_id"] = None
        cursor.execute(insert_query, c)

    cnx.commit()
    cursor.close()
    cnx.close()

    print("Initial data saved in db")
