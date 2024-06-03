def handle_recipe_offline():
    # fetch recipes
    return {'recipe': {'name': 'carrot soup',
                       'prepartion_steps': [
                           {
                               'step_order': 1,
                               'step_details': 'Wash,peel and chop your carrots into small even chunks',
                               'suggested_time_in_minutes': 15,
                           }
                       ],
                       'method': [{
                           'step_order': 1,
                           'step_details': 'To a boiling pan of water add your diced carrots and pumpkin. Allow '
                                           'the vegetables to cook until the water evaporates.',
                           'suggested_time_in_minutes': 15,
                       }],
                       'ingredients': [
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'carrots',
                               'amount': 500,
                               'measurement_unit': 'g',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           },
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'pumpkin',
                               'amount': 500,
                               'measurement_unit': 'g',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           },
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'onion',
                               'amount': 1,
                               'measurement_unit': '',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           },
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'vegetable stock',
                               'amount': 500,
                               'measurement_unit': 'ml',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           },
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'cream',
                               'amount': 250,
                               'measurement_unit': 'ml',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           },
                           {
                               'ingredient_id': '1213456787',
                               'ingredient': 'cream',
                               'amount': 250,
                               'measurement_unit': 'ml',
                               'nutritional_information': {
                                   'vitamins': ['k', 'a'],
                                   'protein_per_serving': '5g'
                               }
                           }
                       ],
                       'people_per_portion': 2,
                       'likes': 9867,
                       'season_suggestion': ['winter', 'spring', 'summer', 'fall'],
                       'dietary_suggestion': ['vegetarian', 'pescatarian'],
                       'user_comments': [
                           {'date_time': '2021-01-25 00:00:00',
                            'active_user': True,
                            'user_name': 'name',
                            'comment': 'I really enjoyed ths dish'}
                       ]
                       }}


if __name__ == '__main__':
    print(handle_recipe_offline())
