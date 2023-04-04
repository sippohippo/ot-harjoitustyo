
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