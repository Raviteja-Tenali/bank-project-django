from django.contrib import admin
from accounts.models import accountholder
from accounts.models import banktype
from accounts.models import amounttype

class accountholderAdmin(admin.ModelAdmin):
    list_display=['Name','Withdraw','interest','interestperyear']

class banktypeAdmin(admin.ModelAdmin):
    list_display=['deposit']

class amounttypeAdmin(admin.ModelAdmin):
    list_display=['withdraw']

# Register your models here.
admin.site.register(accountholder,accountholderAdmin)
admin.site.register(banktype,banktypeAdmin)
admin.site.register(amounttype,amounttypeAdmin)


