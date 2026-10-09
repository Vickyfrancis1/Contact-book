def add_contact(contacts, name, number):
    contacts[name.strip().title()] = number.strip()

def find_contact(contacts, name):
    return contacts.get(name.strip().title())

def delete_contact(contacts, name):
    name = name.strip().title()
    if name in contacts:
        del contacts[name]
        return True
    return False

import unittest

class TestContacts(unittest.TestCase):

    def test_add_and_find(self):
        book = {}
        add_contact(book, "  leo ", "0801")
        self.assertEqual(find_contact(book, "LEO"), "0801")

    def test_find_missing(self):
        self.assertIsNone(find_contact({}, "Ngozi"))

    def test_delete_existing(self):
        book = {"Leo": "0801"}
        self.assertTrue(delete_contact(book, "leo"))
        self.assertEqual(book, {})

    def test_delete_missing(self):
        self.assertFalse(delete_contact({}, "Ngozi"))

unittest.main(exit=False)
