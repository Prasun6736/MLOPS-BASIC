create env
```bash
conda create -n simple
```
activate env
```bash
conda activate simple
```
create a requirement file
```bash
pip install -r requirements.txt
```
git init

dvc init

dvc add dataset/winequality.csv

git add .

git commit -m "xyz"

git remote add origin https://github.com/Prasun6736/MLOPS-BASIC.git

git branch -M main

git push origin main

tox command
```bash
tox
```
pytest command
```bash
pytest -v
```
setup-
```bash
pip install -e .
```
building own package
```bash
python setup.py sdist bdist_wheel
```