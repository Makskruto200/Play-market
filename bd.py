import sqlite3 as sq

def comment(nameapp,email,message,ozenka):
    with sq.connect("main.db") as con:
            cur=con.cursor()
            if ozenka=="laik":
                p=1
            elif ozenka=="dilaik":
                p=(-1)
            cur.execute(f"""INSERT INTO  comments VALUES ("{nameapp}","{email}","{message}","{p}")""")

def check(name):
    with sq.connect("main.db") as con:
            cur=con.cursor()
            t=[i for i in cur.execute("SELECT * FROM  comments")]
            p=False
            for i in t:
                if str(name)==str(i[1]):
                    p=True
            return p


def comment_app(name):
    with sq.connect("main.db") as con:
            cur=con.cursor()
            t=[i for i in cur.execute("SELECT * FROM  comments")]
            p=[]
            for i in t:
                if str(name)==str(i[0]):
                    p.append(i)
            return p

def ozenka(nameapp):
     with sq.connect("main.db") as con:
            cur=con.cursor()
            ozenka=[]
            laik=[]
            dilaik=[]
            t=[i for i in cur.execute(f"SELECT * FROM comments WHERE nameapp='{nameapp}'")]
     for i in t:
         if i[3]==1:
             laik.append(i[3])
         elif i[3]==-1:
             dilaik.append(i[3])
     ozenka.append(len(laik))
     ozenka.append(len(dilaik))
     return ozenka
   

    
             

def category(category):
    with sq.connect("main.db") as con:
        cur=con.cursor()
        t=[i for i in cur.execute(f"SELECT * FROM '{category}'")]
        app=[i for i in cur.execute(f"SELECT * FROM app")]
        ty=[]
        la=[]
    for i in t:
             ty.append(i[0])
    for i in app:
        if i[0] in ty:
            la.append(i)
            
    return la
           
             
                 
def poisk(name):
    with sq.connect("main.db") as con:
        cur=con.cursor()
        p=[]
        app=[i for i in cur.execute(f"SELECT * FROM app")]
        for i in app:
               if name in i[0]:
                            p.append(i)
        
        return p
                                               
                                  

            
        
        

    
    



    