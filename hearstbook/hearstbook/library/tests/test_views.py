from django.core.exceptions import ObjectDoesNotExist
from ..models import Book
from ..serializers import BookSerializer
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class BookViewTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        Book.objects.create(
            title="The Scientist and Engineer's Guide to Digital Signal Processing",
            author="Steven W. Smith",
            price="0.00",
            isbn="9780966017632")
        Book.objects.create(
            title="Real Sound Synthesis for Interactive Applications",
            author="Perry R. Cook",
            price="54.96",
            isbn="9781568811680")

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_filter_book_by_isbn(self):
        response = self.client.get(
            reverse('book-list'),
            {'isbn':'9780966017632'},
            format='json')
        book = Book.objects.filter(isbn="9780966017632")
        serializer = BookSerializer(book, many=True)
        self.assertEqual(response.data,  serializer.data)

    def test_filter_book_by_title(self):
        response = self.client.get(
            reverse('book-list'),
                {'title':'Real Sound Synthesis for Interactive Applications'})
        book = Book.objects.filter(title="Real Sound Synthesis for Interactive Applications")
        serializer = BookSerializer(book, many=True)
        self.assertEqual(response.data,  serializer.data)

    def test_book_delete(self):
        book = Book.objects.create(
            title="The Scientist and Engineer's Guide to Digital Signal Processing - Part Deux",
            author="Steven W. Smith",
            price="0.00",
            isbn="9780966017633")
        response = self.client.delete(
            reverse(
                'book-detail',
                kwargs={'pk':book.pk})
            )
        with self.assertRaises(ObjectDoesNotExist) as context:
            book = Book.objects.get(pk=book.pk)

