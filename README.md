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

4. Clone the project using github url

```
git clone https://github.com/sreenathmmenon/TameofThrones
```

5. Install the required dependencies/modules

```
cd TameofThrones
pip install -r requirements.txt
```

6. Enter into project directory

```
cd tameofthrones
```

7. Use flake8 and analyze the code for potential errors and confirmity to Python Standards

```
flake8 --exclude=venv* --statistics
```
8. Execute unittests and verify the results

```
python -m unittest -v test_tameofthrones
```

9. Calculate the code coverage. We can also verify the test output based on pytest module from here.

```
pytest -v --cov=tameofthrones
```

## Interactive Script and Output

* Run the interactive script for Tame of Thrones Challenge.

```
python tameofthrones.py
```

**Display of Initial Questions**


![Initial Questions](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/universe_ruler_part1.png)

**King Selection Option**

![King Selection option](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/universe_ruler_part2.png)

**Option to Input Messages for Kingdoms**

![Message input option](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/universe_ruler_part3.png)

**Displaying the victorious King Shan and his allies**

![King Shan and allies](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/universe_ruler_part4.png)

**Case when none of the messages have been valid**

![Invalid Messages](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/universe_ruler_part5.png)


### Continous Integrations Status

![CI Status](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/continous_integration_circleci.png)


### Configuring Continous Integration Build System based on CirecleCI

Latest CI build status can be checked from the following location:

Ref: [Latest CI Build Details](https://circleci.com/gh/sreenathmmenon/TameofThrones)

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
The value corresponding to the name key will be shown as the title for every build step in CircleCI user interface.
```

* command:

```
This key represents the command to run via the shell. 
The '|' symbol specifies that what follows is a literal set of commands, one per line, similar to shell/bash script.
```

**Sample automated setup file**

File name - sample_build.sh

Can be used when all the required python modules are already present in our environment.

```
chmod + x sample_build.sh
```

All the modules that are required for correct functioning of this project have been specified in the requirements.txt file.

### Test Outputs


![Output 1](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/test_output1.png)


![Output 2](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/test_output2.png)


![Output 3](https://github.com/sreenathmmenon/TameofThrones/blob/master/images/test_output3.png)
