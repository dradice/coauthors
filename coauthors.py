#!/usr/bin/env python
# Creates a list of coauthors

"""
Given an author generates a list of all coauthors since a given year.
Data is imported from the INSPIRE-HEP database.

Known limitations.
* Will only parse the most recent 1,000 publications

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__author__  = 'David Radice'
__version__ = '1.0'
__license__ = 'GPL'
__email__   = 'dur566@psu.edu'

import argparse
import csv
import sys
import urllib.request, json

# Parse CLI
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bai", dest="bai", required=True,
        help="author identification string (required)")
parser.add_argument("--since", dest="since", type=int, default=0,
        help="if specified lists coauthors since the given year")
parser.add_argument("-o", "--output", dest="output",
        help="output file (if not specified outputs to stdout)")
args = parser.parse_args()

if args.output is None:
    outfile = sys.stdout
else:
    outfile = open(args.output, "w")

inspirehep_profile = 'https://inspirehep.net/api/literature?sort=mostrecent&size=1000&q=a%20' + args.bai
data = json.loads(urllib.request.urlopen(inspirehep_profile).read())

# Dictionary mapping author_bais to (name, affiliation, year)
entries = {}

for hit in data['hits']['hits']:
    year = int(hit['metadata']['earliest_date'][0:4])
    if year < args.since:
        print("Skipping {} since year {} is less than {}".format(
            hit['metadata']['texkeys'][0], year, args.since))
    for author in hit['metadata']['authors']:
        author_bai = author["bai"]
        author_name = author["full_name"]
        # Exclude yourself from coauthor lists
        if author_bai == args.bai:
            continue
        # Check if this is a new author
        if not author_bai in entries:
            if "affiliations" in author:
                affiliation = author["affiliations"][0]["value"]
            elif "raw_affiliations" in author:
                affiliation = author["raw_affiliations"][0]["value"]
            else:
                affiliation = "Unknown"
            entries[author_bai] = (author_name, affiliation, year)
        # Prefer longer version of name
        else:
            if len(author_name) > len(entries[author_bai][0]):
                _, affiliation, year = entries[author_bai]
                entries[author_bai] = (author_name, affiliation, year)

writer = csv.DictWriter(outfile, ["Author", "Affiliation", "Last Active"])
writer.writeheader()
for author_bai, (author_name, affiliation, year) in entries.items():
    row = {"Author": author_name, "Affiliation": affiliation, "Last Active": year}
    writer.writerow(row)
