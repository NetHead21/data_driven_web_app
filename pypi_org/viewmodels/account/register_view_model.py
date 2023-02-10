from pypi_org.viewmodels.shared.view_model_base import ViewModelBase
from pypi_org.services import user_service
from flask import flash


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()
        self.repassword = self.request_dict.repassword.strip()

    def validate(self):
        if not self.name or not self.email or not self.password or not self.repassword:
            self.error = ("Some require field are missing.", "danger")
        elif self.password != self.repassword:
            self.error = ("Passwords do not match. Please try again.", "danger")
        elif user_service.find_user_by_email(self.email):
            self.error = ("Email already exists", "danger")

