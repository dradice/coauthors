# Coauthors

## About

Create a CSV list of all coauthors starting from a given year using
data from the [iNSPIRE-HEP](https://inspirehep.net) database.

```
usage: coauthors.py [-h] -b BAI [--format {DOE,NSF}] [--since SINCE]
                    [-o OUTPUT]
                    [keys ...]

positional arguments:
  keys                  only consider these keys

optional arguments:
  -h, --help            show this help message and exit
  -b BAI, --bai BAI     author identification string (required)
  --format {DOE,NSF}    output format (defaults to NSF)
  --since SINCE         if specified lists coauthors since the given year
  -o OUTPUT, --output OUTPUT
                        output file (if not specified outputs to stdout)
```

The author identification string is the unique ID associated with you
on [iNSPIRE-HEP](https://inspirehep.net). For example, mine is
"D.Radice.1". I would recommended linking
[iNSPIRE-HEP](https://inspirehep.net) and [ORCiD](https://orcid.org/)
and synching all papers prior running the script.

The primarily use of this script is to create/update lists of
coauthors that can be included in the [NSF Collaborators and Other
Affiliations (COA) Information
form](https://nsf.gov/bfa/dias/policy/coa.jsp). While the output of
this script can in most cases be copied and pasted directly into the COA form,
it is advisable to manually verify each entries. You are ultimately
responsible for the validity of the content of your submission to NSF.

## License

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

## Acknowledgements

I adapted some code for the interface with iNSPIRE-HEP from
[citations.py](https://github.com/efranzin/python/blob/master/citations.py).
