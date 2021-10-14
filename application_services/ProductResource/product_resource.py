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

    @classmethod
    def create(cls, data):
        new_product = dict()
        new_product['name'] = data['name']
        new_product['price'] = data['price']
        new_product['description'] = data['description']
        new_product['category'] = data['category']
        new_product['quantity'] = data['quantity']
        new_product['image_url'] = data['image_url']
        new_product['availability'] = data['availability']
        res = RDBService.create("catalog", "product", new_product)
        return res

    @classmethod
    def delete(cls, template):
        res = RDBService.delete("catalog", "product", template)
        return res

    @classmethod
    def update(cls, template, row):
        res = RDBService.update("catalog", "product", template, row)
