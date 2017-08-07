from django.test import TestCase
from ..models import Book


class BookTest(TestCase):

    def setUp(self):
        Book.objects.create(
            title="The Scientist and Engineer's Guide "\
                    "to Digital Signal Processing",
            author="Steven W. Smith",
            price="0.00",
            isbn="9780966017632")
        Book.objects.create(
            title="Real Sound Synthesis for Interactive Applications",
            author="Perry R. Cook",
            price="54.96",
            isbn="9781568811680")

    def test_book_model(self):
        dsp_book = Book.objects.get(isbn=9780966017632)
        synth_book = Book.objects.get(isbn=9781568811680)
        self.assertEqual(
            dsp_book.title,
            "The Scientist and Engineer's Guide to Digital Signal Processing")
        self.assertEqual(
            synth_book.title,
            "Real Sound Synthesis for Interactive Applications")
