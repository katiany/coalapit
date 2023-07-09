from typing import List
from src.api.model.response import Response


def coalesce(data: List[Response]):
    average = Response(deductible=0, stop_loss=0, oop_max=0)
    for response in data:
        average.deductible = average.deductible + response['deductible']
        average.stop_loss = average.stop_loss + response['stop_loss']
        average.oop_max = average.oop_max + response['oop_max']
    
    average.deductible = int(average.deductible/len(data))
    average.stop_loss = int(average.stop_loss/len(data))
    average.oop_max = int(average.oop_max/len(data))

    return average