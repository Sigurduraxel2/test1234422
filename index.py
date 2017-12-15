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
    texti = request.query.get("texti")
    cur.execute("Insert into todo (heiti, stada) values('{}','{:d}')".format(texti, 0))
    conn.commit()
    cur.close()
    conn.close()
    return template('buid', heiti = heiti)

@route('/eyda')
def eyda():
    return template('eyda.tpl')


@route('/buid2', method='get')
def buid2():
    nr2 = request.query.get('enumer')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1007002630', passwd='axelerawesome12',
                           db='1007002630_veflokaverk')
    cur = conn.cursor()
    cur.execute("Delete from todo where id = {}".format(nr2))
    heiti = request.query.get("heiti")
    conn.commit()
    cur.close()
    conn.close()
    return template('buid', heiti = heiti)


@route('/breyta')
def breyta():
    return template('breyta.tpl')
@route('/buid3', method='get')
def buid3():
    nr3 = request.query.get('numer3')
    nytexti = request.query.get('nytexti')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1007002630', passwd='axelerawesome12',
                           db='1007002630_veflokaverk')
    cur = conn.cursor()
    cur.execute("Update todo set stada='{}' where heiti='{}'".format(nr3, nytexti))
    heiti = request.query.get("heiti")
    conn.commit()
    cur.close()
    conn.close()
    return template('buid', heiti = heiti)

    
    
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

