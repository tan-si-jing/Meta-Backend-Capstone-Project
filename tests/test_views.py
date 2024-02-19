from django.test import TestCase, RequestFactory
from api.models import MenuItem
from api.serializers import MenuItemSerializer
from api.views import MenuItemsView

class MenuViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        MenuItem.objects.create(
            title="Item 1",
            price=25,
            inventory=10
        )
        MenuItem.objects.create(
            title="Item 2",
            price=10,
            inventory=4
        )

    def test_getall(self):
        menuitems = MenuItem.objects.all()
        serialized_menuitems = MenuItemSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)