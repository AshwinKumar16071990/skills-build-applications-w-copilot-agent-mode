from django.http import JsonResponse
from pymongo import MongoClient

def users_list(request):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    users = list(db.users.find({}, {'_id': 0}))
    return JsonResponse({'results': users})
