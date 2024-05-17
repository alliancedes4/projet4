# Changelog 

Files in this directory are used to track the changes made to the project
at each mentorship session.

## 2024-05-17 Mentorship Session

### Added
- code for class Tournoi
- delete le copier coller de la classe ronde qui n'etait pas bon

### Updated
- added comments in tournous  create_rounds== > prototype de la methode
- light update of tournois  (crud functions find by , save ....)

### Todo
* MUST HAVE : 
    - créer la classe ronde - tester et valider classe ronde 
    - ecrire le code qui correspond à la methode create_rounds en fonction des commentaires 
        * ecire les rondes 
        * les créer en bdd 
        * les save  
        * ...
        
* NICE TO HAVE : 
    - attaquer get_current_round et update_round

## 2024-04-03  Mentorship Session

### Added 
- new methods for reboot db
- test IPYTHON for all player methods ==> All OK 
- update tests 

### TODO 
- Implement same BUT For tournois
- When all methods for tournois : ==> add new methods : "add_player_to_tournoi" and "change_status" (from created to started, to finished), and "next_round"
- Deeply think about our Tournois class => what are the attributes, what are the methods, what are the relations with other classes => what logic should be implemented in the class?

## 2024-03-27 (done 03-02) Mentorship Session

### Added 

- Test functions for player 
- Add secrest to have random id name ect etc 
- Add a place holder for data storage 
- Add place holder in the joueur class

### Upated

- moove imports
- rename file player.json
- do not trach data (*.json)

- use db.all() for load functions


### Todo


#### Must have

- Understand class and static methods
- fix load
- write search_by_id
- is Jouer is OK, write the Tournoi class (same pattern)

#### Nice to have


## 2024-03-21 Mentorship Session

### Added
- tinydb to requirements .txt 
- placehoders sections in the readme 
- .utils/ to store various utils
- docs and ressources folder 
- .gitignore file
- created .utils to store various utils (*requirements.freeze*)
- Added a tests folder to store the tests (*for later*)

### Updated 
- Due to merge problem re write manually all the code
- restruct folder creating a chess/ main package
- Practice test PR
- restruct folder creating a chess/ main package
- updated the readme with the new structure
- Add placeholders methods in the Jouer class


### TODO
#### Must Have (Ce qu'il faut faire)
- [ ] Be able to store a player in json format using tinydb package
    - [ ] Main work on Joueur class
    - [ ] Learn how to use tinydb
    - [ ] Implement tiny db 
    - [ ] Store a player in json format with tinydb

#### Nice to Have (Ce qui serait bien de faire - mais qu'on ne fera pas forcément)
- [ ] Translate code et comments in english
- [ ] Write tests for the Player class


## 2024-03-11 - Mentorship Session

### Added
- tinydb to requirements .txt 
- placehoders sections in the readme 
- .utils/ to store various utils
- docs and ressources folder 

### Updated
- restruct folder creating a chess/ main package


### Todo