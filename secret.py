from flask import Flask, request, jsonify
from flask_cors import CORS 
from infisical_sdk import InfisicalSDKClient
import requests


app = Flask(__name__)
CORS(app)

CLIENT_ID = "c63c2388-cab9-4f2e-823e-7c1925cf7ad3"
CLIENT_SECRET = "53edcc05b24051248f1f4af5335d30306f435e4dea8d4ba11cafca38f87d9d4b"
NEW_SECRET_CLIENT = "bf7c278dddb6e8a4e994552485e4e004c683dbabfc605472675d38192e3eeafb"
PROJECT_ID = "36bd0fe4-5406-4814-8287-d5adc1b9b182"
SECRET_NAME = "ACCESS_TOKEN_SECRET"
SECRET_TOKEN = "st.bf6a94f0-074e-423a-8711-55545c420378.0ca38f4045d9ec0918d4b6ce31091599.3e9f52a2aab1c93d299d24fac61d45f5"


client = InfisicalSDKClient(host="https://app.infisical.com")

client.auth.universal_auth.login(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

secret = client.secrets.get_secret_by_name(

     secret_name=SECRET_NAME,

     project_id=PROJECT_ID,

     environment_slug="dev",

     secret_path="/",

     expand_secret_references=True,

     include_imports=True,

     version=None

)

try:

    client.auth.universal_auth.login(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    print("Autenticación exitosa")

    secret = client.secrets.get_secret_by_name(

        secret_name=SECRET_NAME,

        project_id=PROJECT_ID,

        environment_slug="dev",

        secret_path="/",

        expand_secret_references=True,

        include_imports=True,

        version=None

    )

    print(f"Secreto obtenido: {secret}")

except Exception as e:

    print(f"Error inesperado: {e}")





@app.route("/token", methods=["GET"])

def token():

    try:

        url = "https://us.infisical.com/api/v3/secrets/raw/ACCESS_TOKEN_SECRET"

        headers = {"Authorization": "Bearer st.bf6a94f0-074e-423a-8711-55545c420378.0ca38f4045d9ec0918d4b6ce31091599.3e9f52a2aab1c93d299d24fac61d45f5"}

        response = requests.request("GET", url, headers=headers)

        

        if response.status_code == 200:

            return jsonify(response.json()), 200

        else:

            return jsonify({"error": response.text}), response.status_code

    except Exception as e:

        return jsonify({"error": str(e)}), 500
    

if __name__=="__main__":
        app.run(debug=True)

