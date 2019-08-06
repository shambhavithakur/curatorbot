import re

words = ['beach', 'mosque', 'slut', 'alcohol', 'lake', 'melancholic', 'knife', 'butt', 'eroticism', 'man and woman', 'nude', 'gun', 'aphrodite', 'anadyomene', 'erotic', 
'sexy', 'pokemon', 'meat', 'proposition', 'nudist', 'negro', 'tramp', 'crucifix', 'hell', 'bath', 'deviant', 'violence', 'sex', 'venus', 'devil', 'beast', 'salom', 'seduce', 'seducer', 'seduction', 'cupid', 'nymph', 'saturn', 'jupyter', 'jupiter', 'lion', 'attack', 'skeleton', 
'smoke', 'tobacco', 'cigar', 'cigarette', 'magdalena', 'magdalene', 'angel', 'david', 'goliath', 'oedipus', 'knight', 'satan']


def prune_title(title):
    title = title.lower()
    return any(word in title for word in words)

