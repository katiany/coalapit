from src.api.config import settings
from src.api.service.request import get


def fetch_data(member_id: int):
    response = []

    api_list = [
        settings.API_1_URL,
        settings.API_2_URL,
        settings.API_3_URL,
    ]
    
    for api_url in api_list:
        url = f"{api_url}?member_id={member_id}"
        response.append(get(url))

    return response
    