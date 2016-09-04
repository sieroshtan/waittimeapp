
def fill_new_data(apps, schema_editor):
    class OldProductCategories(models.Model):
        product = models.ForeignKey(Product)
        category = models.ForeignKey(Category)

        class Meta:
            db_table = 'products_product_categories'

    ProductCategories = apps.get_model('products', 'ProductCategories')

    for data in OldProductCategories.objects.all():
        ProductCategories.objects.create(
            product_id=data.product_id,
            category_id=data.category_id,
        )