from odoo import models


class Project(models.Model):
    _inherit = 'project.project'

    def action_remove_follower_on_task(self):
        for rec in self:
            if rec.task_ids:
                project_partner_ids = rec.message_partner_ids.ids + rec.env.user.partner_id.ids
                task_partner_ids = rec.tasks.message_partner_ids.ids + rec.env.user.partner_id.ids
                rec.message_unsubscribe(partner_ids=project_partner_ids)
                rec.tasks.message_unsubscribe(partner_ids=task_partner_ids)