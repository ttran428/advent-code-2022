FROM python:3.9-slim
WORKDIR /aoc

prod-deps:
    RUN pip install poetry==1.1.7
    RUN python -m venv /venv
    COPY pyproject.toml poetry.lock ./
    RUN . /venv/bin/activate && poetry install --no-dev --no-root
    SAVE ARTIFACT /venv

test-deps:
    FROM +prod-deps
    RUN . /venv/bin/activate && poetry install --no-root
    SAVE ARTIFACT /venv

prod:
    COPY +prod-deps/venv /venv
    COPY main.py ./
    COPY data/ data/
    COPY aoc/ aoc/
    RUN . /venv/bin/activate && python main.py aoc.day2 data/day2.data

test:
    COPY +test-deps/venv /venv
    COPY aoc/ aoc/
    COPY tests/ tests/
    RUN . /venv/bin/activate && python -m pytest

