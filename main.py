import os

from config import config
from utils import get_youtube_data, create_database, save_data_to_database


def main():

    api_key = os.getenv('YT_API_KEY')
    channels_ids = [
        'UCrWWcscvUWaqdQJLQQGO6BA',  # Selfedu
        'UClJzWfGWuGJL2t-3dYKcHTA'   # PythonToday
    ]
    params = config()

    data = get_youtube_data(api_key, channels_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()

