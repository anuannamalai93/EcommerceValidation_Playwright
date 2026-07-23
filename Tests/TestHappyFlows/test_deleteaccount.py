from API.DeleteApi import DeleteApi
from pageobjects.LoginSignup import LoginSignup


def test_delete_account():
    deleteaccount = DeleteApi()
    deleteaccount.delete_account("anuannamalai95@gmail.com","password123")

