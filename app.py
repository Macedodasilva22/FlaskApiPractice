from flask import Flask, request, jsonify
from user_date import user_info, add_user

app = Flask(__name__)


@app.route("/")
def home():
    return "home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_date = user_info(user_id)
    if not user_date:
        return jsonify({"error": "User not found"}), 404

    extra = request.args.get("extra")
    if extra:
        user_date["extra"] = extra

    return jsonify(user_date), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    if not all(key in data for key in ["user_id", "name", "email"]):
        return jsonify({"error": "Missing required fields (user_id, name, email)"}), 400

    user_id = data["user_id"]
    name = data["name"]
    email = data["email"]

    
    existing_user = user_info(str(user_id))
    if existing_user:
        return jsonify({"error": f"User with user_id {user_id} already exists"}), 400

    new_user = add_user(user_id, name, email)

    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(debug=True)
