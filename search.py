def lookThroughWords(data, text):
    for word in text.split():
        word = word.lower()
        if data.get(word, 0) == 0:
            data[word] = 1
        else:
            data[word] += 1

def getTopX(data, forbidden, num):
    topX = []
    for i in range(len(forbidden)):
        forbidden[i] = forbidden[i].lower()
    for word, count in data.items():
        if word in forbidden:
            continue
        word = word.replace(",", "")
        word = word.replace(".", "")
        topX.append((word, count))
        topX = sorted(topX, key = lambda x: x[1], reverse = True)
        #if len(topX) > num:
        #    topX.pop()
        topX = topX[:num]
    return topX


def search(textList, forbidden, num):
    data = {}
    for text in textList:
        lookThroughWords(data, text)
    best = getTopX(data, forbidden, num)
    return best

"""
text = "hello bob bob bob the the the the a a a a hi hello hi jo j ke"
forbidden = ["a", "the"]
lst = search([text], forbidden)
for i in lst:
    print(i[0] + ": " + str(i[1]))
"""
