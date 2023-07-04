words = ["adopt", "bake", "beam", "cook", "time", "grill", "waved", "hire"]
past_tense = []
for x in words:
    if x.endswith('ed'):
        past_tense.append(x)
    elif x.endswith('e'):
        past_tense.append (x+'d')
    else:
        past_tense.append (x+'ed')
print (past_tense)