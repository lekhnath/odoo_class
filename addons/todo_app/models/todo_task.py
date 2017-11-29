from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

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
    'Deadline',
  )
  # display_name = fields.Char(
  #   computed='_compute_display_name'
  # )

  @api.model
  def callme(self):
    countries = self.env['res.country'].search([], ['name'], limit=5)
    print "Total Users %d" %len(countries)

  # @api.one
  # @api.depends('title', 'is_done')
  # def _compute_display_name(self):
  #   #self.ensure_one()

  #   yes_or_no = None
  #   self.display_name = 'Custom'

    # for todo_task in self:
    #   todo_task.display_name = 'Dispaly'

      # if todo_task.is_done:
      #   yes_or_no = '(Yes)'
      # else:
      #   yes_or_no = '(No)'

      # todo_task.display_name = todo_task.title +' '+ yes_or_no
    #self.ensure_one()
    #yes_or_no = '(Yes)' if self.is_done else '(No)'

    # if self.is_done:
    #   yes_or_no = '(Yes)'
    # else:
    #   yes_or_no = '(No)'

    # self.display_name = self.title +' '+ yes_or_no

  @api.multi
  @api.constrains('date_deadline')
  def validate_date_deadline(self):
    self.ensure_one()
    today = datetime.now().date()

    if self.date_deadline and today > fields.Date.from_string(self.date_deadline):
      raise ValidationError('Deadline must be future date')

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
