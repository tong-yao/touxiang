import requests, hashlib, datetime, pymysql

timeout = 20
HOST = "39.97.241.144"
PORT = 3306
USER = "lianzhuoxinxi"
PASSWORD = 'LIANzhuoxinxi888?'
DATABASE = "spider"
CHARSET = "utf8mb4"
start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 开始时间


def connect_mysql():
    # 链接mysql
    db = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        charset=CHARSET
    )
    return db


db = connect_mysql()

with open("icon2.txt", "r")as f:
    url_list = f.readlines()
    id = 0
    for url in url_list:
        url = url.strip('\n')
        print(url)
        try:
            response = requests.get(url)
        except Exception as e:
            print(e)
            continue
        data = response.content
        id += 1

        md5 = hashlib.md5()
        md5.update(data)
        name = md5.hexdigest()
        print(name)
        with open("/home/photo{}.jpeg".format(name), "wb") as f:
            f.write(data)
            photopath = "/home/photo{}.jpeg".format(name)

        with db.cursor() as cursor:
            try:
                sql = "UPDATE namephoto SET photopath = '{}' WHERE id = '{}'".format(
                    photopath, id)
                cursor.execute(sql)
            except Exception as e:
                print(sql)
                print("eeeeeee", e)
            db.commit()
