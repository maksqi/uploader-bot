import yadisk
from datetime import datetime

from data.config import YANDEX_KEY

y = yadisk.YaDisk(token=YANDEX_KEY)
# print(y.check_token())
# print(y.get_disk_info())


async def ya_upload(path, name, user_id):
    date = datetime.strftime(datetime.now(), '%d.%m.%Y-%H.%M.%S')

    if not y.exists(user_id):
        y.mkdir(user_id)

    if not y.exists(f'{user_id}/{date}'):
        y.mkdir(f'{user_id}/{date}')

    y.upload(path, f'{user_id}/{date}/{name}', overwrite=True)
    y.publish(f'{user_id}/{date}/{name}')
    public_url = y.get_meta(f'{user_id}/{date}/{name}')['public_url']

    return public_url
