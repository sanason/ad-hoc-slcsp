from slcsp import extract_rate_areas_per_zipcode, extract_slscp_per_rate_area, extract_slcsp_per_zipcode

plans = [
    {
        'plan_id': '50660KV6559607',
        'state': 'GA',
        'metal_level': 'Catastrophic',
        'rate': '250.12',
        'rate_area': '1'
    },
    {
        'plan_id': '70914AN5022068',
        'state': 'GA',
        'metal_level': 'Bronze',
        'rate': '236.56',
        'rate_area': '1'
    },
    {
        'plan_id': '47213XR5169701',
        'state': 'GA',
        'metal_level': 'Silver',
        'rate': '308.32',
        'rate_area': '3'
    },
    {
        'plan_id': '89017TI4653426',
        'state': 'GA',
        'metal_level': 'Silver',
        'rate': '308.32',
        'rate_area': '3'
    },
    {
        'plan_id': '90721QV8914620',
        'state': 'GA',
        'metal_level': 'Gold',
        'rate': '341.93',
        'rate_area': '2'
    },
    {
        'plan_id': '96410VW6342701',
        'state': 'GA',
        'metal_level': 'Silver',
        'rate': '249.72',
        'rate_area': '2'
    },
    {
        'plan_id': '23107MQ2971140',
        'state': 'GA',
        'metal_level': 'Silver',
        'rate': '304.53',
        'rate_area': '2'
    },
    {
        'plan_id': '83504GU5812189',
        'state': 'AL',
        'metal_level': 'Silver',
        'rate': '201.25',
        'rate_area': '3'
    },
    {
        'plan_id': '33021HF7327978',
        'state': 'AL',
        'metal_level': 'Silver',
        'rate': '199.05',
        'rate_area': '3'
    },
]

zips = [
    {
        'zipcode': '30318',
        'state': 'GA',
        'county_code': '36035',
        'name': 'Fulton',
        'rate_area': '2'
    },
    {
        'zipcode': '35111',
        'state': 'AL',
        'county_code': '01073',
        'name': 'Jefferson',
        'rate_area': '3'
    },
    {
        'zipcode': '35111',
        'state': 'AL',
        'county_code': '301125',
        'name': 'Tuscaloosa',
        'rate_area': '12'
    },
]


def test_extract_slscp_per_rate_area_no_plans_for_area():
    output = extract_slscp_per_rate_area(plans)
    assert output.get(('GA', '5')) is None


def test_extract_slscp_per_rate_area_no_silver_plans_for_area():
    output = extract_slscp_per_rate_area(plans)
    assert output.get(('GA', '1')) is None


def test_extract_slscp_per_rate_area_only_one_silver_plan_rate_for_area():
    output = extract_slscp_per_rate_area(plans)
    assert output.get(('GA', '3')) is None


def test_extract_slscp_per_rate_area_multiple_silver_plan_rates_for_area():
    output = extract_slscp_per_rate_area(plans)
    assert output.get(('GA', '2')) == 249.72
    assert output.get(('AL', '3')) == 199.05


def test_extract_rate_areas():
    output = extract_rate_areas_per_zipcode(zips)
    assert output['30318'] == [('GA', '2')]
    assert output['60640'] == []
    assert output['35111'] == [('AL', '3'), ('AL', '12')]


def test_extract_slscp_per_zipcode():
    output = extract_slcsp_per_zipcode(plans, zips)
    assert output == {'30318': 249.72}
