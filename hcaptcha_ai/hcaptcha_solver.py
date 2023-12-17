# -*- coding: utf-8 -*-
# Time       : 2022/9/23 17:28
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import time
import typing


from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import hcaptcha_challenger as solver
from hcaptcha_challenger import HolyChallenger
from hcaptcha_challenger.exceptions import ChallengePassed

# Existing user data


# Init local-side of the ModelHub
solver.install()


def hit_challenge(ctx, challenger: HolyChallenger, retries: int = 10) -> typing.Optional[str]:
    """
    Use `anti_checkbox()` `anti_hcaptcha()` to be flexible to challenges
    :param ctx:
    :param challenger:
    :param retries:
    :return:
    """
    if challenger.utils.face_the_checkbox(ctx):
        challenger.anti_checkbox(ctx)
        if res := challenger.utils.get_hcaptcha_response(ctx):
            return res

    for _ in range(retries):
        try:
            if (resp := challenger.anti_hcaptcha(ctx)) is None:
                continue
            if resp == challenger.CHALLENGE_SUCCESS:
                return challenger.utils.get_hcaptcha_response(ctx)
        except ChallengePassed:
            return challenger.utils.get_hcaptcha_response(ctx)
        challenger.utils.refresh(ctx)
        time.sleep(1)




def hcaptchaAI(driver):
    challenger = solver.new_challenger(screenshot=True, debug=True)
    hit_challenge(ctx=driver, challenger=challenger)
    

