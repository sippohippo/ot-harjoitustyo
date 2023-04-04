
from invoke import task

# Run tests and get coverage

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=True)

# Generate a coverage report

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html", pty=True)