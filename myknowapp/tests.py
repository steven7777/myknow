from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Entity, EntityHasComponent


class EntityModelTests(TestCase):

    def test_a_opposite_b_is_symmetrical(self) :
        """
        a opposite b => b opposite a
        """
        time = timezone.now() + datetime.timedelta(days=30)
        a = Entity(name='A')
        b = Entity(name='B')
        b.save()
        a.opposite=b
        a.save()
        b = Entity.objects.get(name='B')
        #self.assertIs(b.opposite.name == 'A', True)
        self.assertIs(b.opposite.name,'A')

    def test_components(self) :
        """
        a composed of b and c => b and c have a as compound
        """
        a = Entity.objects.create(name='A')
        b = Entity.objects.create(name='B')
        c = Entity.objects.create(name='C')
        self.assertIs(a.has_components.all().exists(),False)
        a.has_components.add(b,c)
        a.save()
        self.assertIs(a.has_components.all().exists(),True)
        self.assertIs(a.has_components.all()[0].name,'B')
        self.assertIs(a.has_components.all()[1].name,'C')
        self.assertIs(a.components.all().count(),2)
        self.assertIs(a.components.all()[0].component.name,'B')
        self.assertIs(a.components.all()[1].component.name,'C')
        self.assertIs(a.components.all()[0].compound.name,'A')
        self.assertIs(a.components.all()[1].compound.name,'A')

        d = Entity.objects.create(name='D')
        comp = EntityHasComponent(compound=a, component=d, qty=10)
        comp.save()
        self.assertIs(a.components.all().count(),3)
        d_comp = a.components.all().get(component__name='D')
        self.assertIs(d_comp.qty,10)


class EntityIndexViewTests(TestCase):
    def test_no_entity(self):
        pass
        """
        If no entity exist, an appropriate message is displayed.
        """
        '''
        response = self.client.get(reverse('myknowapp:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_entity_list'], [])
        '''
        
class EntityDetailViewTests(TestCase):

    def test_entity_does_notexist(self):
        url = reverse('myknowapp:detail', args=(5,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_entity_exists(self):
        """
        Create an entity and check that it can be viewed (in detail)
        """
        opp = Entity.objects.create(name='e opposite')
        #e = Entity.objects.create(name='toto')
        e = Entity(name='toto', opposite=opp)
        e.save()
        url = reverse('myknowapp:detail', args=(e.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, e.name)
        self.assertContains(response, 'toto')
        self.assertContains(response, 'Opposite:')
        self.assertContains(response, 'e opposite')


