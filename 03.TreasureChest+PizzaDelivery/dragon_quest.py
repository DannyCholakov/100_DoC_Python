import time

book_of_the_dragon = False
dragon_armor = False
crimson_sword = False
items_equipped = False

print(r"""
                              ==(W{==========-             /===-                       
                                ||  (.--.)         /===-_---~~~~~~~----__      
                                | \_,|**|,__      |===-~___            _,-'`    
                   -==\ \       `\ ' `--'   ),    `//~\ \  ~~~~`--._.-~        
               ______-==|        /`\_. .__/\ \    | |  \ \         _-~`           
         __--~~~  ,-/-==\ \     (   | .  |~~~~|   | |   `\       ,'                  
      _-~       /'    |  \ \    )__/==0==-\<>/   / /      \     /                  
    .'        /       |   \ \     /~\___/~~\/  /' /        \   /              
   /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                
  /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                 
                    \_|      /        _) | ;  ),   __--~~                      
                      '~~--_/      _-~/- |/ \   '-~ \                       
                     {\__--_/}    / \ \_>-|)<__\     \                        
                     /'   (_/  _-~  | |__>--<__|      |                       
                    |   _/) )-~     | |__>--<__|      |                        
                    / /~ ,_/       / /__>---<__/      |                       
                   o-o _//        /-~_>---<__-~      /                     
                   (^(~          /~_>---<__-      _-~                      
                  ,/|           /__>--<__/     _-~                        
               ,//('(          |__>--<__|     /                  .--_     
              ( ( '))          |__>--<__|    |                 /' _-_~\    
           `-)) )) (           |__>--<__|    |              /'  /   ~\`\  
          ,/,'//( (             \_ >--<__\   \            /'  //      ||  
        ,( ( ((, ))              ~-__>--<_~-_  ~--__---~'/'/  /'       VV
      `~/  )` ) ,/|                 ~-_~>--<_/-__      __-~ _/
    ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~__--~
     ;'( ')/ ,)(                              ~~~~~~~~                    
    ' ') '( (/                                                            
    """)
print("**********___________DRAGON QUEST___________**********")
print('You mission is to tame your own dragon!')

def wrong_input():
    print("Wrong Input")
    print('Start again')

def game_over():
    print('Game Over!')
    exit()

def castle():
    print('You go inside the castle. Inside it looks even older than on the outside.')
    time.sleep(2)
    armor = input('You see a a dead knight. Do you take his Dragon Armor? Y or N: ')
    time.sleep(2)
    if armor.lower() == 'n':
        print('You don\'t take the sword and leave the castle where you see a Fire Gargoyle that eats you!')
        game_over()
    elif armor.lower() == 'y':
        print('You have the Dragon Armor!')
        time.sleep(1)
        print("You put on the Dragon Armor and go outside the castle where you see Fire Gargoyle flying over you.")
        time.sleep(1)
        fight = input('Do you run or stay and fight? Run or Fight: ')
        if fight.lower() == 'run':
            print('The Fire Gargoyle starts firing at you with his fireballs but you wear the Dragon Armor and take no damage and escape.')
            time.sleep(2)
            print('You go back on your path.')
            time.sleep(2)
        elif fight.lower() == 'fight':
            print('The Fire Gargoyle starts firing at you with his fireballs but you wear the Dragon Armor and take no damage.')
            time.sleep(2)
            print('The Fire Gargoyle gets angry and flies down on you and eats you!')
            game_over()
        else:
            wrong_input()
    else:
        wrong_input()

