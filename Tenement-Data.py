import  requests
from bs4 import BeautifulSoup

def get_lorder_sex(span_class):
    if span_class = ['member_boy_ico']
       return "男"
    elif span_class = ['member_girl_ico']
        return"女"

def get_links(url):
    wb_data = requests.get(url)

    soup = BeautifulSoup(wb_data.text,"lxml")

    links = soup.select("#page_list > ul > li > a > img")

    for link in links:

        href = link.get("href")

        get_detail_info(href)

def get_detail_info(url):
    wb_data = requests.get(url)

    soup = BeautifulSoup(wb_data.text,"lxml")

    titles = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em")

    addresss = soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span")

    pricess = soup.select("#pricePart > div.day_l > span")

    images = soup.select("#imgMouseCusor")

    avartars = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > a > img")

    names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")

    sexs = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > div")

    for title, address, price, image, avartar, name, sex in zip(titles, addresss, prices, images, avartars, names,
                                                                sexs):
        # 从标签里面提取内容
        data = {
            "title": title.get_text(),
            "address": address.get_text(),
            "price": price.get_text(),
            "image": image.get("src"),
            "avartar": avartar.get("src"),
            "name": name.get_text(),
            "sex": get_lorder_sex(sex.get("class"))
        }
        print(data)