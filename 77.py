#Create a script that gets user's age and returns year of birth
from datetime import datetime

year_birth = datetime.now().year - int(input("What's your age? "))
print("You were born back in %s" % year_birth)
