from django.contrib import admin
from .models import VRCPubs

class VRCPubsAdmin(admin.ModelAdmin): 
    list_display = ('title', 'author', 'publishedAt', 'category') 

# Register your models here.
admin.site.register(VRCPubs, VRCPubsAdmin)

admin.site.site_header = "CMPN PAPER PUBLICATIONS"