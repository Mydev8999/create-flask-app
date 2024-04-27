
import os





chem_f = input("enter file location please: ")

os.chdir(chem_f)

os.makedirs( "static")
os.makedirs( "templates")


with open("templates" + "//"  + "index.html", 'w') as f:
    f.write("""

<!DOCTYPE html>
<html>
<head>
    <title>Page d'accueil</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='index.css') }}">
</head>
<body>
    <h1>Bienvenue sur la page d'accueil !</h1>
    <p>Ceci est une page d'accueil de base pour mon application Flask.</p>
</body>
</html>



""")
    
    f.close()


with open( "main.py", 'w') as f:
    f.write("""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')




if __name__ == '__main__':
    
    app.run(debug=True)






""")
    
    f.close()



with open("static" + "//" + "index.css", 'w') as f:
    f.write("""









""")
    
    f.close()



print("app create succefuly")