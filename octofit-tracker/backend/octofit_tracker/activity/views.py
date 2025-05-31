from django.http import JsonResponse
from pymongo import MongoClient

def activities_list(request):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    activities = list(db.activity.find({}, {'_id': 0}))
    return JsonResponse({'results': activities})
