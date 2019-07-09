from django.contrib import admin

# Register your models here.

from .models import Entity, EntityHasComponent


#class EntityInline(admin.StackedInline):
class LinkedInline(admin.TabularInline):
    model = Entity
    fk_name = 'linked_to'
    extra = 3


#class EntityHasComponentInline(admin.StackedInline):
class EntityHasComponentInline(admin.TabularInline):
    model = EntityHasComponent
    fk_name = 'compound'


class EntityAdmin(admin.ModelAdmin):
    #ordering = ('-name',)
    ordering = ('name',)
    # The list of fields to be displayed (and in which order)
    #fields = ['name', 'is_linked_to']
    fieldsets = [

        (None,               
            {'fields': ['name', 'abbr', 'perso', 'living', ('date_birth', 'date_death'), 'is_a', 'is_domain', 'domain', 'comment']}
        ),

        # is_linked_to 1 entity :
        #('Relationships with other entities', {'fields': ['is_linked_to', 'link_direct_name', 'link_reverse_name', 'implies', 'is_composed_of']}),
        ('Relationships with other entities', 
            # Component without through table
            #{'fields': ['opposite', 'linked_to', 'linked_to_direct_name', 'linked_to_reverse_name', 'implies', 'components', 'related_to']}
            # Component with through table : on ajoute EntityHasComponentInline below
            {'fields': ['opposite', ('linked_to_direct_name', 'linked_to', 'linked_to_reverse_name'), ('not_me', 'implies_not', 'implies'), 'synonyms']}
        ),
        # is_linked_to N entity(s) :
        ##('Relationships with other entitys', {'fields': ['link_direct_name', 'link_reverse_name', 'implies', 'is_composed_of']}),

        #('Attributes', {'fields': ['speed', 'height']}),
        ('Attributes', 
            {
                'fields': [('a_speed', 'a_speed_rotation'), ('a_radius', 'a_perimeter'), ('a_height', 'a_width', 'a_length', 'a_depth'), ('a_frequency', 'a_wavelength')], 
                #'classes': ['collapse']
            }
        ),
    ]
    # is_linked_to N entity(s) :
    ##inlines = [LinkedInline]
    # For the "index" view page (Change) :
    search_fields = ['name']
    list_display = ('name', 'is_a')
    list_filter = ['date_created', 'is_a']

    # Component with through table : on ajoute EntityHasComponentInline
    inlines = [EntityHasComponentInline]



# Default admin site
#admin.site.register(Entity)
# Customized admin site
admin.site.register(Entity, EntityAdmin)
#admin.site.register(EntityHasComponent)
