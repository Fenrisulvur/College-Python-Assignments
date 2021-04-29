"""
This is a program that will display information about myself.
Additionally it can calculate your age in 2025.
And also tell knock knock jokes!
"""
import random
from random import shuffle
from datetime import datetime

"""
/-----------------/
About me code section:
/-----------------/
"""
#print my age
def my_age():
  today = datetime.today()
  age = today.year-1995
  print("I am "+str( age if today.month >= 8 else age-1  ) +" years old as of the time this program was ran, and currently live in Howard, PA")
  #Output house ascii art
  print('''\
      ) )        /\\
    =====      /  \\
    _|___|_____/ __ \____________
  |::::::::::/ |  | \:::::::::::|
  |:::::::::/  ====  \::::::::::|
  |::::::::/__________\:::::::::|
  |_________|  ____  |__________|
    | ______ | / || \ | _______ |
    ||  |   || ====== ||   |   ||
    ||--+---|| |    | ||---+---||
    ||__|___|| |   o| ||___|___||
    |========| |____| |=========|
  (^^-^^^^^-|________|-^^^--^^^)
  (,, , ,, ,/________\,,,, ,, ,)
  ','',,,,' /__________\,,,',',;;
  ''')
#print my fav animals
def fav_animals():
  print("My favorite animals are cats and foxes")
  #Output cat ascii art
  print('''\
  _._     _,-'""`-._
  (,-.`._,'(       |\`-/|
      `-.-' \ )-`( , o o)
            `-    \`_`"'-
  ''')
  #Output fox ascii art
  print('''\
    _,-=._              /|_/|
    `-.}   `=._,.-=-._.,  @ @._,
      `._ _,-.   )      _,.-'
          `    G.m-"^m`m' 
  ''')
#print my high school
def my_school():
  print("I graduated from Bald Eagle Area High School in 2013")
  #Output classroom ascii art
  print('''\
                                .------------------------.
                                |    Well, Corey, do       |
      __________________________|   you know the answer?   |
    |  _________________________'-------------,----------'
    | |                         ____         /  | |
    | |  2x+3x/y2x = 4xy-6y    (___ \           | |
    | |                       ( (..) )          | |
    | |                  \\\\\\' |( < ,) )         | |
    | |                   `|_\_\)--(  )         | |
    | |                    \  ,"""(___)         | |
    | |                     `'\_  __  \         | |
    | |                        |    ,  )        | |
    | |_______________________ /  _/  /_________| |
    |________________________ I ///\./I___________|     gnv
                              |       |
                              |       |
                              '-.._..-'   .---------------------------.
                                | |  )   (  Mmm... Beans               )
                                _| | /     '--------,------------------'
                              .'_.�_/7            _/
                                          .((()           Z  z
                _..._                     /_ (())        z
              /     \                   <   ?)))     Z
              |     |                    \_.((((
              \  __ /                    __()))))
                \(__)                    /        \\
              __//  \                   /   ,..--'^|
            /`  (____)-.               /  ( |      |
          /            \                 / |..--/^
  ''')
#print my hobbies
def my_hobbies():
  print("My hobbies are gaming, hunting, 3d modeling, and programming")
  #Output space invader ascii art
  print('''\
                    __
                  _|  |_
                _|      |_
                |  _    _  |
                | |_|  |_| |
            _  |  _    _  |  _
            |_|_|_| |__| |_|_|_|
              |_|_        _|_|
                |_|      |_| 
  ''')

#Display choices to user to learn about me
def about_me():
  while True:
    print("\n\nWhat would you like to learn about me?: \n1: My hobbies. \n2: My favorite animals \n3: My school \n4: My age \n5: Go Back")
    choice = get_user_input_num("Enter your choice ->", 1, 5)
    if choice == 1:
      my_hobbies()
    elif choice == 2:
      fav_animals()
    elif choice == 3:
      my_school()
    elif choice == 4:
      my_age()
    else:
      return
    input("-> Press enter to continue...")


