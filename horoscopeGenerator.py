"""
Horoscope Generator feature. Input: solar sign and type of fortune desired. Output: personality statement and fortune selected.
"""

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

loveFortune = ["(S)he's just not that into you", 
               "Nothing could ever split you two apart", 
               "(S)he is thinking of you right now", 
               "You make their world go round", 
               "Love is not for the weak", 
               "You look so good together", 
               "Ask yourself: does (s)he spark joy?", 
               "(S)he loves you more than you can imagine", 
               "You two will walk into the sunset",
               "(S)he can't stop thinking about you!", 
               "True love is built", 
               "You make them want to dance", 
               "You know it's meant to be", 
               "Love won't just come knocking at your door", 
               "Everyone searches for a love like this", 
               "Look elsewhere", 
               "Love is a two-way street", 
               "Love someone who feels like home", 
               "Marry that", 
               "They love you at your darkest", 
               "You will meet a short, pale stranger",
               "You will never be a second choice", 
               "Just ask them out", 
               "The stars have aligned. Love is coming your way", 
               "Love is patient, love is kind. Looks like this isn't it", 
               "People are naturally attracted to you",
               "Talk to that one person tomorrow",
               "Wink at that one person tomorrow, and watch what happens",
               "You attract the love you give",
               "You don’t choose who you fall in love with",
               "The butterflies never go away"
              ]

healthFortune = ["Check your cholesterol", 
                 "Check your blood sugar", 
                 "A positive attitude will keep you healthy",
                 "You're healthier than your grandma!", 
                 "You might be a hypocondriac",
                 "'Exercise' isn't just a catchphrase", 
                 "Good things come to those who exercise", 
                 "Low fat, low sodium, organic, raw, vegan, local. It's all just too much, isn't it?", 
                 "Spinach, lentils, liver, shellfish, pumpkin seeds, quinoa, turkey: get your iron on!",
                 "Broccoli, avocados, almonds, beans, chia seeds, bananas, artichokes: get your fiber on!",
                 "Mental health is important",
                 "Your mantra for today is: 'Feeling good today, I am feeling good today'",
                 "Gratitude will keep you healthy",
                 "You are what you eat",
                 "Your mantra for today is: 'I am fulfilled. I am fearless'",
                 "You are strong. You are beautiful. You are enough.",
                 "Highly effective people floss every night",
                 "Don't forget to smile",
                 "In case you were wondering, salmon, mackerel and herring are rich in omega-3 fatty acids",
                 "Always carry your insurance card with you",
                 "You obviously cannot get health advice from a cookie. That's what the horoscope is for.",
                 "You are fit",
                 "Geez, have you lost weight?!",
                 "You have walked 2,500 steps today. Only 7,500 to go!"
                ]

wealthFortune = ["Python programmers are billionaires. Become a Python programmer today!",
                 "You will be promoted this summer", 
                 "You will be dirty rich by this time next year", 
                 "Save more for the future", 
                 "You should absolutely invest in those shoes",
                 "Your lucky Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34",
                 "Work hard and you shall succeed!", 
                 "Those caramel lattes will add up fast",
                 "Find opportunities to learn and grow", 
                 "Invest in that project now",
                 "Your lucky square numbers are: 1, 4, 9, 16, 25, 36, 49"
                 "Your lucky palindromes are: 121, 232, 5665, 9009, 12321"
                 "Trust your gut",
                 "Money doesn't grow on trees",
                 "Here's a coupon code for that bag you don't need: DONTDOIT",
                 "You are the sole beneficiary in the will a recently dead African prince",
                 "The hungrier one becomes, the clearer one's mind works",
                 "Winners are not afraid of losing",
                 "Your leadership skills will take you far",
                 "If you want to be rich, never give up. People tend to give up",
                 "Fake it 'till you make it!'",
                 "Work will squeeze you like an orange if you let it",
                 "Your network is your net worth",
                 "Get a credit card with rewards",
                 "When spending money, make sure you're not doing it because you're HALT (hungry, anxious, lonely or tired)",
                 "Find work you love"
                ]

# this function prints a line with personality traits based on zodiac element (water, air, fire or earth)
def horoscopeTraits(sign):
        
    if sign == "Aries" or "Leo" or "Sagittarius":
        print("You are a", random.choice(adverbs), random.choice(fireTraits), "person, with a love for", random.choice(loveFor))

    elif sign == "Taurus" or "Virgo" or "Capricorn":
        print("You are", random.choice(adverbs), random.choice(earthTraits), "person, with a love for", random.choice(loveFor))

    elif sign == "Gemini" or "Libra" or "Aquarius": 
        print("You are a", random.choice(adverbs), random.choice(airTraits), "person, with a love for", random.choice(loveFor))

    elif sign == "Scorpio" or "Cancer" or "Pisces":
        print("You are a", random.choice(adverbs), random.choice(waterTraits), "person, with a love for", random.choice(loveFor))


# this function gets wealth, health, love fortunes, or personality traits
def horoscopeFortuneGenerator(sign):

    fortune = (input("Love, Health, Wealth, or Describe Me?")).lower()

    if fortune == "health":
        print(random.choice(healthFortune))

    elif fortune == "wealth":
        print(random.choice(wealthFortune))

    elif fortune == "love":
        print(random.choice(loveFortune))
    
    elif fortune == "describe me":
        print(horoscopeTraits(sign))

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
