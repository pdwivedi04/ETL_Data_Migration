import pandas as pd # type: ignore
from datetime import datetime

def transform_data(activity_data):
    activity_data['archived_at'] = datetime.now()
    return activity_data
