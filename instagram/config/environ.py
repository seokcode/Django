import os
from dotenv import load_dotenv

load_dotenv()


class Environ:

    # 장고 시크릿 키
    SECRET_KEY = os.environ['SECRET_KEY']