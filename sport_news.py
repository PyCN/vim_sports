# -*- coding: utf-8 -*-
# author: rw
# E-mail: weiyanjie10@gmail.com
import requests
from snake import *


url = "localhost:8080/url_to_latest_news"
former_contents = ""


@key_map("news")
def get_news():
    # TODO: get latest news and display
    global former_contents
    buf = get_current_buffer()
    former_contents = get_buffer_contents(buf)
    contents = ["here is a news from sportscommunity",
                "from original website",]
    set_buffer_lines(buf, contents)


@key_map("close")
def close_news():
    global former_contents
    buf = get_current_buffer()
    set_buffer_contents(buf, former_contents)


if __name__ == '__main__':
    pass

