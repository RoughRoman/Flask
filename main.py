from flask import Flask, request
from server.create import create_server
from server.delete import delete_server

app = Flask(__name__)

@app.post('/server')
def post_server():
    return(create_server(request))

@app.delete('/server')
def delete_server():    
    return(delete_server(request))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)