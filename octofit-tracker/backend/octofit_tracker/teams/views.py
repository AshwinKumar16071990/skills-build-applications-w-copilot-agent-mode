from django.http import JsonResponse
from pymongo import MongoClient

def teams_list(request):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    teams = list(db.teams.find({}, {'_id': 0}))
    return JsonResponse({'results': teams}, status=200)
