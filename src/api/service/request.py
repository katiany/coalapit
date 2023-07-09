import httpx


def get(url):
    try:
        response = httpx.get(url)
        if response.status_code == httpx.codes.OK:
            return response.json()
    except httpx.HTTPStatusError as error:
        print(error.response.status_code)
    except httpx.TimeoutException as error:
        print(error)