from quiz.resources.questions import SimpleQuestionsApi

def initialize_routes(api):
    api.add_resource(SimpleQuestionsApi, '/simple')