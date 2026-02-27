from invoke import task


@task
def run(c, host="127.0.0.1", port=8000):
    c.run(f"poetry run uvicorn app.main:app --reload --host {host} --port {port}")


@task
def lint(c):
    c.run("poetry run ruff check .")


@task
def fmt(c):
    c.run("poetry run ruff format .")


@task
def test(c):
    c.run("poetry run pytest -q")


@task
def check(c):
    fmt(c)
    lint(c)
    test(c)
