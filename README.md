# Smart Nutrition API powered by AI
## About
The Smart Nutrition API (S.N.A.P.I) is a versatile RESTful API Powered by Artificial Intelligence that can been consumed
and used by any application that supports JSON-RPC protocol such as Mobile Applications, JavaScript Application such as
browser Extensions, for users who are conscious about the foods their consume, whether they are following a meal plan
provide by a Nutrition specialist due to health complications, or they are trying to change their lifestyle by watching
or keeping track of their daily macros.

SNAPI is trained to recognize different kinds of foods consumed by humans and works by allowing Applications to feed it
various kinds of raw data such images, voice prompts and text prompts (constrained to human food), depending on the type
of information given, SNAPI then uses either image processing to analyze the image and categories the type of food
contained in the image (e.g Banana). It then takes that data and compose a phrase such as “Nutritional Value in a Banana”, to
which the phrase is then posed to ChatGPT API, and receives a response that is further analyzed and returned to the
consumer/client of the API as a JSON response.

## Project Setup
Under the hood, SNAPI uses FastAPI to handle requests
### Requirements (Windows 10 or Later)
- [Visual Studio Code](https://code.visualstudio.com/download) OR [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)
- [Python 3.10](https://www.python.org/downloads/release/python-31013/)
- [Postgres 14](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- [pgAdmin](https://www.pgadmin.org/download/pgadmin-4-windows/)
- [Postman](https://www.postman.com/downloads/)

## Python Virtual Environment
### Windows ONLY Setup
#### To avoid complications,  use Git Bash to execute the following commands on Windows
install the virtual environment
```bash
python -m venv venv
```

activate your newly install virtual environment

```bash
source venv/Scripts/activate
```

install python packages in the requirements.txt file by using PIP

```bash
pip install -r requirements.txt
```

To run the project type

```bash
uvicorn app.main:app --reload
```
### Unix/Linux ONLY Setup
install the virtual environment
```bash
python3 -m venv venv
```

activate your newly install virtual environment

```bash
source venv/bin/activate
```

install python packages in the requirements.txt file by using PIP

```bash
pip3 install -r requirements.txt
```

To run the project type

```bash
uvicorn app.main:app --reload
```


## Database Migrations
*sample data is already provided inside app/database/snapidb.db, and the application by default connects to it*

### Proceed with this section only have if you have a fresh install of the database
#### Running the migrations
This command will  create all the necessary database tables, BUT will NOT seed any data, 
it's your responsibility to do that, just as it is to config a new database connection.
```bash
alembic upgrade head
```

## Roadmap
The future of SNAPI will be trained to allow it to accept request in various formats such as voice prompts and text prompts (constrained to human food),
depending on the type of information given, SNAPI will then use Natural Language Processing (NLP) to process Voice and Text (e.g “How many
calories are in this Banana”). It then takes that data and compose a phrase such as “Nutritional Value in a Banana”, to
which the phrase is then posed to ChatGPT API, and receives a response that is further analyzed and returned to the
consumer/client of the API as either JSON response or voice output using NLP.
