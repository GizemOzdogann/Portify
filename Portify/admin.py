from django.contrib import admin
from Project.models import MyModel, ContactMessage

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)      

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')  
    search_fields = ('name', 'email')                 
    list_filter = ('email',)   