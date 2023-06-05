FROM python:3.10-slim

WORKDIR /electrosales_net/

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8000

CMD python3 ./manage.py runserver 0.0.0.0:8000

