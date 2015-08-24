from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from bson import ObjectId

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.copo_mongo
collection = db.person

def view_person(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        doc = {
            "firstname": firstname,
            "lastname": lastname
        }
        collection.insert(doc)
        people = collection.find({})
        return render(request, 'view_person.html', {'people':people})
    else:
        people = collection.find({})
        return render(request, 'view_person.html', {'people':people})


def quicksearch(request):
    import requests
    import json
    import jsonpickle
    firstname = request.GET['firstname']
    url = 'http://localhost:9200/mongoindex/person/_search'
    q = json.dumps({"query":{"match_phrase_prefix":{"firstname":firstname}}})
    data = requests.post(url, q)
    r = data.json()
    return HttpResponse(data.text)