def field():
    print('You get to the field and see a small house.')
    house = input('Do you go inside the house? Y or N: ')
    if house.lower() == 'n':
        print('You decide to look around the field. Suddenly and eagle sees you and start attacking!')
        print("The eagle starts attacking your naked skin and you Die")
        game_over()
    elif house.lower() == 'y':
        book = input('You get inside the house and see a book. Do you open it? Y or N: ')
        if book.lower() == 'n':
            print('You leave the house and suddenly something inside pulls you in and kills you!')
            game_over()
        elif book.lower() == 'y':
            print('You start reading the book. Inside of it you read about a spell that can tame a Dragon, but for it you will need to have 3 items!')
            time.sleep(2)
            print('The Book of the Dragon, The Dragon Armor and the Dragon Crimson Sword')
            time.sleep(2)
            print('You have the Book of the Dragon!')
            time.sleep(2)
            print('You go back on your path.')
            time.sleep(2)
        else:
            wrong_input()
    else:
        wrong_input()

def cave():
    cave_choice = input('You go inside the cave.There are 2 paths which do you take? Left or Right: ')
    if cave_choice.lower() == 'left':
        print('You see a giant bolder!')
        time.sleep(2)
        print("IT'S a GOLEM")
        time.sleep(2)
        print('The golem smashes you around!')
        game_over()
    elif cave_choice.lower() == 'right':
        sword = input('In front of you there is a sword inside a rock. Do you pull it out? Y or N: ')
        if sword.lower() == 'n':
            print('Suddenly a giant Golem comes from behind and smashes you around!')
            game_over()
        elif sword.lower() == 'y':
            print('You take the sword out of the rock. Suddenly a giant Golem comes from behind attacks you!')
            time.sleep(2)
            print('You use the sword which pierces directly trough the Golem and kills it!')
            time.sleep(2)
            print('You have the Crimson Sword!')
            time.sleep(2)
            print('You go back on your path.')
        else:
            wrong_input()
    else:
        wrong_input()

begin_game = input('Are you ready? Y or N: ')

if begin_game.lower() == 'n':
    print('Sorry to hear that you are scared!')
    game_over()
elif begin_game.lower() == 'y':
    print("You wake up in a forest near a lake.")
    time.sleep(2)
    look_around = input('Would you look around? Y or N: ')

    if look_around.lower() == 'n':
        print('You got eaten by a wolf!')
        game_over()
    if look_around.lower() == 'y':
        answer = input('You see that there is a bridge in front of you.Do you wish to cross it? Y or N: ')
        time.sleep(2)
        if answer.lower() == 'n':
            print('A mountain wolf jumps on top of you and kills you!')
            game_over()
        if answer.lower() == 'y':
            print('You get on the bridge right before a wolf can jump on you from behind.')
            time.sleep(2)
            print('You get to the other side and see an old castle, a big field and a cave.')

            while not (dragon_armor and book_of_the_dragon and crimson_sword):

                place_to_visit = input('Where do you want to go? Castle, Field or Cave: ')

                if place_to_visit.lower() == 'castle' and dragon_armor == False:
                    castle()
                    dragon_armor = True

                if place_to_visit.lower() == 'field' and book_of_the_dragon == False:
                    field()
                    book_of_the_dragon = True

                if place_to_visit.lower() == 'cave' and crimson_sword == False:
                    cave()
                    crimson_sword = True

        print('You have all the relics!')
        time.sleep(2)
        print('Suddenly the dragon Red Dread appears.')
        time.sleep(2)
        choice = input('Do you attack him or use the 3 legendary items? Attack or Tame: ')
        if choice.lower() == 'tame':
            print('You put the book on the ground and pierce it with your sword releasing the dragon from his pain!')
            time.sleep(2)
            print('Red Dread is in your debt and becomes your loyal friend and servant!')
            time.sleep(2)
            print('You achieved the title: DRAGON LORD!')
            time.sleep(2)
            print('Congratulations you won!')
            print('Game over!')
            exit()
        elif choice.lower() == 'attack':
            print('You charge forward with your sword and pierce the dragon!')
            time.sleep(2)
            print('Red Dread roars in relief and dissolves...')
            time.sleep(2)
            print('You achieved the title: DRAGON SLAYER!')
            time.sleep(2)
            print('Congratulations you won...!')
            time.sleep(2)
            print('But at what cost...')
            time.sleep(3)
            print('Game over!')
            exit()
        else:
            wrong_input()
else:
    wrong_input()