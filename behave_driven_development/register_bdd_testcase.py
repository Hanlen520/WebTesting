#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_bdd_testcase.py
@Time    :   2019/9/1 18:09
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from behave import *
from behave_driven_development.register_bdd_page import RegisterPage

use_step_matcher('re')


@When('I open the register website')
def step_register(context, url):
    # context.driver.get(url)
    RegisterPage(context).get_url(url)


@Then('I except that the title is "([^"]*)"')
def step_register(context, title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title


@When('I set with useremail "([^"]*)"')
def step_register(context, useremail):
    RegisterPage(context).send_useremail(useremail)


@When('I set with username "([^"]*)"')
def step_register(context, username):
    RegisterPage(context).send_userename(username)


@When('I set with password "([^"]*)"')
def step_register(context, password):
    RegisterPage(context).send_password(password)


@When('I set with code "([^"]*)"')
def step_register(context, code):
    RegisterPage(context).send_code(code)


@When('I click with registerbutton')
def step_register(context):
    RegisterPage(context).click_register_button


@Then('I except that text "([^"]*)"')
def step_register(context, code_text):
    text = context.driver.find_element_by_id("captcha_code-error").text
    assert code_text in text