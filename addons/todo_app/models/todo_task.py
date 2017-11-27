from odoo import models, fields, api

class TodoTask(models.Model):
  _name = 'todo_app.task'
  _description = """
  This is Task table for todo application
  """
  _rec_name = 'title'

  active = fields.Boolean(
    'Is Active?',
    default=True
  )
  title = fields.Char(
    'Tilte/Name',
    required=True
  )
  is_done = fields.Boolean(
    'Task Done?'
  )
  date_deadline = fields.Date(
    'Deadline'
  )

  @api.model
  def archive_done(self):
    # completed_todos = self.search([('is_done', '=', True)])
    # completed_todos.write({
    #   'active': False
    # })
    for todo_task in self.search([('is_done', '=', True)]):
      todo_task.active = False

    return True

  @api.multi
  def toggle_done(self):
    self.ensure_one() #singletone recordset

    # Self is record set and follows active record set mechanism
    for todo_task in self:
      todo_task.is_done = not todo_task.is_done

    return True