"""
/-----------------/
user age code section:
/-----------------/
"""
#calculate user age based off of current age and current year
def get_user_age():
  print("\n\nWhat is your current age?")
  age = get_user_input_num("Enter your age -> ", 1, 140)
  today = datetime.today()
  
  if today.year > 2025:
    age -= today.year-2025
  elif today.year < 2025:
    age += 2025 - today.year
  
  print("You shall be %i in 2025"%age)
  input("-> Press enter to continue...")



"""
/-----------------/
Joke code section:
/-----------------/
"""
joke_list = [
            ["Canoe", "Canoe come out and play with me today?"],
            ["Lettuce", "Lettuce in, it's cold out here."],
            ["Boo", "Don't cry, it's just me."],
            ["Atch", "Bless you!"],
            ["Figs", "Figs the doorbell, it's broken!"],
            ["Olive", "Olive you."],
            ["Who", "Are you an owl?"],
]
#pick a joke and tell it
def joke_picker():
	rand_joke = random.choice(joke_list)
	currentJoke = Knock_Knock_Joke(rand_joke[0], rand_joke[1])
	currentJoke.tell()
  
#joke helper class to keep things organized
class Knock_Knock_Joke(object):

  proper_responses = {
    "who's there?", "whos there?",
    "who's there?", "to whom am I speaking?", 
    "whos there", "wt","who are you","who are you?"
    }

  def __init__(self, visitor, punchline):
    self.visitor = visitor
    self. punchline = punchline

  def tell(self):
    print("Knock Knock")
    response = input("-> ")

    while not (response in self.proper_responses):
      print("Come on, you know what I want you to say!")
      response = input("-> ").lower()

    print("{}.".format(self.visitor))
    response = input("-> ").lower()
    expected_responses = ["%s who?" % self.visitor.lower(), "%s who" % self.visitor.lower()]

    while not (response in expected_responses):
      print( "Hmmpf... You're supposed to say \"%s who?\"! Try again." % self.visitor)
      response = input("-> ").lower()

    print("{}".format(self.punchline))
    input("-> Press enter to continue...")
    if get_yes_no("Want to hear another joke?", default='no'):
      joke_picker()


"""
/-----------------/
driver code section:
/-----------------/
"""
#grab user number input within set bounds
def get_user_input_num(text, min,max):
    while True:
        user_inp = ""
        try:
            user_inp = input(text)
            amnt = int(user_inp)
            if len(str(amnt)) == 0 or amnt > max or amnt < min:
                print("Must be a number & between %i-%i" % (min, max))
            else:
                return amnt
        except ValueError:
            if user_inp == "forcequit":
                raise SystemExit(0)
            print("Must be a whole number")

def to_bool(value):
    """
        Converts 'something' to boolean. Raises exception for invalid formats
            Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
            Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true",  "t", "1"):
        return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"):
        return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))

#grab yes/no input
def get_yes_no(question, default='no'):
    if default is None:
        prompt = " [y/n] "
    elif default == 'yes':
        prompt = " [Y/n] "
    elif default == 'no':
        prompt = " [y/N] "
    else:
        raise ValueError("Unknown setting '{default}' for default.")

    while True:
        try:
            resp = input(question + prompt).strip().lower()
            if default is not None and resp == '':
                return default == 'yes'
            else:
                return to_bool(resp)
        except ValueError:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

#main switchboard loop
def main():
  print("_-"*20+"_")
  print("Hello! My name is Corey")
  while True:
    print("\n\nWhat would you like to do?: \n1: Learn more about me.\n2: Get your age\n3: Knock knock joke\n4: Quit")
    choice = get_user_input_num("Enter your choice -> ",1,4)
    if choice == 1:
      about_me()
    elif choice == 2:
      get_user_age()
    elif choice == 3:
      joke_picker()
    else:
      return


main()


print("Thank you for running my about me script!")

