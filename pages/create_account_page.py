class CreateAccountPage():
    def __init__(self, driver):
        self.driver = driver

    # variables
    def determine_variables(self):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        user_dictionary = {'fn': 'Alex', 'ln': 'Kardash', 'password': 'Abc123456!'}

        first_name_field.send_keys(user_dictionary['fn'])
        last_name_field.send_keys(user_dictionary['ln'])
        password_field.send_keys(user_dictionary['password'])
        confirm_password_field.send_keys(user_dictionary['password'])

    def validate_username_field(self, driver, email):
        import time
        validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
        username_field = driver.find_element_by_id("username")
        next_button = driver.find_element_by_id("accountDetailsNext")
        username_field.clear()
        username_field.send_keys(email)
        next_button.click()
        time.sleep(1)
        assert validation_error in driver.page_source