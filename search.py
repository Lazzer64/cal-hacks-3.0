def lookThroughWords(data, text):
    for word in text.split():
        word = word.lower()
        if data.get(word, 0) == 0:
            data[word] = 1
        else:
            data[word] += 1

def getTopFive(data, forbidden):
    topFive = []
    for i in range(len(forbidden)):
        forbidden[i] = forbidden[i].lower()
    for word, count in data.items():
        if word in forbidden:
            continue
        word = word.replace(",", "")
        word = word.replace(".", "")
        topFive.append((word, count))
        topFive = sorted(topFive, key = lambda x: x[1], reverse = True)
        if len(topFive) > 5:
            topFive.pop()
    return topFive


def search(textList, forbidden):
    data = {}
    for text in textList:
        lookThroughWords(data, text)
    best = getTopFive(data, forbidden)
    return best

"""
text = "hello bob bob bob the the the the a a a a hi hello hi jo j ke"
forbidden = ["a", "the"]
lst = search([text], forbidden)
for i in lst:
    print(i[0] + ": " + str(i[1]))
"""
