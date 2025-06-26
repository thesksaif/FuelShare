from flask import Flask, render_template, request
from utils.mail_helper import send_fuel_summary_email  # Importing your helper function

app = Flask(__name__)

# -------------------- Routes --------------------

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    if email:
        return render_template("home.html", form_data=request.form, email=email)
    return "Enter a Valid Email", 401


@app.route("/calculate", methods=["POST"])
def calculate():
    email = request.form.get("email")
    car_avg = float(request.form.get("car_avg"))
    petrol_price = float(request.form.get("petrol_price"))
    km = float(request.form.get("km"))
    person_count = int(request.form.get("person_count"))

    per_km_cost = round(petrol_price / car_avg, 2)
    total_petrol = round(km / car_avg, 2)
    petrol_cost = round(total_petrol * petrol_price, 2)
    total_amount = round(per_km_cost * km, 2)
    per_person = round(total_amount / person_count, 2)
    
    return render_template("home.html",
                           per_km_cost=per_km_cost,
                           per_person=per_person,
                           total_amount=total_amount,
                           total_petrol=total_petrol,
                           petrol_cost=petrol_cost,
                           email=email,
                           form_data=request.form)


@app.route("/send-email", methods=["POST"])
def send_email():
    # Collect All Data from form
    email = request.form.get("email")
    car_avg = request.form.get("car_avg")
    petrol_price = request.form.get("petrol_price")
    km = request.form.get("km")
    person_count = request.form.get("person_count")
    per_km_cost = request.form.get("per_km_cost")
    total_petrol = request.form.get("total_petrol")
    petrol_cost = request.form.get("petrol_cost")
    per_person = request.form.get("per_person")
    total_amount = request.form.get("total_amount")

    # Use the helper function
    success, message = send_fuel_summary_email(
        email, car_avg, petrol_price, km, person_count,
        per_km_cost, total_petrol, petrol_cost, per_person, total_amount
    )

    return render_template("home.html",
                       form_data=request.form,
                       email=email,
                       per_km_cost=per_km_cost,
                       total_petrol=total_petrol,
                       petrol_cost=petrol_cost,
                       per_person=per_person,
                       total_amount=total_amount,
                       message=message)

    # return render_template("home.html", message=message) # You can also render a template with a success/failure message

if __name__ == "__main__":
    app.run(debug=True)
