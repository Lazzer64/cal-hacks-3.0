import json
from watson_developer_cloud import *

def personality(texts, auth):
    person = PersonalityInsightsV3(username=auth[0], password=auth[1], version='2016-10-20')
    text = ' '.join(texts)
    response = person.profile(text=text)

    personality = response.get('personality')
    for trait in personality:
        print trait.get('name'),':', trait.get('percentile')
        for child in trait.get('children'):
            print '--',child.get('name'),':', child.get('percentile')
