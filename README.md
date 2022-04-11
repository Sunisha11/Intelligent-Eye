# Intelligent Eye

## Requirements

1. python 3.x

## Setup

1. Create a new folder in your local system anywhere
2. Navigate to this new folder.
3. Create a virtual environment using below given commands.

```
$ pip install virtualenv
$ virtualenv env
```

4. Download the code file or clone the repository in this folder.
5. Activate the virtual environment.

```
$ source env/Scripts/activate
```

6. Install python packages mentioned in requirements.txt file using following command.

```
$ pip install -r Intelligent_Eye/requirements.txt
```

7. Note for Windows OS:
   You might face errors while running above command because of pyaudio library. To install pyaudio follow the steps mentioned here: https://stackoverflow.com/a/55630212/12025398

8. Note for Ubuntu users:
   You might also face similar issues. Simply run the following command:

```
$ sudo apt-get install portaudio19-dev python-pyaudio
$ pip install PyAudio
```

## How to run the code?

```
cd Intelligent_Eye
py main.py
```
