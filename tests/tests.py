import unittest
import friends as friends


class Test(unittest.TestCase):
    def setUp(self):
        self.token = \
            '8abcb1528abcb1528abcb152408ad43e5388abc8abcb152d6e13d15574a6a3ca2d54608'

    def test_get_id(self):
        with self.subTest(case='By username must return id (fiza09)'):
            self.assertEqual(friends.get_id('fiza09', self.token), 65308700)
        with self.subTest(case='By username must return id (titusjaka)'):
            self.assertEqual(friends.get_id('titusjaka', self.token), 14807196)

        with self.subTest(case='By id must return id (65308700)'):
            self.assertEqual(friends.get_id('65308700', self.token), 65308700)
        with self.subTest(case='By id must return id (14807196)'):
            self.assertEqual(friends.get_id('14807196', self.token), 14807196)

        with self.subTest(case='By incorrect id should return ValueError'):
            self.assertRaises(ValueError, friends.get_id, 'fiza', self.token)

    def test_get_friends(self):
        with self.subTest(case='Should return list of dicts with id (int) and bdate (str)'):
            friend_list = friends.get_friends(65308700, self.token)
            self.assertIsInstance(friend_list, list)
            self.assertEqual(len(friend_list), 85)
            self.assertIsInstance(friend_list[0], dict)
            friend_data = {'id': 447952, 'first_name': 'Sergey', 'last_name': 'Avdonin', 'bdate': '2.2'}
            self.assertIn(friend_data, friend_list)

    def test_get_age_dict(self):
        with self.subTest(case='Should return a dictionary where the key is age, '
                               'and the value is the number of people of that age.'):
            friends_list = [
                {'id': 447952, 'first_name': 'Sergey', 'last_name': 'Avdonin', 'bdate': '2.2'},
                {'id': 1471450, 'first_name': 'Denis', 'last_name': 'Mukhametyanov', 'bdate': '23.6'},
                {'id': 471132068, 'first_name': 'Valentina', 'last_name': 'Pakhomova', 'deactivated': 'banned'},
                {'id': 61686388, 'first_name': 'Alexey', 'last_name': 'Chukhlantsev', 'bdate': '19.3.1993', 'lists': [29]},
                {'id': 7769983, 'first_name': 'Anastasia', 'last_name': 'Malikova', 'bdate': '4.4.1993', 'lists': [26]},
                {'id': 12129619, 'first_name': 'Water', 'last_name': 'Lily', 'lists': [27]},
                {'id': 23431910, 'first_name': 'Ivan', 'last_name': 'Morozov', 'bdate': '1.1.1920'},
                {'id': 4161243, 'first_name': 'Ivan', 'last_name': 'Gusev'},
                {'id': 106367911, 'first_name': 'Evgeny', 'last_name': 'Veritov', 'bdate': '7.2.1989'}
            ]

            expected_dict = {
                26: 2,
                99: 1,
                30: 1,
            }

            self.assertEqual(friends.count_friends_of_same_age(friends_list), expected_dict)

        with self.subTest(case='If user does not have a bdate, '
                               'he should not be included in the dict'):
            friends_list = [
                {'id': 4161243, 'first_name': 'Ivan', 'last_name': 'Gusev'}
            ]

            self.assertEqual(friends.count_friends_of_same_age(friends_list), {})

        with self.subTest(case='If there is no year in bdate, the user should not be dict'):
            friends_list = [
                {'id': 1471450, 'first_name': 'Denis', 'last_name': 'Mukhametyanov', 'bdate': '23.6'}
            ]

            self.assertEqual(friends.count_friends_of_same_age(friends_list), {})

    def test_get_year(self):
        with self.subTest(case='Should return year (int) if there is no year in bdate'):
            self.assertEqual(friends.get_year('7.2.1989'), 1989)
        with self.subTest(case='Should return None if there is no year in bdate'):
            self.assertEqual(friends.get_year('2.2'), None)

    def test_output(self):
        with self.subTest(case='Should return list of tuples ages and counts, '
                               'sorted by count (reverse) and by ages'):
            test_dict = {
                21: 6,
                40: 2,
                20: 1,
                26: 8,
                19: 1,
                22: 6
            }

            expected_list = [
                (26, 8),
                (21, 6),
                (22, 6),
                (40, 2),
                (19, 1),
                (20, 1),
            ]

            self.assertEqual(friends.format_data_for_output(test_dict), expected_list)
