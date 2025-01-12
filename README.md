# Test BQ write truncate

Test doing write truncate with the edited dataframe provided by streamlit

## Prerequisites

- Python 3.11+
- Poetry
- Bigquery service account
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

3. Create file `secrets.toml` according to the template `secrets.toml.example` and fill in the credential

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
docker build -t bq-write-truncate .
```

2. Run the container:
```bash
docker run -p 8501:8501 bq-write-truncate
```

The application will be available at `http://localhost:8501`

## Project Structure

```
bq-write-truncate/
├── app.py          # Main Streamlit application
├── template.html       # Invoice HTML template
├── pyproject.toml      # Poetry dependency configuration
├── poetry.lock         # Poetry lock file
├── README.md           # Project documentation
├── Dockerfile          # Docker configuration
└── .gitignore          # Git ignore rules
```

## Concern

1. The secrets is not tested in docker
2. If the validation failed, user can still click Sync Table To BQ, but without the failed validation column