from flask import Flask, request, Response

from src.email_.operations import send_email as send_email_operation


app = Flask(__name__)


@app.route('/email', methods=['POST'])
def send_email():
    def _validate_params(params_: dict) -> bool:
        required_params = {
            'to': str,
            'to_name': str,
            'from': str,
            'from_name': str,
            'subject': str,
            'body': str
        }
        for param, type_ in required_params.items():
            if not isinstance(params_.get(param), type_):
                return False

        return True

    params = request.json

    if _validate_params(params) is False:
        return Response(
            "Invalid parameters",
            status=400,
        )

    sent, client_used = send_email_operation(
        params['to'],
        params['to_name'],
        params['from'],
        params['from_name'],
        params['subject'],
        params['body'],
    )

    return {
        "sent": sent,
        # Note: Should this be exposed to the client
        "client_used": client_used
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
