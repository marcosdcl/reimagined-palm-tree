from customer.models import Customer
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'doc_num', 'phone')


admin.site.register(Customer, CustomerAdmin)
