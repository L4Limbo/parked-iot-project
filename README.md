# parked-iot-server

## Περιγραφή 
Το παρόν project αποτελεί το backend μέρος της εφαρμογής Parked η οποία αναπτύχθηκε στα πλαίσια του μαθήματος Διαδίκτυο των πραγμάτων (Internet Of Things) και προορίζεται για χρήση από κινητή συσκευή.
To backend λειτουργεί ως api για να παρέχει δεδομένα στο client μέρος της εφαρμογής

## Public Domain
Το project έχει ανέβει στην πλατφόρμα της Heroku: https://parked-iot-project.herokuapp.com/

## Client
Το frontend διατίθεται στο repository: https://github.com/L4Limbo/parked-iot-client

## Contributors
* Μητακίδης Ανέστης, Undergrad Student of ECE at the University of Patras. : https://github.com/L4Limbo
* Εμμανουήλ Τζαγάκης, Undergrad Student of ECE at the University of Patras. : https://github.com/Xenonas

# Οδηγίες Εγκατάστασης Backend
## Project Download
git clone https://github.com/L4Limbo/parked-iot-projetc.git
### Είσοδος στον φάκελο του project 
cd parked-iot-project

## Εγκατάσταση Python
Windows
https://www.python.org/downloads/windows/
Linux
sudo apt install python3
python3 --version
expected output: Python 3.x.x

## Δημιουργία Virtual Environment στην Python
Windows
python -m venv myvenv
myvenv\Scripts\activate
Linux και OS X
python3 -m venv myvenv
source myvenv/bin/activate
## Εγκατάσταση Django
python -m pip install --upgrade pip
## Εγκατάσταση Απαιτήσεων (μέσα στο Virtual Environment)
python -m pip install --upgrade pip
pip install -r requirements.txt
## Δημιουργία βάσης PostgreSQL
https://www.postgresql.org/docs/8.2/server-start.html
Προτείνεται κατά την εκτέλεση της εφαρμογής ο client να κάνει requests στο production (public) API, εφόσον υπάρχουν δυσκολίες στην δημιουργία της βάσης.

## Δημιουργία env file
Προκειμένου να τρέξει o client και να φορτωθούν οι χάρτες χρειάζεται να δημιουργηθεί ένα 
SECRET_KEY=[SECRET_KEY]
DB_HOST=[DB_HOST]
DB_NAME=[DB_NAME]
DB_USER=[DB_USER]
DB_PASS=[DB_PASS]

## Δημιουργία Μοντέλων 
python manage.py migrate
python manage.py makemigrations
## Εκκίνηση Server
Windows
python manage.py runserver
Linux
python3 manage.py runserver
```
Ο server τρέχει localhost στο port 8000 εφόσον αυτό δεν είναι απασχολημένο.

Πλέον ο server-api τρέχει και μπορούμε να ακολουθήσουμε τις οδηγίες του [client](https://github.com/L4Limbo/parked-iot-client#readme
) για να τρέξει η εφαρμογή