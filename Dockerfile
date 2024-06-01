# syntax=docker/dockerfile:1

FROM python:3.11

#======================#
# install dependencies #
#======================#

WORKDIR /code

COPY . .

RUN PYTHONDONTWRITEBYTECODE=1 pip install -U --no-cache-dir -r requirements.lock

#=====================#
# run the application #
#=====================#

EXPOSE 3100

WORKDIR /code/src

CMD ["gunicorn", "-c", "/code/gunicorn.conf.py", "fastapi_sandbox.main:app"]
