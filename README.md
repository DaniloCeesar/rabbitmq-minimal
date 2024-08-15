# RabbitMQ: Minimal Example

## Development & Testing

### Requirements

- **[Git](https://git-scm.com/)** — free and open source distributed version control system.
- **[Docker](https://www.docker.com/)** — accelerated container application development.
- **[Python](https://www.python.org/)** — easy to learn, powerful programming language.
- **[pip](https://pypi.org/project/pip/)** — package installer for Python packages.

### Build instructions

1. `git clone https://github.com/DaniloCeesar/rabbitmq-minimal.git` — clone this repository into a new directory;
2. `cd rabbitmq-minimal` — change the current directory to this project source code;
3. `pip install -r requirements.txt` — install the dependencies from the `requirements.txt` file into the project's folder;
4. `FLASK_APP=publisher.py flask run` — run the development server. The URL address and port will be displayed on your terminal.

## Usage

Instantiate a _container_ for using RabbitMQ:

`$ docker run --rm -it --hostname rabbitmq-minimal -p 15672:15672 -p 5672:5672 rabbitmq:3-management`

Send a new message to the Flask server. There is an example in the `send_message.js` script file.

Start consuming the new messages:

`$ python consumer.py`

The messages will be displayed on your terminal.
