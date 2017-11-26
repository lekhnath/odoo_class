{
  'name': 'To-Do Application',
  'description': """
  To-Do Application for Odoo
  """,
  'version': '10.0.1.0',
  'author': 'Lekhnath Rijal',
  'category': 'Uncategorized',
  'depends': [
    'base',
  ],
  'data': [
    'views/view.xml',
  ],
  'demo': [
    'data/todo_app.task.csv',
  ],
  'application': True,
  'installable': True,
}
