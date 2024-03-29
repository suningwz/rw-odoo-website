# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_forum.controllers.main import WebsiteForum
from odoo.addons.web.controllers.main import Home


class RestrictWebBLog(WebsiteBlog):
    @http.route(auth='user')
    def blog(self, blog=None, tag=None, page=1, **opt):
        return super(RestrictWebBLog, self).blog(blog, tag, page, **opt)

    @http.route(auth='user')
    def blog_post(self,blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        return super(RestrictWebBLog, self).blog_post(blog, blog_post, tag_id, page, enable_editor, **post)

class RestrictWebsite(Website):
    @http.route(auth='user')
    def index(self):
        return super(RestrictWebsite, self).index()

class RestrictForum(WebsiteForum):
    @http.route(auth='user')
    def forum(self, **kwargs):
        return super(RestrictForum, self).forum(**kwargs)


