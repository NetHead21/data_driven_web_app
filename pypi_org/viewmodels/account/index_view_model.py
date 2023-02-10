from pypi_org.viewmodels.shared.view_model_base import ViewModelBase
from pypi_org.services import user_service


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)