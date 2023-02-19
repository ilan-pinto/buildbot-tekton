import json
import sys
from flask import Flask
from flask import request,jsonify

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def parse():
    
    res = json.loads(request.get_data().decode('utf-8'))  
   
    if res.get("form"):
    
        form_data = json.loads(res["form"])
        print (form_data["text"] ,file=sys.stderr)
            
        extensions = {}
        extensions["branch"] = form_data.get("text")[0].split()[0]
        extensions["image"] = form_data.get("text")[0].split()[1]
        
        res = {
                "extensions":extensions ,
                "continue": True,
                "status": {"code": 0 , 
                           "message":"slack interceptor "
                           }
            }
    else:         
        res = {
                "extensions":extensions ,
                "continue": False,
                "status":  {"code": 3 , 
                           "message":"slack interceptor could not find http post data"
                           }
            
        }        
            
    result = jsonify(res)
    result.status_code = 200       
    return result
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)  