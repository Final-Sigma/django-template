from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

class ProjectAdmin(admin.AdminSite):
    pass
    # Set custom variables

    # logout_template = 'admin/logout.html'

    # title_header = 'Project Admin'
    # site_header = 'Project Administration'
    # index_title = 'Project Admin'
    
    
class ProjectAdminConfig(AdminConfig):    
    default_site = 'project_admin.admin.ProjectAdmin'
