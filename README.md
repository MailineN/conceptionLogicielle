# 🍫🍫 Miam Miam le chocolat 🍫🍫
On peut séparer ce rendu de TP en deux parties : <br>
Les commandes pour lancer les différentes parties du TP doivent être exécutées depuis un terminal au choix de type terminal par défaut d'ubuntu, Alacritty (ou Powershell si après les 1000 heures de debug divers et variés du cours, vous n'avez pas compris que Windows c'est pas génial) <br>
### Partie webservice : 
Depuis la racine : <br>
``` $ cd Webservice ``` <br>
``` $ pip install -r requirements.txt ``` <br>
``` $ uvicorn main:app --reload ``` <br>
Sur un navigateur internet on va là : http://127.0.0.1:8000/docs#/ 

### Partie client: 
Depuis la racine : <br>
``` $ cd Client ``` <br>
``` $ pip install -r requirements.txt ``` <br>
``` $ python3 main.py ``` <br>
ou alors <br>
``` $ python main.py ``` <br>

### Tests unitaires:
Des tests unitaires (enfin un test unitaire pour une unique fonction) ont étés codés pour la partie Client <br>
Pour lancer ce test, on rentre depuis la racine : <br>
``` $python3 -m unittest tests/test_Clients.py  ``` <br>

### Automatisation des tests unitaires:
Les tests peuvent être automatisés avec Github Actions, pour cela, il faut lancer un environnement virtuel au sein du projet: <br>
On suppose que ```python3-venv``` est installé, sinon on lance la commande suivante sur ubuntu (Je ne sais pas pour windows désolée)
```sudo apt-get install python3-venv``` <br>
Pour lancer l'environnement virtuel on rentre depuis la racine : <br>
``` $python3 -m venv .env ``` <br>
``` $source .env/bin/activate ``` <br>
Et voilà!


### 🐼 Pour la fin 🐼
![alt text](https://raw.githubusercontent.com/MailineN/conceptionLogicielle/main/ImAPanda/pandaSpin.gif "Les pandas dominent le monde")
