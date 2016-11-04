# coding=utf-8

__import__('framework').init()

import unittest

from mimas.fs.s3 import S3

ACCESS_KEY = ""
ACCESS_SECRET = ""
PREFIX_URL = ""
BUCKET_NAME = "saturn"
ACL = "public-read"
FILE_NAME = "saturn/test.text"


class S3Test(unittest.TestCase):
    def test_bucket(self):
        s3 = S3(ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME, PREFIX_URL)
        assert S3
        assert s3.bucket_name == BUCKET_NAME
        assert s3.bucket

        r = s3.bucket_acl(ACL)
        assert r

    def test_upload(self):
        s3 = S3(ACCESS_KEY, ACCESS_SECRET, BUCKET_NAME, PREFIX_URL)
        assert S3

        r = s3.upload_file("hello word!", FILE_NAME)
        assert r

        r = s3.is_file_exists(FILE_NAME)
        assert r

        url = s3.get_url(FILE_NAME)
        assert url == PREFIX_URL + "/" + BUCKET_NAME + "/" + FILE_NAME

        r = s3.delete_file(FILE_NAME)
        assert r

        r = s3.is_file_exists(FILE_NAME)
        assert not r
