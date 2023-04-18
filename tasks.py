
from invoke import task


# start, this is still a placeholder

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

# testing

@task
def test(ctx):
	ctx.run("pytest src", pty=True)

# Run tests and get coverage

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=True)

# Generate a coverage report

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html", pty=True)

# Correct formatting

@task
def format(ctx):
	ctx.run("autopep8 --in-place --recursive src")

# Check Pylint

@task
def lint(ctx):
	ctx.run("pylint src")

# Initialize database

@task
def build(ctx):
	ctx.run("python3 src/database.py")