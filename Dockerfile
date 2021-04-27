FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 AS test-api-server
ENV APPDIR /app
WORKDIR ${APPDIR}
COPY . ${APPDIR}
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
