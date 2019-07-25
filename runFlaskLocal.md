# Clone github repo
git clone https://github.com/ddkingsley/3308_project_repo.git

## cd into project repo
cd 3308_project_repo

#######################################
# Mac:
## install venv, creates venv folder
python3 -m venv venv

## activate venv
source venv/bin/activate

## install dependencies
pip install -r requirements.txt

## run flask locally
flask run

########################################
# Windows
## install venv, creates venv folder
python3 -m venv venv

## activate venv
venv/Scripts/activate

## install dependencies
pip install -r requirements.txt

## run flask locally
flask run

#########################################
# Initialize local database
flask init-db

