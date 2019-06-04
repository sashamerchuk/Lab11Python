from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from Main import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://lab13:lab13@localhost/lab13'
db=SQLAlchemy(app)
ma = Marshmallow(app)

class CreativityGood(db.Model):
    __tablename__ = 'creativityGood'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80))
    price = db.Column(db.Integer)

    def __init__(self,name="", price=0):
        self.name=name
        self.price=price

    def __str__(self):
        return "{" + "name = '" + str(self.name) + '\''\
            +", price = '" + str(self.price) + "}"

class CreativityGoodSchema(ma.Schema):
    class Meta:
        fields = ('name','price')
creativity_good_schema = CreativityGoodSchema()
creativity_good_schema = CreativityGoodSchema(many=True)
db.create_all()

@app.route("/creativityGood/",methods=["POST"])
def add_creativity_good():
    name = request.get_json()["name"]
    price = request.get_json()["price"]

    new_creativity_good = CreativityGood(name,price)

    db.session.add(new_creativity_good)
    db.session.commit()

    return jsonify(request.json)

@app.route("/creativityGood/",methods=["GET"])
def all_creativity_good():
    all_creativity_good = CreativityGood.query.all()
    result= creativity_good_schema.dump(all_creativity_good)
    return jsonify(result.data)


@app.route("/creativityGood/<id>",methods=["GET"])
def get_creativity_good(id):
    creativity_good = CreativityGood.query.get(id)
    return creativity_good_schema.jsonify(creativity_good)



@app.route("/creativityGood/<id>",methods=["PUT"])
def replace_creativity_good(id):
    creativity_good = CreativityGood.query.get(id)
    creativity_good.name=request.json["name"]
    creativity_good.price=request.json["price"]

    db.session.commit()
    return creativity_good_schema.jsonify(request.json)

@app.route("/creativityGood/<id>",methods=["DELETE"])
def creativity_good_delete(id):
    creativity_good = CreativityGood.query.get(id)

    db.session.delete(creativity_good)
    db.session.commit()

    return creativity_good_schema.jsonify(creativity_good)

if __name__ == '__main__':
    app.run(debug=True)