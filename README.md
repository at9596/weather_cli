# Weather CLI App

A simple command-line weather application built with Python.

This project helps beginners learn:
- API integration
- HTTP requests
- JSON parsing
- Environment variables
- CLI development with argparse
- Error handling

---

# Features

- Search weather by city
- Current temperature
- Weather condition
- Humidity
- Wind speed
- Environment variable support
- Error handling

---

# Project Structure

```bash
weather_cli/
│
├── weather.py
├── .env
├── requirements.txt
└── README.md
```

---

# Requirements

- Python 3.8+

Check Python version:

```bash
python --version
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/at9596/weather_cli
```

Move into project directory:

```bash
cd weather_cli
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

## Linux / macOS

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
requests
python-dotenv
```

---

# Setup API Key

Create a free API key from:

https://openweathermap.org/api

Create `.env` file:

```env
API_KEY=your_api_key_here
```

---

# Usage

## Get Weather

```bash
python weather.py Delhi
```

---

# Example Output

```bash
Weather in Delhi
------------------------------
Temperature : 38°C
Condition   : haze
Humidity    : 42%
Wind Speed  : 3.5 m/s
```

---

# Example Code Concepts

This project covers:

- argparse
- requests
- dotenv
- JSON parsing
- API integration
- Error handling
- Environment variables

---

# Future Improvements

Possible enhancements:

- 5-day forecast
- Multiple unit support
- Weather icons
- Colored terminal output
- Table formatting
- Async requests
- Docker support
- Unit testing
- City search history

---

# Tech Stack

- Python
- requests
- python-dotenv
- OpenWeather API

---

# Author

Abhishek Tanwar