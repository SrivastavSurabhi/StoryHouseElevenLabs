# storyhouse

## Technical Requirements
- [Python](https://www.python.org/downloads/)(Python 3.10.5)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtual environment](https://docs.python.org/3/library/venv.html)
- [Wkhtmltopdf](https://wkhtmltopdf.org/).

## Getting Started Instructions
Make sure that your project contains media folder with following paths:
 
- /media/home/esmee/mouthpiece/ebooks
- /media/home/esmee/mouthpiece/htmls
- /media/home/esmee/mouthpiece/text
- /media/home/esmee/mouthpiece/mp3s
- /media/home/esmee/mouthpiece/pdfs
- /media/home/esmee/mouthpiece/summaries
- /media/userprofile

Note: If not present then create a folder media inside the directorary 'storyhouse' and then create inside folders as mentioned above
## Installation
Write these commands in terminal

1. create virtual environment

For Windows run:
```sh
py -m pip install --upgrade pip

py -m pip --version

py -m pip install --user virtualenv

py -m venv storyHouse_env

.\storyHouse_env\Scripts\activate
```


For Unix/macOS run:
```sh
python3 -m pip install --user --upgrade pip

python3 -m pip --version

python3 -m pip install --user virtualenv

python3 -m venv storyHouse_env

source storyHouse_env/bin/activate
```

2. Change Directory:
```sh
cd storyhouse
```
3. Install requirements:
```sh
pip install -r requirement.txt
```
4. Run Migrate command:
```sh
python manage.py migrate
```
5. Run command to create superuser :
```sh
python manage.py createsuperuser
```
```
Then enter username , email and password
```
7. Now you are ready to go:
```sh
python manage.py runserver
```
