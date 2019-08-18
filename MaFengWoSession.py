# -*- coding: utf-8 -*-

import requests



# session代表某一次连接
mafengwoSession = requests.session()

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "https://passport.mafengwo.cn/",
    "User-Agent": userAgent,
}


# 马蜂窝模仿 登录
def getCookies(account, password):
    print("开始模拟登录马蜂窝")
    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport": account,
        "password": password,
    }
    # 使用session直接post请求
    responseRes = mafengwoSession.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    return responseRes.cookies


# 通过访问个人中心页面的返回状态码来判断是否为登录状态
def redirectToPage(cookie):
    routeUrl = "http://www.mafengwo.cn/plan/route.php"
    # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
    requests.session().cookies=cookie
    responseRes = mafengwoSession.get(routeUrl, headers = header, allow_redirects = False)
    print(f"redirectToPage = {responseRes.status_code}")
    if responseRes.status_code != 200:
        return False
    else:
        return responseRes.text


if __name__ == "__main__":
    cookie=getCookies("13656813728", "taotao@jun1")
    redirectToPage(cookie)
# -*- coding: utf-8 -*-

import requests



# session代表某一次连接
mafengwoSession = requests.session()

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "https://passport.mafengwo.cn/",
    "User-Agent": userAgent,
}


# 马蜂窝模仿 登录
def getCookies(account, password):
    print("开始模拟登录马蜂窝")
    postUrl = "https://passport.mafengwo.cn/login/"
    postData = {
        "passport": account,
        "password": password,
    }
    # 使用session直接post请求
    responseRes = mafengwoSession.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    return responseRes.cookies


# 通过访问个人中心页面的返回状态码来判断是否为登录状态
def redirectToPage(cookie):
    routeUrl = "http://www.mafengwo.cn/plan/route.php"
    # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
    requests.session().cookies=cookie
    responseRes = mafengwoSession.get(routeUrl, headers = header, allow_redirects = False)
    print(f"redirectToPage = {responseRes.status_code}")
    if responseRes.status_code != 200:
        return False
    else:
        return responseRes.text


if __name__ == "__main__":
    cookie=getCookies("13656813728", "taotao@jun1")
    redirectToPage(cookie)
