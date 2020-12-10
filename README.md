# trellocli

## About This Project
This is a cli utility which will allow the user to interact with trello board, this tool made it easy to add, update or delete objects on the Trello board.


### Built With

This tool uses Python3.x language and has some dependencies packages.

* [click](https://click.palletsprojects.com)
* [requests](https://requests.readthedocs.io)
* [pyyaml](https://pyyaml.org)
* [colorama](https://pypi.org/project/colorama)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may use the tool locally.

### Prerequisites

Those are the prerequisit is an example of how to install need to use the software and how to install them.
* python3
* pip
* virtualenv
   ```sh
   pip install virtualenv
   ```

### Installation

1. Get API Key from Trello (https://trello.com/app-key)
2. Generate a Server Token by clicking on Token withing this page (https://trello.com/app-key)
3. Clone the repo
   ```sh
   git clone https://github.com/trellocli.git
   ```

4. Change the directory to the trellocli folder
5. Create a virtual environment
   ```sh
   virtualenv venv
   ```
6. Enable the virtual environment
   ```sh
   source venv/bin/activate
   ```
7. Install the dependencies and package the tool.
   ```sh
    pip install -e .
    ```
8. Run trellocli if you see the output below it means you have successfully installed the cli.
   ```sh
   trellocli
Usage: trellocli [OPTIONS] COMMAND [ARGS]...

  Welcome to trellocli !!!

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  config
  create-board
  create-card
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).

