from flask import Flask, render_template, redirect, jsonify
import pymongo
import mission_to_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    # print(mars)
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    
    mars = mongo.db.mars
    mars_data = mission_to_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)