from mypackage import my_module
def test_error():
    '''
    make sure my module worls correctly
    '''

    assert my_module.standard_mean_error([31.7, 29.6, 28.8, 30.6, 29.5, 28.9, 30.4, 29.2, 30.8, 29.9]) == 0.2964562196528, 'correct'

