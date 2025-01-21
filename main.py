import requests

url = "https://us.infisical.com/api/v3/secrets/raw/ACCESS_TOKEN_SECRET"

querystring = {"workspaceId":"36bd0fe4-5406-4814-8287-d5adc1b9b182"}

headers = {"Authorization": "Bearer st.bf6a94f0-074e-423a-8711-55545c420378.0ca38f4045d9ec0918d4b6ce31091599.3e9f52a2aab1c93d299d24fac61d45f5"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


