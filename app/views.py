from datetime import datetime
from flask import request

from app import app
import requests


@app.route('/')
def init():
    return getClime()


@app.route('/sunrise', methods=['GET'])
def getClime():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    event_type = request.args.get('eventtype')

    if latitude and longitude and event_type:
        url = 'https://api.sunrise-sunset.org/json?lat=' + latitude + '&lng=' + longitude + '&date=today'
        response = requests.get(url)
        sunrise = response.json()['results']['sunrise']
        sunset = response.json()['results']['sunset']

        format_hour = '%I:%M:%S %p'
        today = datetime.now()
        hour = today.time()
        date_obj = datetime.combine(datetime.today(), hour)

        if event_type == 'sunrise':
            hour = datetime.strptime(sunrise, format_hour).time()
        elif event_type == 'sunset':
            hour = datetime.strptime(sunset, format_hour).time()

        hora_desejada_objeto = datetime.combine(datetime.today(), hour)
        difference_time = hora_desejada_objeto - date_obj

        try:
            hora_objeto = datetime.strptime(str(difference_time), "%H:%M:%S.%f").time()
            data_hora_objeto = datetime.combine(today.date(), hora_objeto)
            data_hora_formatada = data_hora_objeto.strftime("%d/%m/%Y %H:%M:%S")
        except:
            return str(f'The {event_type} its over' )
        return str(f'Remaining time until {event_type}:{data_hora_formatada}')
