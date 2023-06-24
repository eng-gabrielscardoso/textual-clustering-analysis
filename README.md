# Textual Clustering Analysis

This project is a work requested for the discipline of Data Structures II taught in the Bachelor's Degree in information Systems at UFPA.

This works aims to provide the solutions for the problems encountered in the Section II of [requirements](src/assets/requirements.pdf) using the Python language and some strategies learned during the discipline.

## Technologies

In this project we use the following technologies:

- [Python3](https://www.python.org/)
- [PIP](https://pypi.org/project/pip/)
- [Autopep8](https://pypi.org/project/autopep8/)
- [Coverage](https://pypi.org/project/coverage/)
- [Pytest](https://pypi.org/project/pytest/)
- Git and Github

## Installation

### With installed SDK

If you have the installed SDK in your system just make sure that you have the same versions required for the project and setup in your IDE of preference (we recommend [Visual Studio Code](https://code.visualstudio.com/)).

### Docker

If you have the installed Docker in your system you can follow the instructions below to interact with application:

First, run the following command to build the image:

```bash
docker build -t app .
```

After build the image, run the following command to run the container with the application:

```bash
docker run -d app
```

Using the command above you can concatenate some common commands to interact with the application, since inside the container we have the exactly same environment that we have installed the SDK.

```bash
# e.g.
docker run app python src/main.py
```

### Docker Compose

If you have the installed Docker Compose in your system you can follow the instructions below to interact with application:

First, run the following command to build the Docker Compose image:

```bash
docker-compose up -d --force-recreate
```

After build the image, run the following command to run the container with the application:

```bash
docker-compose exec app <command>
```

Using the command above you can concatenate some common commands to interact with the application, since inside the container we have the exactly same environment that we have installed the SDK.

```bash
# e.g.
docker-compose exec app python src/main.py
```

## Packages

If you want to contribute with project we recommend install the dependencies inside [`requirements.txt`](requirements.txt). To use this packages you will need to update your `PATH` configuration. On Linux you should update your `.bashrc` including the following:

```bash
export PATH="$PATH:/home/${USER}/.local/bin"
```

After it, run the command `source` in your `.bashrc` to reload the configuration and then you will be able to use the packages binaries.

## Useful commands

### Running application

- Run application:

```bash
python3 src/main.py
```

### Lint

- Lint project with PEP8 specifications:

```bash
# -a: aggressively
# -i: make changes in file in-place
# -r: recursively
autopep8 -a -i -r .
```

### Test

- Run all tests:

```bash
pytest
# or
pytest .
```

- Run specific test:

```bash
# you must specify the path to the test
pytest tests/example_test.py
```

### Coverage

- Run tests with coverage:

```bash
coverage run -m pytest .
```

- Generate coverage report:

```bash
coverage report
```

## Authors

To see the list of authors, please go to [authors file](AUTHORS.md).

## Licence

This project is licenced under the MIT Licence. see [here](LICENSE.md).
