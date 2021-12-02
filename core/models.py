# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)


class BaseModel(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(BaseModel, self).fields_get(allfields, attributes)

        # _logger.info("debug mode: %s", request.debug)
        # _logger.info("group_no_one: %s", self.user_has_groups('base.group_no_one'))

        # check if we are in debug mode and the feature is enabled
        if request and request.debug and self.user_has_groups('debug_fieldsname.group_show_fields_name'):
            for field in res:
                res[field]['string'] = field

        return res
