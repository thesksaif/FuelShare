# 🚗 FuelShare — Smart Travel Fuel Split Calculator

![FuelShare Screenshot](screenshot.png)

FuelShare is a **Flask-based full-stack web application** that calculates and shares fuel cost summaries for group travel. Enter trip details (distance, mileage, fuel rate, people count) and instantly get a breakdown emailed to you — all securely and beautifully rendered.

> 🟢 **Live Demo**: [https://fuelshare.webspidy.in](https://fuelshare.webspidy.in)

---

## 🔥 Why This Project Matters

This app solves a real problem — quickly splitting travel fuel costs among people. It showcases **practical full-stack development** including:

- 💻 Backend logic with Python Flask
- 🧠 Secure email integration with SMTP
- 🧾 Dynamic HTML templating with Jinja2
- 📩 Environment-based credential management
- 🎨 Custom responsive UI
- 🧪 Production-ready structure and deployment

---

## 🧪 Features

- 🔢 Input: distance, car average, fuel price, total persons
- 📊 Output: cost per km, fuel needed, per-person share
- 📬 Automatic email summary using secure SMTP (via Hostinger)
- 💡 .env-based credential protection
- ⚙️ Clean modular structure (`utils/`, `templates/`, `static/`)

---

## 📸 Screenshot

![FuelShare UI Preview](screenshot.png)

---

## 🛠️ Tech Stack

| Layer     | Technologies Used                       |
|-----------|------------------------------------------|
| Frontend  | HTML, CSS, custom styles (no framework) |
| Backend   | Python, Flask                           |
| Email     | `smtplib`, `email.mime`, `ssl`, Hostinger SMTP |
| Config    | `python-dotenv` for secure `.env` usage |
| Hosting   | Live at Hostinger (`fuelshare.webspidy.in`) |

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/thesksaif/FuelShare.git
cd FuelShare

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Create your environment file
cp .env.example .env
# Then edit `.env` to add your email credentials

# Run the server
flask run
