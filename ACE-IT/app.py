from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enquire", methods=["POST"])
def enquire():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    program = request.form.get("program", "").strip()

    if not name or not phone or not program:
        return render_template(
            "index.html",
            message="Please complete all fields."
        )

    # Demo only: no database or email delivery is configured.
    print(f"New enquiry: {name}, {phone}, {program}")

    return render_template(
        "index.html",
        message="Thanks! Your enquiry has been received."
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("FLASK_DEBUG") == "1"
    )