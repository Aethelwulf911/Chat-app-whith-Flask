#BOUSSOURA Mohamed Cherif
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# connection a flask 
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )
# connection avec socketio
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

# connection au server
if __name__ == '__main__':
  socketio.run( app, debug = True )

# virtualenv templates
# git bash
# cd Desktop/.../...
# source templates/Scripts/activate