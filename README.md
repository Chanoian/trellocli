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
   Welcome to trellocli !!!
   ```



<!-- USAGE EXAMPLES -->
## Usage

1. #### trellocli -h
   will show the help menu

2. #### trellocli --version
   will print out the version

3. #### trellocli config
   Mandatory command to configure your API_KEY and SERVER_TOKEN, It will store the information as yaml file with the same directory.

4. #### trellocli create-board -n myboard
   will create a Trello Board with the name myboard

5. #### trellocli create-card --board myboard --list Doing --title mycard
   Will create a card in specific board and specific list with given title.
   -- comment : Optional argument if you want to add comment to the card.
   -- label : Optional argument , if you want to label the card.



<!-- ROADMAP -->
## Roadmap - TODO List
1. need to move the .trello.cfg file from the source code directory to the user directory ~/.trello.cfg since it's more secure if the configuration files exists within the user directory.
2. need to add more functionalities to the cli like remove card , remove board .. etc
3. enhance the exception handling to make it more clear to the user when an error occur.
4. need to add unit testing to this project 

