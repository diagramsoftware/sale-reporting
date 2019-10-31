import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-sale-reporting",
    description="Meta package for oca-sale-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-sale_comment_template',
        'odoo11-addon-sale_layout_category_hide_detail',
        'odoo11-addon-sale_order_report_product_image',
        'odoo11-addon-sale_report_delivered_subtotal',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
