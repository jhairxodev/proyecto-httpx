import httpx

respuesta = httpx.get("https://api.github.com/users/octocat")

print(respuesta.status_code)
print(respuesta.json()["name"])
