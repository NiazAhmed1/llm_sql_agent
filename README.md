# SQL Agent on Chinook Database

## Overview

This project implements an **SQL Agent** using **LangChain** to interact with the **Chinook** database. The agent processes natural language queries, converts them into SQL queries, executes them on the database, and returns structured responses.

## Features

- **Automated SQL Query Generation**: Converts natural language questions into SQL queries.
- **Database Interaction**: Queries the Chinook database (SQLite format).
- **LLM-Based Explanation**: Uses an LLM to explain query results in natural language.
- **Testing Framework**: Includes predefined questions and expected answers for validation.

## Repository Structure

```plaintext
llm_sql_agent/
│-- chinook.db            # SQLite database file
│-- main.py               # Main script implementing the SQL agent
│-- requirements.txt      # List of required Python libraries
│-- test_Q&A.json         # JSON file with test questions and answers
│-- README.md             # Project documentation
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/NiazAhmed1/llm_sql_agent.git
cd llm_sql_agent
```

### 2. Install Dependencies

Ensure you have **Python 3.8+** installed, then run:

```sh
pip install -r requirements.txt
```

### 3. Run the SQL Agent

```sh
python main.py
```

This will:

- Load the **Chinook database**
- Display the database schema
- Run sample queries and output the results

## Example Queries

The agent can answer questions like:

- **"How many employees are there?"**
- **"What is the most popular music genre by number of tracks?"**
- **"Find the most expensive track in the database."**
- **"List all the albums by artists with 'black' in their name."**

## Testing

The `test_Q&A.json` file contains test cases for validating the agent’s responses. You can extend it to add more test cases.

## License

This project is open-source and available under the **MIT License**.

---

Feel free to contribute by submitting issues or pull requests!
