## Tame of Thrones Challenge

[![CircleCI](https://circleci.com/gh/sreenathmmenon/TameofThrones.svg?style=svg)](https://circleci.com/gh/sreenathmmenon/TameofThrones)

### Installation Instructions
1. Setup Virtual Environment

```
Command - virtualenv <name of env>
virtualenv venv
```
2. Activate the virtual environment

```
. venv/bin/activate
```
3. Enter into virtual environment
```
cd venv
```

4. Install the required dependencies/modules

```
pip install -r requirements.txt
```

5. Clone the project using github url

```
git clone https://github.com/sreenathmmenon/TameofThrones
```

6. Enter into project directory

```
cd TameofThrones
cd tameofthrones
```

7. Use flake8 and analyze the code for potential errors and confirmity to Python Standards

```
flake8 --exclude=venv* --statistics
```

8. Calculate the code coverage. We can also verify the test output from here.
```
pytest-cov
```

## Interactive Script and Output

* Run the interactive script for Tame of Thrones Challenge.

```
python tameofthrones.py
```

**Display of Initial Questions**

![Initial Questions](https://raw.githubusercontent.com/sreenathmmenon/TameofThrones/master/images/universe_ruler_part1.png)

**King Selection Option**

![King Selection option](https://raw.githubusercontent.com/username/TameofThrones/master/images/universe_ruler_part2.png)

**Option to Input Messages for Kingdoms**

![Message input option](https://raw.githubusercontent.com/username/TameofThrones/master/images/universe_ruler_part3.png)

**Displaying the victorious King Shan and his allies**

![King Shan and allies](https://raw.githubusercontent.com/username/TameofThrones/master/images/universe_ruler_part4.png)

**Case when none of the messages have been valid**

![Invalid Messages](https://raw.githubusercontent.com/username/TameofThrones/master/images/universe_ruler_part5.png)


### Configuring Continous Integration Build System based on CirecleCI

1. Following config file is used for setting up Continous Integration for the project.

```
# CirlceCI configuration file for Tame of Thrones
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:2.7

    working_directory: ~/repo

    steps:
      # Step 1: Obtain repo from GitHub
      - checkout
      # Step 2: Create virtual env and install dependencies
      - run:
          name: Install dependencies
          command: |
            #python2.7 -m venv venv
            virtualenv venv
            . venv/bin/activate
            pip install -r requirements.txt
      # Step 3: Run linter and tests
      - run:
          name: run tests
          command: |
            . venv/bin/activate
            flake8 --exclude=venv* --statistics
            pytest -v --cov=tameofthrones
```

**Config File Explanation**

##### Syntax
* Indentation - used for structure
* Colons - used to separate key value pairs
* Dashes - used to create lists

##### Config Entries
* version:

```
Each config.yml starts with the CircleCI version number. 
Used to issue warnings about breaking changes.
```

* jobs:

```
Represent a single build execution of the build. It's defined by a collection of steps. 
```

* build:

```
Build is the name of our job. When multiple jobs are present, they need to be given unique names.
```

* docker:

```
The steps of a job occur in an environment called an executor. The common executor in CircleCI is a Docker container.
It is a cloud-hosted execution environment.
```

* image:

```
A Docker image is a file used to create a running Docker container. We are using an image that has Python 2.7 preinstalled.
```

working_directory:

```
Working directory corresponds to the location on the build server where our repository will be checked out and stored.
```

* steps:

```
This marks the start of a list of steps that is to be performed by the build server.
```

* checkout:

```
The first step the server needs to do is check the source code out to the working directory. 
This is performed by a special step called checkout.
```

* run:
```
Executing command-line programs or commands is done inside the command key. 
The actual shell commands will be nested within.
```

* name:

```
The CircleCI user interface shows you every build step in the form of an expandable section.
The title of the section is taken from the value associated with the name key from config file.
```

* command:

```
This key represents the command to run via the shell. 
The | symbol specifices that what follows is a literal set of commands, one per line, similar to shell/bash script.
```

