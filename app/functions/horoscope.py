import random

waterTraits = ["emotional", "intuitive", "creative", "empathetic", "spiritual", "perceptive", "passionate", "imaginative", "loving",
              "authentic", "private", "adaptable", "secure", "curious", "inquisitive", "intellectual", "independent"
              "analytical", "logical", "purposeful", "willful", "stubborn", "resolute", "intelligent", "insightful", "intense",
              "enthusiastic", "astute", "ambitious", "hardworking", "trustworthy", "confident", "resourceful", "romantic",
              "generous"]

fireTraits = ["willful", "stubborn", "passionate", "resolute", "intelligent", "determined", "authentic", "intense",
             "instinctive", "impetuous", "expressive", "enthusiastic", "impulsive", "spontaneous", "audacious", "courageous",
             "intrepid", "fearless", "adventurous", "bold", "wild", "cheerful", "positive", "joyful", "optimistic", "intrepid", 
             "proud", "temperamental", "confident" "ambitious", "inspiring", "hardworking", "trustworthy", "idealistic", "independent", 
              "resourceful", "lively", "romantic", "generous"]

airTraits = ["intellectual", "quick-witted", "communicative", "non-conformist", "authentic", "curious", "inquisitive", "independent",
             "entertaining", "social", "analytical", "logical", "purposeful", "intelligent", "enthusiastic", "spontaneous",
            "volatile", "adventurous", "astute", "easy-going", "trustworthy", "inventive", "witty", "resourceful", "agreeable",
            "charming", "lively", "romantic", "glamorous", "original", "generous", "imaginative", "artsy", "creative"]

earthTraits = ["tenacious", "resolute", "driven", "organized", "dedicated", "composed", "easy-going", "ambitious", "hardworking", 
               "trustworthy", "realistic", "wise", "resourceful", "romantic", "self-possessed", "logical", "rational", "strong-minded", 
               "intelligent", "judicious", "cultured", "grounded", "determined", "practical", "prudent", "sensible", "stable", 
               "astute",  "attentive", "generous", "reliable", "conscientious"]

adverbs = ["a deeply", "a very", "an extremely", "a profoundly", "an extraordinarily", "an exceptionally", "an immensely", 
           "a distinctly", "an authentically", "a genuinely", "a fiercely"]

loveFor = ["art", "discovery", "nature", "having fun", "introspection", "intimacy", "excitement", "intricacy",
          "mystery", "the unknown", "danger", "speed", "novelty", "living dangerously", "life", "a quiet night in",
          "a good book", "deep conversation", "standup comedy", "ice cream", "a wild party", "comfort", "the sound of the rain",
          "impossible riddles", "everything non-vegan", "getting lost in nature", "a quiet walk on the beach", "surprises!",
          "working as little as possible", "learning", "sleeping in", "cracking dad jokes", "dancing off beat"]


# print a personality trait line based on zodiac element (water, fire, earth, air)
def horoscopeTraits(sign):
        
    if sign == "Aries" or "Leo" or "Sagittarius":
        trait = str("You are " + random.choice(adverbs) + random.choice(fireTraits) + " person, with a love for " + random.choice(loveFor))
        return trait

    elif sign == "Taurus" or "Virgo" or "Capricorn":
        trait = str("You are " + random.choice(adverbs) + random.choice(earthTraits), " person, with a love for " + random.choice(loveFor))
        return trait

    elif sign == "Gemini" or "Libra" or "Aquarius": 
        trait = str("You are " + random.choice(adverbs) + random.choice(airTraits), " person, with a love for " + random.choice(loveFor))
        return trait

    elif sign == "Scorpio" or "Cancer" or "Pisces":
        trait = str("You are " + random.choice(adverbs) + random.choice(waterTraits), " person, with a love for " + random.choice(loveFor))
        return trait
        
        
# gets wealth, health, or love fortunes
def horoscopeFortuneGenerator(sign):

    fortune = (input("Love, Health, Wealth, or Describe Me?")).lower()

    if fortune == "health":
        healthFortune = open("healthFortunes.txt").readlines()
        yourFortune = random.choice(healthFortune)
        return str(yourFortune)

    elif fortune == "wealth":
        wealthFortune = open("wealthFortunes.txt").readlines()
        yourFortune = random.choice(wealthFortune)
        return yourFortune

    elif fortune == "love":
        loveFortune = open("loveFortunes.txt").readlines()
        yourFortune = random.choice(loveFortune)
        return yourFortune
    
    elif fortune == "describe me":
        return horoscopeTraits(sign)

# calls the fortune generator and keeps up the dialogue
def driver(sign):
    
    horoscopeFortuneGenerator(sign)
    
    more=True
    
    while (more == True):

        another = (input("Would you like another insight? (yes/no)")).lower()

        if another == "yes":
            horoscopeFortuneGenerator(sign)

        if another == "no":
            more=False
            break
        
# start the conversation: ask for solar sign, give personalized statement, offer fortune types
sign = (input("What's your solar sign?")).lower()    
horoscopeTraits(sign)
driver(sign)

