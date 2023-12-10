from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)  # __name__代表目前執行的模組
app.config["SECRET_KEY"] = "bruh"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def handle_message(message):
    print("Receive message: " + message)
    if message != "User connected!":
        socketio.send(message)


@socketio.on("update_number")
def connected_msg(message):
    print("Receive update_number message")
    socketio.emit("update_number", message)


@socketio.on("last_number")
def connected_msg(message):
    print("Receive last_number message")
    socketio.emit("last_number", message)


@socketio.on("next_number")
def handle_next_number(message):
    print("Receive next_number message")
    socketio.emit("next_number", message)


@socketio.on("call")
def handle_call():
    print("Receive call message")
    socketio.emit("call")


@app.route("/")  # Decoractor: 已函式為基礎，提供附加功能
def home():
    return render_template("index.html")


@app.route("/index")  # Decoractor: 已函式為基礎，提供附加功能
def index():
    return render_template("index.html")


@app.route("/controller")
def controller():
    return render_template("controller.html")


@app.route("/displayer")
def displayer():
    return render_template("displayer.html")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

# , debug=True, port=5000
