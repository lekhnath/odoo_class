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
    'security/ir.model.access.csv',
    'security/todo_task_owner_assignee_rule.xml',
  ],
  'application': True,
  'installable': True,
}
