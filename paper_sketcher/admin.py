from django.contrib import admin

# Register your models here.
from .models import Profile, CS_Research_Paper, CS_Proposal, CS_Thesis, IS_Thesis, IS_Proposal, IS_Research_Paper

admin.site.site_header = "Research Paper Sketcher"
#admin.site.site_title = "Title ea page"
#admin.site.index_title = "Index title ea hao"

@admin.register(Profile)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(CS_Research_Paper)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(CS_Proposal)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(CS_Thesis)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(IS_Thesis)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(IS_Proposal)
class MainappAdmin(admin.ModelAdmin):
    pass

@admin.register(IS_Research_Paper)
class MainappAdmin(admin.ModelAdmin):
    pass