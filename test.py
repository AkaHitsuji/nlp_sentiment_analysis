import json

reviews = open('CellPhoneReview.json', 'r').read().strip().split('\n')
reviews = [json.loads(s) for s in reviews]

print(type(reviews))
