import requests

def send_request(url, data):
    try:
        response = requests.post(url, files=data)
        print("[Debugger] " + str(response.json()))
        return {
            'status': 'ok',
            'status_code': response.status_code,
            'data': response.json()
        }
    except requests.exceptions.ConnectionError as e:
        return {
            'status': 'error',
            'error': e
        }
    except Exception as e:
        return {
            'status': 'unknow',
            'error': e
        }

def core_login(account, password):
    url = "http://127.0.0.1:21000/api/login"
    data = {
        'username': (None, account),
        'password': (None, password)
    }
    return send_request(url, data)

def core_login_4399(account, password):
    url = "http://127.0.0.1:21000/api/login/4399"
    data = {
        'username': (None, account),
        'password': (None, password)
    }
    return send_request(url, data)

def core_login_4399_with_captcha(account, password, captcha, sessionid):
    url = "http://127.0.0.1:21000/api/login/4399"
    data = {
        'username': (None, account),
        'password': (None, password),
        'captcha': (None, captcha),
        'sessionid': (None, sessionid)
    }
    return send_request(url, data)

def core_login_sauth(cookie):
    url = "http://127.0.0.1:21000/api/login/sauth"
    data = {
        'sauth': (None, str(cookie))
    }
    return send_request(url, data)

def core_get_server_list(user_id):
    url = "http://127.0.0.1:21000/api/get_server_list"
    data = {
        'user_id': (None, user_id)
    }
    return send_request(url, data)

def core_get_server_info(user_id, server_id):
    url = "http://127.0.0.1:21000/api/get_server_info"
    data = {
        'user_id': (None, user_id),
        'server_id': (None, server_id)
    }
    return send_request(url, data)

def core_get_player_list(user_id, server_id):
    url = "http://127.0.0.1:21000/api/get_player_list"
    data = {
        'user_id': (None, user_id),
        'server_id': (None, server_id)
    }
    return send_request(url, data)

def core_add_player(user_id, server_id, player_name):
    url = "http://127.0.0.1:21000/api/add_player"
    data = {
        'user_id': (None, user_id),
        'server_id': (None, server_id),
        'player_name': (None, player_name)
    }
    return send_request(url, data)

def core_start_proxy(user_id, server_id, player_name, port, sock5_ip=None, sock5_auth=None):
    url = "http://127.0.0.1:21000/api/run_local"
    data = {
        'user_id': (None, user_id),
        'server_id': (None, server_id),
        'player_name': (None, player_name),
        'port': (None, port),
        'sock5_ip': (None, sock5_ip),
        'sock5_auth': (None, sock5_auth)
    }
    return send_request(url, data)

def core_get_resource(user_id, server_id):
    url = "http://127.0.0.1:21000/api/get_resource"
    data = {
        'user_id': (None, user_id),
        'server_id': (None, server_id)
    }
    return send_request(url, data)

def core_login_ferver(username, password):
    url = "http://127.0.0.1:21000/api/login/ferver"
    data = {
        'username': (None, username),
        'password': (None, password)
    }
    return send_request(url, data)


def core_ferver_sms_get(phone):
    url = "http://127.0.0.1:21000/api/login/ferver/sms"
    data = {
        'phone': (None, phone)
    }
    return send_request(url, data)

def core_ferver_sms_verify(phone, code):
    url = "http://127.0.0.1:21000/api/login/ferver/sms/verify"
    data = {
        'phone': (None, phone),
        'code': (None, code)
    }
    return send_request(url, data)


# core_login_4399("", "")
# core_login_4399_with_captcha("", "", "ABCD", "CaptchaReqxxxxxxxxxxxxxx")
# core_login_ferver("???@163.com", "?")
# core_ferver_sms_get("10000000001")
# core_ferver_sms_verify("10000000001", "123456")
# 补充：如果谈验证码了
# {"code": -2, "message": "出现验证码,请提交captcha与sessionid,如已输入验证码可能是输入错误", "sessionid": "CaptchaReqxxxxxxxxxxxxxxxxxxx", "url": "https://ptlogin.4399.com/ptlogin/captcha.do?captchaId=CaptchaReqxxxxxxxxxxxxxxx"}
# 再发一次/api/login/4399
# 加两个参数：captcha（验证码：ABCD） sessionid （会话ID）

# core_login_sauth(input("Cookie:"))
# core_get_server_list("")
# core_get_server_info("", "81")
# core_get_player_list("", "81")
# core_add_player("", "81", "")
# core_start_proxy("", "81", "", 25565)
# core_get_resource
