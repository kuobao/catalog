from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class ProductResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_data_resource_info(cls):
        return "catalog", "product"

    @classmethod
    def get_product(cls, pid):
        res = ProductResource.get_by_template({"id": pid})
        return res

