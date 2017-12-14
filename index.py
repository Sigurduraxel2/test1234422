import os
import pymysql
from bottle import route, run, static_file, request, error, template, post


@route('/baeta')
def baeta():
    return template('baeta')

@route('/buid', method='get')
def buid():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2304003260', passwd='mypassword',
                           db='2304003260_todo')
    cur = conn.cursor()
    heiti = request.query.get("heiti")
    val = request.query.get("val")
    nr = request.query.get("nr")
    if val == "baeta":
        cur.execute("Insert into todo (heiti, stada) values('{}','{:d}')".format(heiti, 0))
        #cur.execute("INSERT INTO todo (heiti,stada) Values(heiti,0)")
        conn.commit()
        cur.close()
        conn.close()
    elif val == "breyta":
        cur.execute("Update todo set stada='{}' where heiti='{}'".format(nr, heiti))
        conn.commit()
        cur.close()
        conn.close()
    else:
        cur.execute("Delete from todo where heiti = '{}'".format(heiti))
        conn.commit()
        cur.close()
        conn.close()
    return template('buid', heiti = heiti)


@route('/')
def todo():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2304003260', passwd='mypassword',
                           db='2304003260_todo')
    cur = conn.cursor()
    cur.execute("SELECT * FROM todo")
    data = cur.fetchall()
    #conn.close()

    return template('index', cur = data)

if os.environ.get('Gaman'):
    run(host="0.0.0.0", port=os.environ.get('PORT'))
else:
    run(host='localhost', port=8080, debug=True)
