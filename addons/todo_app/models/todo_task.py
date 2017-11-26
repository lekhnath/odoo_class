from odoo import models, fields

class TodoTask(models.Model):
  _name = 'todo_app.task'
  _description = """
  This is Task table for todo application
  """
  _rec_name = 'title'

  title = fields.Char(
    'Tilte/Name'
  )
  is_done = fields.Boolean(
    'Task Done?'
  )
  date_deadline = fields.Date(
    'Deadline'
  )
