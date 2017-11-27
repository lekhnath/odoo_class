from odoo import models, fields

class TodoTag(models.Model):
    _name='enhance_todo_app.tag'

    name = fields.Char('Name')
    active = fields.Boolean('Is Active?', default=True)

class EnhanceTodoTask(models.Model):
    _inherit = 'todo_app.task'

    priority = fields.Selection([
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ],
    string = 'Task Priority',
    default='low')

    assignee_id = fields.Many2one(
        string='Assigned To',
        comodel_name='res.users',
        ondelete='set null',
    )

    tag_ids = fields.Many2many(
        comodel_name='enhance_todo_app.tag',
        string='Tags'
    )
