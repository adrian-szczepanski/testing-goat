from django.test import TestCase
from lists.models import Item, List


class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()

        self.assertEqual(2, saved_items.count())
        self.assertEqual('The first (ever) list item', saved_items[0].text)
        self.assertEqual('Item the second', saved_items[1].text)
        self.assertEqual(saved_items[0].list, list_)
        self.assertEqual(saved_items[1].list, list_)

