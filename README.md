# Psychotherapy AI Bot
An interactive chatbot for individuals who need someone to talk to
## GitHub Repository Setup

This repository contains the following files and folders:

1. Folder: **services**  
   - File: cohere_service.py
   - File: openai_service.py
   - File: pinecone_service.py

These files correspond to partner services that we used in our project. To utilize the API for each service, follow the instructions below.

## API Setup

1. Open the file **openai_service.py**.
2. Locate the designated area for the API and paste your API credentials.

3. Open the file **pinecone_service.py**.
4. Locate the designated area for the API and paste your API credentials.

## SQLITE Installation

To use the SQLite database, please follow these instructions:

1. Install SQLite. Make sure to install it in the C: drive.

## Requirements Installation

To install the required packages for this project, run the following command:

```
pip install -r requirements.txt
```

## Database File Location

In the following files, replace the existing database file path with the location of the `database.db` file:

1. File: **create_db.py**  
   - Replace the line: `conn=sqlite3.connect('C:\\Users\\User\\Desktop\\language\\EDITH_MENTAL_HEALTH\\database.db')`

2. File: **app.py**  
   - Replace the line: `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\User\\Desktop\\language\\EDITH_MENTAL_HEALTH\\database.db'`

Make sure to provide the correct path to the `database.db` file in both files.

## Running the Project

To run the project, execute the following command:

```
python app.py
```

Once you have completed the above steps and executed the command, the project should start running successfully.
