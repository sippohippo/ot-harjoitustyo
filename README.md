
# Gym Training App (Ohjelmistotekniikka-repo)

The primary purpose of this app is to allow a user to record what exercises they have done at a gym and to track how they have developed overtime in terms of the weights and repetitions. No ads, no unnecessary features, just a pure elegant and functional gym diary. 

## Releases

[V1 Release](https://github.com/sippohippo/ot-harjoitustyo/releases/tag/viikko5), published on week 5 of the course


## Documentation

[Software requirements specification](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Timesheet](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/timesheet.md)

[Changelog](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Architecture](https://github.com/sippohippo/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Installation and setup

1. Clone this repository as shown below (or download the release)

```bash
git clone https://github.com/sippohippo/ot-harjoitustyo
```

2. Go to the newly created directory (or unpack the downloaded release zip file and go to its directory)

```bash
cd ot-harjoitustyo
```

3. Install dependencies

```bash
poetry install
```

4. Initialize the database

```bash
poetry run invoke build
```

5. Start the program

```bash
poetry run invoke start
```

## Other command line functionalities

### Run tests

```bash
poetry run invoke test
```

### Generate a test coverage report

```bash
poetry run invoke coverage-report
```

### Check that the code follows the format specified with Pylint

```bash
poetry run invoke lint
```

## What is this?

This is a repository for my submissions in the University of Helsinki course *Ohjelmistotekniikka / Software Development)* (**2023 spring edition**)

You can find the course materials [here](https://ohjelmistotekniikka-hy.github.io). 

