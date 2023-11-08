from django.contrib import admin
from .models import PostForm, CommentForm
from django.contrib.auth.models import * 



# Register your models here.
# admin.site.register(Post)
admin.site.register(CommentForm)

class CommentAdminInline (admin.TabularInline):
    model = CommentForm



#В случае, если нам не нужны дополнительные настройки в админке, а просто добавить в админку
# admin.site.register(WorkingService)

# Если нам нужно что-то поменять (все пункты работают, проверено)

@admin.register(PostForm)
class WorkingServiceAdmin (admin.ModelAdmin):
    # Фильтр по дате - в модели тоже должно быть это поле (иначе откуда брать данные)    
    date_hierarchy = "date_create"

#     #Отвечают за поля, которые будут отображаться при создании формы
#     # Эти данные будут приходит в запросе POST в WorkingService 
#     # Если мы ничего не напишем, то отображаться будут все, которые есть у модели   
    fields = ["date_create","title", "text", "counter", "category"]

    # # исключить какой-то параметр из отображения
    # # либо мы пишем те, которые показать, либо те, которые исключить (из создания и изменения)
    # exclude = ["text"]    
    # # pass

    # # пишем те поля, которые отображаются в верхнем каталоге данных
    # Если не напишем, то будет отображать например Post object (44)
    list_display = ["title","date_create", "category","counter","get_counter_byn"]

    # # Пишем сюда то, что отображается в админке, но нельзя менять
    # # работает в паре с fields
    readonly_fields = ["date_create"]

    # # Указываем fields, по которым будет поиск (один параметр)
    search_fields = ["category"]
    # search_fields = ["title__startswith"]
    # search_fields = ["name__endswith"]
    
    # # Сортировка по полю
    ordering = ["-date_create"] 

    # # Поля, к которым добавляем фильтры
    list_filter = ["category", "counter"]

    list_editable = ['counter']

    inlines = [
        CommentAdminInline,  
    ]
    def get_counter_byn(self,obj: PostForm):
        return obj.counter * 2
    get_counter_byn.short_desctiption = 'BYN price'
    


