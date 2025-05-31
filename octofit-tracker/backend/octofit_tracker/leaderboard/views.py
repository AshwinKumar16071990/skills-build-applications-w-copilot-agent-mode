from django.http import JsonResponse
from pymongo import MongoClient

def leaderboard_list(request):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
    return JsonResponse({'results': leaderboard})
