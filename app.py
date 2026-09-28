from flask import Flask, jsonify, render_template

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Vivek",
        "role": "SRE Engineer",
        "location": "Bengaluru"
    },
    {
        "id": 2,
        "name": "Rahul",
        "role": "DevOps Engineer",
        "location": "Kochi"
    },
    {
        "id": 3,
        "name": "Anu",
        "role": "Developer",
        "location": "Chennai"
    }
]


@app.route("/")
def home():
    return render_template("index.html", employees=employees)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})


@app.route("/api/employees")
def get_employees():
    return jsonify(employees)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
