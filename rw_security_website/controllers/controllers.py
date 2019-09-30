# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_forum.controllers.main import WebsiteForum


class RestrictWebBLog(WebsiteBlog):
    @http.route(auth='user')
    def blogs(self):
        return super(RestrictWebBLog, self).blogs()


class RestrictWebsite(Website):
    @http.route(auth='user')
    def index(self):
        return super(RestrictWebsite, self).index()

class RestrictForum(WebsiteForum):
    @http.route(auth='user')
    def forum(self):
        return super(RestrictForum, self).forum()
