from django.http import JsonResponse
from pymongo import MongoClient

def workouts_list(request):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    workouts = list(db.workouts.find({}, {'_id': 0}))
    return JsonResponse({'results': workouts})
