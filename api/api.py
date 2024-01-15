import justpy as jp
import difinition
import json


class Api:
    """Responds to requests at /api?w={word}"""
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = difinition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined

        }

        wp.html = json.dumps(response)
        return wp


