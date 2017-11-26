from odoo import models, fields

class EnhanceTodoTask(models.Model):
    _inherit = 'todo_app.task'

    priority = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ],
    string = 'Task Priority',
    default='low')
