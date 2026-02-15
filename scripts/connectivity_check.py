import os
import requests

from dotenv import load_dotenv
load_dotenv()

def check_openai():
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        print("✅ API key is valid, OpenAI is reachable")
    else:
        print(f"❌ OpenAI connection failed: {resp.status_code}, {resp.text}")

def check_openweather():
    city = "London"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": os.getenv("OPEN_WEATHER_API_KEY"), "units": "metric"}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        print("✅ API key is valid, OpenWeatherMap is reachable")
    else:
        print(f"❌ OpenWeatherMap connection failed: {resp.status_code}, {resp.text}")

def check_polygon():
    symbol = "IBM"
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev"
    params = {"adjusted": "true", "apiKey": os.getenv("POLYGON_API_KEY")}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        print("✅ API key is valid, Polygon is reachable")
    else:
        print(f"❌ Polygon connection failed: {resp.status_code}, {resp.text}")

def check_tavily():
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": "ping",
        "max_results": 1,
    }

    resp = requests.post(url, json=payload)

    if resp.status_code == 200:
        print("✅ API key is valid, Tavily is reachable")
    else:
        print(f"❌ Tavily connection failed: {resp.status_code}, {resp.text}")


def main():
    print("🔍 Checking connectivity...\n")
    check_openai()
    check_openweather()
    check_polygon()
    check_tavily()

if __name__ == "__main__":
    main()