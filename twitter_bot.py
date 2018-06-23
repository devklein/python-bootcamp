# Lesson Trump Twitter Bot
import random

tweet = []

# Some usual Trump Tweet phrases
part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

# capsule all parts in one list
best_words = [part1, part2, part3, part4]

for part in best_words:
    # get a random phrase out of every part and append it to the tweet-list
    r = random.randint(0, len(part)- 1)
    tweet.append(part[r])

# print the tweet and bring your karma down
print(" ".join(tweet) + "!")    