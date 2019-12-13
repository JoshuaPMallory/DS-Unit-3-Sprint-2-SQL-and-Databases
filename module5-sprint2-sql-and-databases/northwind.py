import sqlite3
import SQL


parttwo   = SQL.SQL('northwind_small.sqlite3')

questions = ['What are the ten most expensive items (per unit price) in the database?'
            ,'What is the average age of an employee at the time of their hiring?'
            ,'What are the ten most expensive items (per unit price) in the database *and* their suppliers?'
            ,'What is the largest category (by number of unique products in it)?'
            ]
answers   = []


# What are the ten most expensive items (per unit price) in the database?
answers.append(parttwo.query('''
SELECT
    UnitPrice
FROM
    Product
ORDER BY
    UnitPrice DESC
LIMIT
    10
'''))

# What is the average age of an employee at the time of their hiring?
# (Hint: a lot of arithmetic works with dates.)
answers.append(parttwo.query('''
SELECT
    AVG(HireDate - BirthDate)
FROM
    Employee
''')[0][0])

num     = 0
running = True

# What are the ten most expensive items (per unit price) in the database *and* their suppliers?
answers.append(partthree.query('''
SELECT
    UnitPrice, ProductName, CompanyName
FROM
    Product
INNER JOIN
    Supplier on Product.SupplierID
GROUP BY
    ProductName
ORDER BY
    UnitPrice DESC
LIMIT
    10
'''))

# What is the largest category (by number of unique products in it)?

# After all my work, all I can concluse after searching dozens of questions online is that SQL has no built in method of grabbing the fucking headers
# SQL also doens't understand that I can't to grab CategoryID, which is somehow both listed inside the table, yet also is ungrabbable
# What this is doing is multiplying all of the category data across all other information, whcih makes it impossible to get anything but exactly the same information everywhere.
# The only way then to actually grab the headers is to go outside the code and look it up either inside the file or in a database viewer.
# SQL is an awful language and needs to be replaced.

answers.append(partthree.query('''
SELECT
    CategoryName, COUNT(ProductName)
FROM
    Product
LEFT JOIN
    Category on Product.CategoryID = Category.ID
GROUP BY
    CategoryName
ORDER BY
    COUNT(ProductName) DESC
LIMIT 1
''')[0])



while running:
    print(questions[num], '\n', answers[num], '\n')
    
    num += 1
    if num == len(questions):
        running = False
