# -*- coding:utf-8 -*-
import os
from dotenv import load_dotenv
from pathlib import Path


class ProductionConfig:
    DEBUG = True
    SERVER_PORT = 5001


class DevelopmentConfig:
    DEBUG = True
    SERVER_PORT = 5002

class TestingConfig:
    DEBUG = True
    TESTING = True
    SERVER_PORT = 5003




