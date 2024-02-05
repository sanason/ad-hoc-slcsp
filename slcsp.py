import csv
import sys
from collections import defaultdict


# Create and populate a dict "state,rate_area" -> slscp from a list of plans
def extract_slscp_per_rate_area(plans: list[dict]) -> dict:
    rate_area_to_rates = defaultdict(set)
    for plan in plans:
        if plan['metal_level'] != 'Silver':
            continue
        rate = float(plan['rate'])
        rate_area = plan['state'], plan['rate_area']
        rate_area_to_rates[rate_area].add(rate)
    return {k: sorted(v, reverse=True)[1] for k, v in rate_area_to_rates.items() if len(v) > 1}


# Each zipcode lies within one or more rate areas
# Create and populate a dict zipcode -> list of rate_area
def extract_rate_areas_per_zipcode(zips: list[dict]) -> dict:
    zipcode_to_rate_areas = defaultdict(list)
    for z in zips:
        zipcode_to_rate_areas[z['zipcode']].append((z['state'], z['rate_area']))
    return zipcode_to_rate_areas


def extract_slcsp_per_zipcode(plans, zips) -> dict:
    zipcode_to_slscp = {}
    rate_area_to_slscp = extract_slscp_per_rate_area(plans)
    zipcode_to_rate_areas = extract_rate_areas_per_zipcode(zips)
    for zipcode, rate_areas in zipcode_to_rate_areas.items():
        # Only set slcsp for zipcode if rate area for zipcode is unambiguous
        if len(rate_areas) == 1:
            unique_rate_area_for_zip = rate_areas[0]
            zipcode_to_slscp[zipcode] = rate_area_to_slscp.get(unique_rate_area_for_zip)
    return zipcode_to_slscp


def main():
    with (open('input/plans.csv', newline='') as plan_file,
          open('input/zips.csv', newline='') as zip_file,
          open('input/slcsp.csv', newline='') as slcsp_file):
        plans = list(csv.DictReader(plan_file))
        zips = list(csv.DictReader(zip_file))
        zipcode_to_slcsp = extract_slcsp_per_zipcode(plans, zips)

        reader = csv.reader(slcsp_file)
        writer = csv.writer(sys.stdout)
        # write the header row
        writer.writerow(next(reader))

        for row in reader:
            zipcode = row[0]
            slscp = zipcode_to_slcsp.get(zipcode)
            writer.writerow([zipcode, slscp])


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
