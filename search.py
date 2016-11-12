def lookThroughWords(data, text):
    for word in text.split():
        if data.get(word, 0) == 0:
            data[word] = 1
        else:
            data[word] += 1

def getTopFive(data, forbidden):
    topFive = []
    for word, count in data.items():
        if word in forbidden:
            next
        word = word.replace(",", "")
        word = word.replace(".", "")
        topFive.append((word, count))
        topFive = sorted(topFive, key = lambda x: x[1], reverse = True)
        if len(topFive) > 5:
            topFive.pop()
    return topFive


def search(textList):
    data = {}
    for text in textList:
        lookThroughWords(data, text)
    best = getTopFive(data)
    return best
