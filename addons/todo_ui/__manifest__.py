{
    'name': 'User Interface for To-Do application',
    'depends': [
        'enhance_todo_app',
        'web',
    ],
    'author': 'Lekhnath Rijal',
    'data': [
        "views/assets.xml",
        "views/view.xml",
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'application': False,
    'installable': True,
}
