from flask import Response, request
from flask_restful import Resource
from quiz.database.models import SimpleQuestions

class SimpleQuestionsApi(Resource):
    def get(self):
        questions = SimpleQuestions.objects().to_json()
        return Response(questions, mimetype="application/json", status=200)
    def post(self):
        body = request.get_json()
        question = SimpleQuestions(**body).save()
        id = question.id
        return {'id':str(id)},200
