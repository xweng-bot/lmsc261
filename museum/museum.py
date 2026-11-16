import requests

url = "https://api.artic.edu/api/v1/artworks/search"

search = input("What would you like to search? ")
min_year = int(input("What's the minimum year you'd like to search? "))
max_year = int(input("What's the maximum year you'd like to search? "))



headers = {
    "AIC-User-Agent": "museum-crawler (xweng@berklee.edu)",
    "User-Agent": "museum-crawler (xweng@berklee.edu)"
}

params = {
    "q": search,
    "fields": "title,artist_display,date_display,date_start,date_end"
}


response = requests.get(url, params = params, headers = headers)

data = response.json()

def format_and_print(data, min_year, max_year):

    for art in data["data"]:

        title = art.get("title")
        artist = art.get("artist_display")
        year = art.get("date_display")
        date_start = art.get("date_start")
        date_end = art.get("date_end")

        if date_start is not None and date_end is not None:
            if date_start <= max_year and date_end >= min_year:
                print(f"{title} is by {artist} which was displayed on {year}")
     


format_and_print(data, min_year, max_year)