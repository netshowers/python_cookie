import requests
from bs4 import BeautifulSoup


def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None


def extract_next_page_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    next_page_link = soup.find("a", class_="next pager_next")
    if next_page_link:
        next_page_url = next_page_link["href"]
        return next_page_url
    else:
        return None


def extract_previous_page_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    previous_page_link = soup.find("a", class_="pre pager_prev")
    if previous_page_link:
        previous_page_url = previous_page_link["href"]
        return previous_page_url
    else:
        return None


def extract_page_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    page_content = soup.find("div", id="htmlContent").get_text()
    return page_content


def main():
    # 初始页面的URL
    url = "https://www.69shu.org/book/112299/40773464.html"

    # 读取初始页面的内容
    current_page_content = fetch_page_content(url)
    if current_page_content:
        print(extract_page_content(current_page_content))

        while True:
            command = input("请输入指令（下一页/上一页/退出）: ")

            if command == "下一页":
                next_page_url = extract_next_page_url(current_page_content)

                if next_page_url:
                    next_page_content = fetch_page_content(next_page_url)

                    if next_page_content:
                        current_page_content = next_page_content
                        print(extract_page_content(current_page_content))
                    else:
                        print("无法访问下一页")
                else:
                    print("已到达最后一页")
            elif command == "上一页":
                previous_page_url = extract_previous_page_url(current_page_content)

                if previous_page_url:
                    previous_page_content = fetch_page_content(previous_page_url)

                    if previous_page_content:
                        current_page_content = previous_page_content
                        print(extract_page_content(current_page_content))
                    else:
                        print("无法访问上一页")
                else:
                    print("已到达第一页")
            elif command == "退出":
                break
            else:
                print("无效指令，请重新输入")
    else:
        print("无法访问初始页面")


if __name__ == '__main__':
    main()
