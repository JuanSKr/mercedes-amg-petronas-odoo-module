{
    'name': 'Gestión Mercedes AMG Petronas F1 Team',
    'summary': """
        Módulo para la gestión de piezas de la fábrica de Mercedes AMG Petronas F1 Team
    """,
    'author': 'Juan Castaño',
    'category': 'Gestión',
    'version': '1.0',
    'depends': [],
    'data': [
        'views/menu_view.xml',
        'views/piezas_view.xml',
        'views/pilotos_view.xml',
        'views/fabrica_view.xml',
        'views/motores_view.xml',
        'views/ingenieros_view.xml',
        'security/pieza_security.xml',
        'security/ir.model.access.csv'
    ],
    'images': ['static/description/icon.png'],
}