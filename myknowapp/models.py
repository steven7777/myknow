from django.db import models

# Create your models here.

class Entity(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=10, blank=True, null=True)

    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    #date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_birth = models.DateField(blank=True, null=True)
    date_death = models.DateField(blank=True, null=True)
    #pub_date = models.DateTimeField('date published')
    #votes = models.IntegerField(default=0)

    # RELATIONSHIPS

    # - Generalization : 
    # "Mars" is_a "Planet" (superclass), and "Planet" is_a "CelestialBody"
    # Reverse : "Planet" has subclasses "Mars", "Earth", "Venus"...
    #is_a = models.ForeignKey('Entity', on_delete=models.CASCADE, related_name="subclasses", null=True)
    is_a = models.ForeignKey('self', on_delete=models.CASCADE, related_name="subclasses", blank=True, null=True)

    domain = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="domain_entities", blank=True, null=True)
    is_domain = models.BooleanField(default=False)

    comment = models.TextField(blank=True, null=True)

    # - STRONG Association
    #is_linked_to = models.ForeignKey('Entity', on_delete=models.DO_NOTHING, related_name="links")
    #is_linked_to = models.ForeignKey('Entity', on_delete=models.SET_NULL, related_name="linked", null=True)
    linked_to = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="linked", blank=True, null=True, help_text="STRONG link (like Earth 'turns around' Sun)")
    linked_to_direct_name = models.CharField(max_length=100, null=True, blank=True)
    linked_to_reverse_name = models.CharField(max_length=100, null=True, blank=True)

    # - Consequence/Implication
    not_me = models.BooleanField(default=False, help_text="NOT me")
    #implies = models.ForeignKey('Entity', on_delete=models.SET_NULL, related_name="consequences", null=True)
    implies = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="consequences", blank=True, null=True)
    implies_not = models.BooleanField(default=False, help_text="implies NOT")

    # - Composition/Agregation:
    #is_composed_of = models.ManyToManyField('Entity', through='CompoundHasComponents', related_name='components', null=True)
    #is_composed_of = models.ManyToManyField('Entity', related_name='components', null=True)
    #is_composed_of = models.ManyToManyField('self', symmetrical=False, related_name='components', blank=True)
    # NO QTY FOR COMPONENT
    #components = models.ManyToManyField('self', symmetrical=False, related_name='compounds', blank=True)
    # COMPONENT with a quantity
    has_components = models.ManyToManyField('self', through='EntityHasComponent', symmetrical=False, related_name='iscomponentof', blank=True)

    # - WEAK Association - Symetrical links ("friend of", "synonym of", "related to"...)
    #related_to = models.ManyToManyField('self', symmetrical=True, blank=True, help_text="WEAK link (like 'is friend of', 'is synonym of', ...)")
    synonyms = models.ManyToManyField('self', symmetrical=True, blank=True)

    # - Opposite ("love"=>"hate")
    # For a symmetrical relaiton, see https://stackoverflow.com/questions/55522760/django-symmetrical-relation-onetoonefield
    # Also, https://stackoverflow.com/questions/28307964/django-symmetrical-relation
    opposite = models.OneToOneField('self', on_delete=models.SET_NULL, blank=True, null=True)

    # ATTRIBUTES with UNITS (all preceded with prefix 'a_')
    a_radius = models.CharField('Radius (km)', max_length=20, null=True, blank=True)
    a_perimeter = models.CharField('Perimeter (km)', max_length=20, null=True, blank=True)
    a_speed = models.CharField('Speed (km/s)', max_length=20, null=True, blank=True)
    a_speed_rotation = models.CharField('Rotation speed (km/h)', max_length=20, null=True, blank=True)
    a_height = models.CharField('Height (m)', max_length=20, null=True, blank=True)
    a_width = models.CharField('Width (m)', max_length=20, null=True, blank=True)
    a_length = models.CharField('Length (m)', max_length=20, null=True, blank=True)
    a_depth = models.CharField('Depth (m)', max_length=20, null=True, blank=True)
    a_wavelength = models.CharField('Wavelength (m)', max_length=20, null=True, blank=True)
    a_frequency = models.CharField('Frequency (Hz)', max_length=20, null=True, blank=True)

    # GENERAL ATTRIBUTES
    living = models.BooleanField(default=False)
    perso = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'entity'
        verbose_name_plural = "entities"

    def __str__(self):
        return (str(self.name))

    def save(self, *args, **kwargs):
        # This is same as : super(Entity,self).save(*args, **kwargs)
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # Opposite : makes it reflexive : A <=> B : A opposite B => B opposite A
        # => makes the "opposite" entity points to me as its own opposite
        if self.opposite:
            ''' This does not work because it's infinitely recursive... : self saves also opposite wich saves also self (which is its opposite)...
            opp = Entity.objects.get(pk=self.opposite.id)
            opp.opposite = self
            opp.save(update_fields=['opposite'])
            '''
            self.opposite.opposite = self
            super(Entity,self.opposite).save()


class EntityHasComponent(models.Model):
    qty = models.IntegerField(default=1)
    compound = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='components')
    component = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='compounds')
    #date_joined = models.DateField()
    #invite_reason = models.CharField(max_length=64)


