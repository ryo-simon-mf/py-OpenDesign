import requests

class LineNotify:
    def __init__(self, token, api):
        self.line_notify_token = 'O18iHn7FkuvIkEDDzfL9CjA70wPklYC6YSpfob9sNfZ'
        self.line_notify_api = 'https://notify-api.line.me/api/notify'

    def send_message(self, message):
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + self.line_notify_token}
        line_notify = requests.post(self.line_notify_api, data=payload, headers=headers)
        return line_notify
