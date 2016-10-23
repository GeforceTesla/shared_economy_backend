import requests
#from requests import Request, Session


class restful_base(object):

    def __init__(self, base_url, user=None, password=None):
        self.session = requests.Session()
        self._base_url = base_url
        self.session.auth = (user, password) if user else None

    def _set_remove_session_args(self, key, **kwargs):
        if kwargs.get(key, None):
            setattr(self.session, key, kwargs[key])
            del kwargs[key]

    def _session_cookies(self, **kwargs):
        cookies = kwargs.get('cookies', None)
        if cookies:
            del kwargs['cookies']
        return cookies

    def _session_cert(self, **kwargs):
        self._set_remove_session_args('cert', **kwargs)

    def _session_header(self, **kwargs):
        for key, value in kwargs.iteritems():
            if key == 'content_type':
                self.session.headers.update({'Content-Type': value})
            else:
                self.session.headers.update({key: value})

    def _process_session_args(self, **kwargs):
        cookies = self._session_cookies(**kwargs)
        self._session_cert(**kwargs)
        self._session_header(**kwargs)
        return cookies

    def get(self, url_args, **kwargs):
        cookies = self._process_session_args(**kwargs)
        url = "%s/%s" % (self._base_url, url_args)
        r = self.session.get(url, cookies=cookies)
        return r.status_code, r.content, r.headers

    def put(self, url_args, data, **kwargs):
        cookies = self._process_session_args(**kwargs)
        url = "%s/%s" % (self._base_url, url_args)
        r = self.session.put(url, data=data)
        return r.status_code, r.content, r.headers

    def post(self, url_args, data=None, json=None, **kwargs):
        cookies = self._process_session_args(**kwargs)
        url = "%s/%s" % (self._base_url, url_args)
        r = self.session.post(url, data=data, json=json)
        return r.status_code, r.content, r.headers

    def delete(self, url_args, **kwargs):
        cookies = self._process_session_args(**kwargs)
        url = "%s/%s" % (self._base_url, url_args)
        r = self.session.delete(url)
        return r.status_code, r.content, r.headers


if __name__ == "__main__":
    user = 'rwang3'
    pwd = 'Wr@nsfz1983'
    base_url = 'https://fishbulb-dev.sg05.orchard.apple.com'
    sess = restful_base(base_url, user, pwd)

    url_args = 'api/v1/shift'
    #r_code, r_content, r_headers = sess.get(url_args, Accept='application/json')
    r_code, r_content, r_headers = sess.get(url_args)
    print(r_code)
    print(r_content)
    print(r_headers)