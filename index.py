import os
import pymysql
from bottle import route, run, static_file, request, error, template, post


@route('/baeta')
def baeta():
    return template('baeta')

@route('/buid', method='get')
def buid():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1007002630', passwd='axelerawesome12',
                           db='1007002630_veflokaverk')
    cur = conn.cursor()
    info = request.query.get("info")
    val = request.query.get("val")
    nr = request.query.get("nr")
    if val == "baeta":
        cur.execute("Insert into todo (info, stada) values('{}','{:d}')".format(info, 0))
        #cur.execute("INSERT INTO todo (heiti,stada) Values(heiti,0)")
        conn.commit()
        cur.close()
        conn.close()
    elif val == "breyta":
        cur.execute("Update todo set stada='{}' where info='{}'".format(nr, info))
        conn.commit()
        cur.close()
        conn.close()
    else:
        cur.execute("Delete from todo where info = '{}'".format(info))
        conn.commit()
        cur.close()
        conn.close()
    return template('buid', info = info)


@route('/')
def todo():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1007002630', passwd='axelerawesome12',
                           db='1007002630_veflokaverk')
    cur = conn.cursor()
    cur.execute("SELECT * FROM todo")
    data = cur.fetchall()
    #conn.close()

    return template('index', cur = data)


run(host="0.0.0.0", port=os.environ.get('PORT'))

