import sys
from flask import Flask
from flask import request,jsonify

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def parse():
    print(request.form ,file=sys.stderr)
    print(request.form ,file=sys.stdout)
    print(request.headers ,file=sys.stderr)
    print(request.headers ,file=sys.stdout)
    extensions = {}
    result = request.form.to_dict(flat=False)
    extensions["branch"] = result.get("text")[0].split()[0]
    extensions["image"] = result.get("text")[0].split()[1]
    
    res = {
            "extensions":extensions ,
            "continue": True,
            "status": " "
          }
    
    print(res)
    result = jsonify(res)
    result.status_code = 200 
    
    
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)  