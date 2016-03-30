
#.............................................................................................

from sqlalchemy import *
from sqlalchemy.sql import *
from flask  import *
from markdown import markdown
import os, hashlib, json
from json import *

# ............................................................................................... #

app = Flask(__name__)
app.secret_key = os.urandom(256)        

SALT = 'foo#BAR_{baz}^666'              


                                    

        
#.....................................................................................................................
#Definition des differentes routes 
@app.route('/')
def page():
    return redirect('/index/')

@app.route('/index/')
def index():
    return render_template('index.html')


# ............................................................................................... #

if __name__ == '__main__':
    app.run(debug=True)

# ............................................................................................... #      
                                                 

