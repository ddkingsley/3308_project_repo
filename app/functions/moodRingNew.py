import random


colors = ["Black", "Yellow", "Orange", "Light green", "Green", "Blue", "Dark Blue", "Violet", "Pink"]


def moodRing():
  color = random.choice(colors)
  print(color)

  if color == "black":
    print("You feel angery, fearful, or apathetic.")
  
  if color == "yellow":
    print("Your emotions are mixed or conflicted. You may feel distracted or slightly anxious.")

  if color == "orange":
    print("You are upset. You feel nervous, stress, or confused about something.")

  if color == "light green":
    print("You are anxious about something or someone. You are guarded and alert. You may also feel mild jealousy or stress.")
  
  if color == "green":
    print("This is the default color. Your emotions are stable today: you do not feel excessive negativity or positivity.")

  if color == "blue":
    print("You are cheerful and optimistic today!")
  
  if color == "dark blue":
    print("You are content.")

  if color == "violet":
    print("You have romance on your mind. You may feel moody, mischievous or sensual. You are prone to unpredictable choices today.")

  if color == "pink":
    print("You are overcome with strong emotions. You are infatuated with someone or something.")



def callMoodRing():
  moodRing()

  again = True

  while again == True:
    reply = input("Would you like to try again? (yes/no)")

    if reply == "yes":
      callMoodRing
    else:
      break 


play = input("Would you like to known your emotional energy? (yes/no)")
if play == "yes":
  callMoodRing()

