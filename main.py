import requests

youtube = requests.get("https://www.youtube.com/")

with open("youtube.html" , "wb") as f:
    f.write(youtube.content)
     

try:
    if youtube.status_code == 200:
        print("YouTube is accessible.")
    else:
        print(f"YouTube returned status code: {youtube.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while trying to access YouTube: {e}")

payload = {
    "search_query": "Python programming tutorials"
}

search = requests.get("https://www.youtube.com/", params=payload)

print(search.text)

search_2 = requests.post("https://www.youtube.com/", json=payload)




if search_2.status_code == 200:
    try:
        data =  search.json()
        with open("search_2.json", "w") as f:
                f.write(data)
    except ValueError as e:
        print(f"the error is {e}")