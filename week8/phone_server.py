from flask import Flask
from flask import render_template
from flask import Flask, jsonify, abort, request
import facade


app = Flask(__name__)
route = "/api/phones/"

facade.prepare_data()


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route(route + "/all")
def get_all():
    return jsonify(facade.get_all())


@app.route(route + "/add_new", methods=["POST"])
def add_new():
    if not request.json or not "name" in request.json or not "price" in request.json:
        abort(400)
    cell_phone = {}
    cell_phone["name"] = request.json["name"]
    cell_phone["price"] = request.json["price"]
    return jsonify(facade.add_new(cell_phone))
