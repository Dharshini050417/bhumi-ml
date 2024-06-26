import requests

def getJson(dimensions,metrics,dateRanges,dimensionFilters):
    url = "https://bhumi-project-1.onrender.com/analytics/report"
    payload = {
        "dimensions": dimensions,
        "metrics": metrics,
        "dateRanges": dateRanges,
    }
    if (dimensionFilters):
        payload["dimensionFilters"]=dimensionFilters
    response = requests.post(url, json=payload)
    # response =requests.get(url)
    return (response.json())

