#Play market 

#Импорты
from flask import Flask,render_template,url_for,request,flash,redirect
import os
import sqlite3 as sq
import bd
#Регестрация приложения
app=Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"]="djsenrbbrvrjsiskssnbeehrhejsn"

#Главное приложение
@app.route("/")
def index():
    category=[["Для детей","kids_category"],
                      ["Образовательные","um_category"] 
                         ]
    with sq.connect("main.db") as con:
        cur=con.cursor()
        app=[i for i in cur.execute("SELECT * FROM app ")]
        z=[]
        for i in app:
                g=[]
                g.append(i[0])
                g.append(url_for("static", filename=i[1]))
                g.append(i[2])
                g.append(url_for("static", filename=i[3]))
                z.append(g)
   
    return render_template("index.html",app=z,category=category)
    
    
    
@app.route("/app/<nameapp>")
def appname(nameapp):
 with sq.connect("main.db") as con:
     cur=con.cursor()
     app=[i for i in cur.execute("SELECT * FROM app ")]
     z=[]
     p=[]
     for i in app:
                g=[]
                g.append(i[0])
                g.append(url_for("static", filename=i[1]))
                g.append(i[2])
                g.append(url_for("static", filename=i[3]))
                if i[4]:
                    g.append(url_for("static", filename=i[4]))
                if i[5]:
                    g.append(url_for("static", filename=i[5]))
                if i[6]:
                    g.append(url_for("static", filename=i[6]))
                if i[7]:
                    g.append(url_for("static", filename=i[7]))
                if i[8]:
                    g.append(url_for("static", filename=i[8]))
                
                z.append(g)
                
     for i in z:
          h=[bd.ozenka(nameapp)]
          if str(i[0])==str(nameapp):
              p.append(i)
     return render_template("app.html",app=p, comment=bd.comment_app(nameapp),ozenka=h)

@app.route("/comment/<nameapp>",methods=["POST","GET"])
def comment(nameapp):
   if request.method=="POST":
       
           bd.comment(nameapp,request.form["email"],request.form["comment"],request.form["zena"])
           
   return "Комментарий успешно опубликован"
   
@app.route("/category/<namecategory>")
def category(namecategory):
      a=(bd.category(namecategory))
      z=[]
      for i in a:
                g=[]
                g.append(i[0])
                g.append(url_for("static", filename=i[1]))
                g.append(i[2])
                g.append(url_for("static", filename=i[3]))
                z.append(g)
    
      return render_template("index.html",app=z)
      
@app.route("/app/poisk",methods=["POST","GET"])
def poisk():
        if request.method=="POST":
            app=bd.poisk(request.form["poisk"])
            z=[]
            for i in app:
                g=[]
                g.append(i[0])
                g.append(url_for("static", filename=i[1]))
                g.append(i[2])
                g.append(url_for("static", filename=i[3]))
                z.append(g)
            
            return render_template("poisk.html",title=request.form["poisk"],app=z)
            
        else:
            return render_template("form.html")
            
     

# Запуск приложения 
if __name__=="__main__":
    app.run(debug=True)
    