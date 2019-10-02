import sqlite3

def add(id):
    choice = input("What bucket fruit (f) or vegetable (v) ")
    item   = input("What item are you adding ")
    cursor.execute("INSERT INTO PRODUCE (ID,TYPE,NAME) \
       VALUES (?,?,?)",(id,choice,item));  
    conn.commit()
               
def find():
    choice2 = input("what fruit or vegetable item do you want to find ")
    for row in cursor.execute( """SELECT TYPE FROM PRODUCE WHERE NAME = '%s'""" % (choice2)):
        print(" the bucket (if any) it is in is:")
        print(row)

def display():
    print(" PRODUCE DB Contents")
    for row in cursor.execute("SELECT ID, TYPE,NAME from PRODUCE"):
	
        print("id number = ", row[0])
        print("type of produce = ", row[1])
        print("name = ", row[2], "\n")
   
conn = sqlite3.connect('produceCA.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''CREATE TABLE IF NOT EXISTS PRODUCE (ID INT PRIMARY KEY NOT NULL,TYPE STRING NOT NULL,NAME STRING NOT NULL);''')

def main():
    answer="y"
    idNum=1
    while answer=="y":
        print ("Fruits and Vegetable Buckets") 
        print ("\n1: add item to inventory/bucket database") 
     
        print ("2: find item by name (displays which bucket it is in)") 
        
        print ("3: display all items in bucket\n")
        choice = input("what do you want to do? 1,2,3 ")
        if choice=="1":
            add(idNum)
            idNum=idNum+1
        if choice=="2":
            find()
        if choice=="3":
            display()
        
        answer = input("Do you want to continue? Enter y or n ")
	
    conn.commit()
    conn.close()
main()
