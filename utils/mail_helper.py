import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

import ssl

# Load environment variables
load_dotenv()

def send_fuel_summary_email(email, car_avg, petrol_price, km, person_count,
                            per_km_cost, total_petrol, petrol_cost, per_person, total_amount):
    html_content = f"""
    <html>
    <body style="font-family: Arial; padding: 20px;">
        <h2>🚗 FuelShare – Your Travel Budget Summary</h2>

        <h3>🔢 Trip Input Details</h3>
        <p><strong>Car Average:</strong> {car_avg} KM/L</p>
        <p><strong>Petrol Price:</strong> ₹{petrol_price} / L</p>
        <p><strong>Total Distance:</strong> {km} KM</p>
        <p><strong>Total Persons:</strong> {person_count}</p>

        <h3>💰 Calculated Summary</h3>
        <p><strong>Per Kilometer Cost:</strong> ₹{per_km_cost} / KM</p>
        <p><strong>Total Petrol Needed:</strong> {total_petrol} L</p>
        <p><strong>Total Petrol Cost:</strong> ₹{petrol_cost}</p>
        <p><strong>Per Person Share:</strong> ₹{per_person}</p>
        <p><strong>Total Amount:</strong> ₹{total_amount}</p>

        <br><p>Thanks for using <strong>FuelShare</strong>!</p>
    </body>
    </html>
    """
    
        # Load sensitive info from environment variables
    smtp_user = os.getenv("MAIL_USERNAME")
    smtp_pass = os.getenv("MAIL_PASSWORD")
    smtp_host = os.getenv("MAIL_SERVER")
    smtp_port = int(os.getenv("MAIL_PORT", 465))  # default to 465 if not found

    msg = MIMEText(html_content, "html")
    msg["Subject"] = "Your FuelShare Budget Summary"
    msg["From"] = smtp_user
    msg["To"] = email

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as smtp:
            smtp.login(smtp_user, smtp_pass)
            smtp.send_message(msg)
        return True, "✅ Email sent successfully!"
    except Exception as e:
        return False, f"❌ Email sending failed: {e}"
