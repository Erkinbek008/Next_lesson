from sqlite3 import connect
test = connect('oquvchilar.dp')
cursor= test.cursor()

cursor.executescript('''
    CREATE TABLE oquvchilar(
       id INT,
       name TEXT,
       age INT,
       school TEXT
    );
''')

cursor.execute('''
INSERT INTO oquvchilar VALUES(
    '1',
    'Erkinbek',
    '14',
    '23-maktab' 
    ); 
''')

cursor.execute('''
INSERT INTO oquvchilar VALUES(
    '2',
    'Xumoyun',
    '18',
    'TATU' 
    ); 
''')
cursor.execute('''
INSERT INTO oquvchilar VALUES(
    '3',
    'Mirafzal',
    '18',
    'TATU' 
    ); 
''')
cursor.execute('''
INSERT INTO oquvchilar VALUES(
    '4',
    'Otabek',
    '21',
    'Shanghai JiaoTong university' 
    ); 
''')
cursor.execute('''
INSERT INTO oquvchilar VALUES(
    '5',
    'Madaminbek',
    '25',
    'ELITE school' 
    ); 
''')
test.commit()
test.close()