''' Here I continue to try a unittest

'''

import unittest
from unittest.mock import patch
# from collections import deque

from Regex_and_Parsing_HTML import MyHTMLParser


class TestMyHTMLParser(unittest.TestCase):
    # @classmethod
    # @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    def setUpClass(cls):
        cls.parser = MyHTMLParser()
        with open('test_data_for_HTML_2.txt', 'r', encoding='utf-8') as f:
            inp_str = f.read()
        print(inp_str)


    def test_feed(self):
        with open('test_data_for_HTML_2.txt', 'r', encoding='utf-8') as f:
            inp_str = f.read()
        print(inp_str)


# @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    # def test_client_put(self):
    #     test_data_for_html = [
    #         ("test", 0.5, 1),
    #         ("test", 2.0, 2),
    #         ("test", 0.4, 2),
    #         ("load", 301, 3),
    #     ]
    #     for metric, value, timestamp in test_data_for_html:
    #         try:
    #             self.parser.put(metric, value, timestamp)
    #         except ServerSocketException as exp:
    #             message = exp.args[0]
    #             self.fail(f"Ошибка вызова parser.put("
    #                       f"'{metric}', {value}, timestamp={timestamp})\n{message}")
    #
    # @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    # def test_client_get_key(self):
    #     try:
    #         rsp = self.parser.get("test")
    #     except ServerSocketException as exp:
    #         message = exp.args[0]
    #         self.fail(f"Ошибка вызова parser.get('test')\n{message}")
    #
    #     metrics_fixture = {
    #         "test": [(1, .5), (2, .4)],
    #     }
    #     self.assertEqual(rsp, metrics_fixture)
    #
    # @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    # def test_client_get_all(self):
    #     try:
    #         rsp = self.parser.get("*")
    #     except ServerSocketException as exp:
    #         message = exp.args[0]
    #         self.fail(f"Ошибка вызова parser.get('*')\n{message}")
    #
    #     metrics_fixture = {
    #         "test": [(1, .5), (2, .4)],
    #         "load": [(3, 301.0)]
    #     }
    #     self.assertEqual(rsp, metrics_fixture)
    #
    # @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    # def test_client_get_not_exists(self):
    #     try:
    #         rsp = self.parser.get("key_not_exists")
    #     except ServerSocketException as exp:
    #         message = exp.args[0]
    #         self.fail(f"Ошибка вызова parser.get('key_not_exists')\n{message}")
    #
    #     self.assertEqual({}, rsp, "check rsp eq {}")
    #
    # @patch("socket.create_connection", ServerSocket.create_connection)
    # @patch("socket.socket", ServerSocket.create_connection)
    # def test_client_get_client_error(self):
    #     try:
    #         self.assertRaises(ClientError,
    #                           self.parser.get, "get_client_error")
    #     except ServerSocketException as exp:
    #         message = exp.args[0]
    #         self.fail(f"Некорректно обработано сообщение сервера об ошибке: {message}")
