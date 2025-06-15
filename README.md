# SA: Phase 4 Code Challenge: Superheroes 

An API for tracking heroes and their superpowers using Flask, SQLAlchemy, and RESTful routes. This project allows interaction with data about superheroes, their powers, and the strength of each superhero's individual powers.

---

## 🗂️ Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Badges](#badges)

---

## 📘 Project Description

This project implements an API for managing a list of **Heroes**, their **Powers**, and the **strength** of each hero-power association. The project is built with **Flask**, using **SQLAlchemy** for ORM, and includes proper serialization, validations, and error handling.

---

## 🧪 Installation

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/superheroes-api.git
   cd superheroes-api
## Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate  

## Install dependencies:

pip install -r requirements.txt


## Run migrations:


flask db init
flask db migrate
flask db upgrade
Seed the database:

## Seed the database
python seed.py

## Start the development server:

python app.py

🚀 Usage
Once the server is running at http://127.0.0.1:5000, use Postman or curl to interact with the following routes.

Postman Collection: Download Here

🔁 Routes
✅ GET /heroes
Returns a list of all heroes.

✅ GET /heroes/:id
Returns a single hero with their powers. Returns error if not found.

✅ GET /powers
Returns a list of all powers.

✅ GET /powers/:id
Returns a single power. Returns error if not found.

✅ PATCH /powers/:id
Updates a power’s description. Requires at least 20 characters.

✅ POST /hero_powers
Creates a HeroPower link between a hero and a power, with a strength value (Strong, Weak, Average).



👥 Contributing
Contributions are welcome! Here's how you can help:

1. Fork the repository

2. Create your feature branch: git checkout -b my-feature

3. Commit your changes: git commit -m 'Add some feature'

4. Push to the branch: git push origin my-feature

5. reate a pull request

Please follow standard Python conventions and ensure your changes pass linting and tests.

## Credits
Starter code and inspiration from Flatiron School

Superhero data: fictional dataset for academic use

Postman collection: provided by the instructor

##  License
This project is licensed under the MIT License.