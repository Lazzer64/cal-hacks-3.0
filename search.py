def lookThroughWords(data, text):
    for word in text.split():
        if data.get(word, 0) == 0:
            data[word] = 1
        else:
            data[word] += 1

def getTopFive(data):
    topFive = []
    for word, count in data.items():
        word = word.replace(",", "")
        word = word.replace(".", "")
        topFive.append((word, count))
        topFive = sorted(topFive, key = lambda x: x[1], reverse = True)
        if len(topFive) > 5:
            topFive.pop()
    return topFive



text = "hi bob why are you at cal hacks. bob you should go to sleep. bob do it now"
data = {}
lookThroughWords(data, text)
best = getTopFive(data)
for item in best:
    print(item[0] + " has count:" + str(item[1]))
