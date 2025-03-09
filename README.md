# FC Barcelona Merchandise Web App

## Overview
This web application is built using Python Django and provides a platform for managing FC Barcelona merchandise, including jerseys and accessories. Users can add, edit, and delete items with a seamless and user-friendly interface.

## Features
- **Jersey Management**: Add, edit, and delete jerseys with images and prices.
- **Accessories Page**: Manage accessories like keychains, mugs, and more.
- **Navigation Bar**: Navigate through Home, Jerseys, Accessories, About, and Contact pages.
- **About Page**: Information about the platform.
- **Contact Page**: Users can send messages through a form and find LinkedIn & GitHub links.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django database)

## ⚙️ Installation & Setup
### Prerequisites
Ensure you have Python installed:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Adi1exe/TheBarcaStore.git
cd TheBarcaStore
```

###2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```
###3️⃣ Install Dependencies
```bash
pip install django
pip install pillow
--OR--
pip install -r requirements.txt
```
### 4️⃣ Run Migrations & Start Server
```sh
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## How to Use
1. Navigate to the Jerseys or Accessories page.
2. Add new items using the provided form.
3. Edit or delete existing items as needed.
4. Visit the About page to learn more about the project.
5. Use the Contact page to send a message.

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is open-source under the MIT License.

---

### Contact
- **GitHub**: [Your GitHub](https://github.com/Adi1exe)
- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/aditya-dolas-992a44265/)

