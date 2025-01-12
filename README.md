# {{ app_name }}

{{ app_description }}

## Prerequisites

- Python 3.11+
- Poetry
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone {{ git_path }}
cd invoice-generator
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Running the Application

### Method 1: Using Poetry shell
1. Activate the Poetry shell:
```bash
poetry shell
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

### Method 2: Direct Poetry run
```bash
poetry run streamlit run app.py
```

### Method 3: Using Docker
1. Build the Docker image:
```bash
docker build -t {{ app_name }} .
```

2. Run the container:
```bash
docker run -p 8501:8501 {{ app_name }}
```

The application will be available at `http://localhost:8501`

## Project Structure

```
{{ app_name }}/
├── app.py          # Main Streamlit application
├── template.html       # Invoice HTML template
├── pyproject.toml      # Poetry dependency configuration
├── poetry.lock         # Poetry lock file
├── README.md           # Project documentation
├── Dockerfile          # Docker configuration
└── .gitignore          # Git ignore rules
```

## Usage

{{ usage }}