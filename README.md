# KIC Education

## Installation

1. Create virtual environment

```bash
python3 -m venv .venv
```

2. Activate virtual environment

```bash
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Setup environment variables

   View `.env.example` file

5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Seed development database

```bash
python manage.py seed_data
```
