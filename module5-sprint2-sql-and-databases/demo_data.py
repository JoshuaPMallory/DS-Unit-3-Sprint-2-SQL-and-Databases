import sqlite3
import SQL


questions = ['Count how many rows you have.'
            ,'How many rows are there where both `x` and `y` are at least 5?'
            ,'How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?'
            ]

answers   = []


partone.query('''
CREATE TABLE demo
    (s CHAR(1)
    ,x INT(1)
    ,y INT(1)
    )
''')

# Row 1
partone.query('''
INSERT INTO
    demo
VALUES
    ('g', 3, 9)
''')

# Row 2
partone.query('''
INSERT INTO
    demo
VALUES
    ('v', 5, 7)
''')

# Row 3
partone.query('''
INSERT INTO
    demo
VALUES
    ('f', 8, 7)
''')


# Count how many rows you have
answers.append(partone.query('''
SELECT
    COUNT(*)
FROM
    demo
''')[0][0])


# How many rows are there where both `x` and `y` are at least 5?
answers.append(partone.query('''
SELECT
    COUNT(*)
FROM
    demo
WHERE
    x >= 5 AND y >= 5
''')[0][0])

# How many unique values of `y` are there (hint - `COUNT()` can accept a keyword `DISTINCT`)?
answers.append(partone.query('''
SELECT
    COUNT(DISTINCT y)
FROM
    demo
''')[0][0])


num     = 0
running = True

while running:
    print(questions[num], '\n', answers[num], '\n')
    
    num += 1
    if num == len(questions):
        running = False
