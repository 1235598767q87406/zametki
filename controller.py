from model import Model
from view import View
from loguru import logger


class Controller:
    def __init__(self):
        self.task = 0
        self.model = Model()
        self.view = View()

    def logic(self):
        self.task = self.view.user_menu()
        logger.info(f"пользователь дал выражение {self.task}")
