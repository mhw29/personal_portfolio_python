from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
