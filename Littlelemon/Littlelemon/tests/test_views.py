from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Crear instancias de prueba del modelo Menu
        self.client = APIClient()
        
        self.user = User.objects.create_user(username='testuser', password='Usu4r10T')

        # Autenticar al cliente con el usuario de prueba
        self.client.force_authenticate(user=self.user)
        
        self.item1 = Menu.objects.create(title="IceCream", price=8, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza Pepperoni", price=12, inventory=50)
        self.item3 = Menu.objects.create(title="Burger", price=10, inventory=200)

    def test_getall(self):
        # Obtener la URL de la vista que devuelve todos los objetos Menu
        url = reverse('menu-list')  # Usa el nombre de la ruta
        response = self.client.get(url) # Asegúrate de que la URL coincida con la definida en urls.py

        # Serializar los datos esperados
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Comprobar si los datos serializados son iguales a la respuesta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)