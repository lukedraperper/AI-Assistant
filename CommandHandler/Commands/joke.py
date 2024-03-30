def Joke():
    global CS
    url = requests.get("https://v2.jokeapi.dev/joke/any").json()
    response = ""
    if url["type"] == "twopart":
        response = url["setup"]
        time.sleep(1)
        response = url["delivery"]
    else:
        response = url["joke"]
    
    return response