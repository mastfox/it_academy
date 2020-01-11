#!/usr/bin/python3.7

# -*- coding: utf-8 -*-


class Router:

    saved_path = {}

    def add_path(self, method, path, func):
        self.saved_path[func] = [path, method]

    def request(self, method, path):

        for func, values in self.saved_path.items():
            if method in values:
                if path in values:
                    return func()
                else:
                    return f'Error 405, Method {method} not allowed'
            else:
                return f'Error 404, path {path} not found'

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path):
        return self.request(path, 'POST')

    def put(self, path):
        return self.request(path, 'PUT')

    def patch(self, path):
        return self.request(path, 'PATCH')

    def delete(self, path):
        return self.request(path, 'DELETE')

    def options(self, path):
        return self.request(path, 'OPTIONS')


def my_info():
    return 200, {'me': 'Joanne'}


def update_me():
    return 200, 'OK'


if __name__ == '__main__':
    router = Router()

    router.add_path('/me', 'GET', my_info)
    router.add_path('/me', 'UPDATE', update_me)

    print(router.request('GET', '/me'))
    print(router.get('/me'))

    print(router.post('/me'))
    print(router.get('/us'))