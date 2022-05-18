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

4. Now create a new folder here named 'Intelligent-Eye' and move into it.
5. Initialize git for Intelligent-Eye folder by using the command:

```
$ git init
```

6. Download the code file or clone the repository in this folder.

```
$ git clone 'https://github.com/SrishtiSingh2001/Intelligent-Eye.git'
```

7. Activate the virtual environment.

```
$ source env/Scripts/activate
```

8. Install python packages mentioned in requirements.txt file using following command.

```
$ pip install -r Intelligent_Eye/requirements.txt
```

9. Note for Windows OS:
   You might face errors while running above command because of pyaudio library. To install pyaudio follow the steps mentioned here: https://stackoverflow.com/a/55630212/12025398

10. Note for Ubuntu users:
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

## The workflow of the code
1. You need to activate our helping bot Drishti by calling her (just like Google Assistant). Console will print start for the first time, then you need to call Drishti by speaking phrases like 'Hello Drishti', 'Good morning Drishti', 'Help me Drishti', etc.
2. Drishti will get activated and now you can start with your queries like asking for decribing the road, reading the book or filling the form or time and many other things.
3. You can end the conversation by saying something like 'end the conversation' or 'Stop Drishti'. 



![image](https://user-images.githubusercontent.com/64425886/168954561-0f69da6a-ddb9-42d3-b5ed-6111f5628ec9.png)


