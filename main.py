from flask import Flask, render_template, request, jsonify
import socket
import ipaddress
import sys
import keyboard
# from pynput.keyboard import Controller, Key
# pkeyboard = Controller()

app = Flask(__name__)
# to write aplhanumeric use keyboard.write("A")
# to use enter backspace space use keyboard.send("value") where send = press + release

state = 0
@app.route("/")
def main():
    # Pass the template data into the template main.html and return it to the user
    print("Home Called")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "Home"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("auth response Sent")
    return response

@app.route("/auth/<action>")
def action_auth(action):
    print("auth Called")
    data = {}
    data["Name"] = "skorboard"
    data["Service"] = socket.gethostname()
    if action == "get":
        data["Status"] = "Enabled"
    if action == "set":
        data["Status"] = "Disabled"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("auth response Sent")
    return response
@app.route("/api/v1/ok")
def action_ok():
    print("Enter Called")
    keyboard.send("enter")
    # pkeyboard.press(Key.enter)
    # pkeyboard.release(Key.enter)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "Ok"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("Ok response Sent")
    return response

@app.route("/api/v1/back")
def backspace():
    print("backspace Called")
    keyboard.send("backspace")
    # pkeyboard.press(Key.backspace)
    # pkeyboard.release(Key.backspace)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "backspace"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("backspace response Sent")
    return response

@app.route("/api/v1/led")
def led():
    print("led Called")
    keyboard.send("esc")
    # pkeyboard.press(Key.esc)
    # pkeyboard.release(Key.esc)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "led"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("led response Sent")
    return response

@app.route("/api/v1/space")
def space():
    print("space Called")
    keyboard.send("space")
    # pkeyboard.press(Key.space)
    # pkeyboard.release(Key.space)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "space"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("space response Sent")
    return response

@app.route("/api/v1/btnLeft")
def action_left():
    print("btnLeft arrow Called")
    keyboard.send("left")
    # pkeyboard.press(Key.left)
    # pkeyboard.release(Key.left)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnLeft arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnLeft arrow response Sent")
    return response

@app.route("/api/v1/btnRight")
def btnRight():
    print("btnRight arrow Called")
    keyboard.send("right")
    # pkeyboard.press(Key.right)
    # pkeyboard.release(Key.right)

    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnRight arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnRight arrow response Sent")
    return response
@app.route("/api/v1/btnUp")
def btnUp():
    print("btnUp arrow Called")
    keyboard.send("up")
    # pkeyboard.press(Key.up)
    # pkeyboard.release(Key.up)

    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnUp arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnUp arrow response Sent")
    return response

@app.route("/api/v1/btnDown")
def btnDown():
    print("btnDown arrow Called")
    keyboard.send("down")
    # pkeyboard.press(Key.down)
    # pkeyboard.release(Key.down)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnDown arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnDown arrow response Sent")
    return response

@app.route("/api/v1/keys/<action>")
def btnVirtualKey(action):
    print("Nymeric Btn Called")
    if action == "fSlash":
        action = "/"
    if action == "dot":
        action = "."
    
    keyboard.write(action)
    # pkeyboard.press(action)
    # pkeyboard.release(action)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = action
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print(action + " response Sent")
    return response

# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     d["Query"] = "1100"
#     response = jsonify(d)
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Credentials", "true")
#     print("Page not found Called")
#     return response

@app.route("/api",methods=["GET"])
def word_predictor():
    d = {}
    text = str(request.args["Query"])
    text = text[::-1]
    d["Query"] = text
    response = jsonify(d)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("api Called")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)
