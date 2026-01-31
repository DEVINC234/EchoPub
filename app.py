import smtplib
from email.message import EmailMessage
from flask import Flask, request, render_template

app = Flask(__name__)

# =====================================
# 🔴 HARDCODED EMAIL CONFIG (TEMP ONLY)
# =====================================

EMAIL_USER = "notifications.echo@gmail.com"        # sender Gmail
EMAIL_PASS = "wceujosmuelmuanl"           # Gmail APP PASSWORD (no spaces)
ADMIN_EMAIL = "trendytrolls9@gmail.com"           # admin receiver email

# =====================================
# ROUTES
# =====================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
   try:
        name = request.form.get("name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("time")

        # just return success temporarily
        return "Form received"

    except Exception as e:
        print("ERROR IN /submit:", str(e))
        return "Something went wrong", 500

    # Create email
    msg = EmailMessage()
    msg["Subject"] = "🧠 New Psychology Booking"
    msg["From"] = EMAIL_USER
    msg["To"] = ADMIN_EMAIL
    msg.set_content(
        f"""
New booking received.

Name   : {name}
Mobile : {mobile}
Email  : {email}

Session Date : {date}
Session Time : {time}
Duration     : 1 Hour
Amount       : ₹999


Please contact the user.
"""
    )
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout = 15) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print("EMAIL ERROR:", e)


    return "Booking submitted successfully. We will contact you soon."

# =====================================
# RUN APP
# =====================================

if __name__ == "__main__":

    app.run(debug=True)





