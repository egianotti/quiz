import json
from .models import Pregunta
import datetime as dt
import os

def formatear_json(request):
    try:
        req=request.POST
        req=dict(req)
        response={'pregunta':req['pregunta'][0],
                  'respuestas':[(req['respuesta'][x-1],req['correcta{}'.format(str(x))]) for x in range(1,len([c for c in req['respuesta'] if c != ''])+1)]}
        p="eso"
        name=str(dt.datetime.now()).replace(":","_").replace(" ","_")
        with open('{}.json'.format(name), 'w') as archivo:
            json.dump(response, archivo)
        pregunta=Pregunta()
        pregunta.pregunta=response["pregunta"]
        pregunta.archivo=name
        pregunta.save()
        os.remove("{}".format(name))

    except Exception as e:
        print(e)