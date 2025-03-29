{
    "name": "Estados de flujo de ventas (shokale)",
    "version": "17.0.1.0.1",
    "summary": """
        Agrega nuevos estados en `sale` de `sale.order`
     """,
    "category": "sale",
    "author": "Juan D. Collado Vasquez",
    "website": "https://tagre.pe",
    "depends": [
        "sale_management","shokale_templates"
    ],
    "data": [
        'views/sale_order_views.xml',
        'reports/production_template.xml',
        'reports/production_report.xml',
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
