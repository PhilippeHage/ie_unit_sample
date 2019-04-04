from ie_nlp_utils import sum_numbers


def test_sum_two_numbers_gives_expected_result():
    a = 2
    b = 2

    expected_output = 4

    output = sum_numbers(a, b)

    assert output == expected_output
