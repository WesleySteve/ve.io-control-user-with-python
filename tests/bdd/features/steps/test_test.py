from behave import when, then


@when('sum "{num_1:d}" and "{num_2:d}"')
def sum_two_values(context, num_1, num_2):
    pass


@then('result must equal "{result:d}"')
def assert_result(context, result):
    pass
