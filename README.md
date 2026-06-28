# Project 7 — Web Automation Testing | Playwright + Python

## Overview
Web automation testing project using Playwright and Python.
This project automates a real e-commerce user flow on Noon.com UAE —
from searching for a product to verifying the product page loaded correctly.

## Test Summary
| Field | Details |
|---|---|
| Tester | Ammar Hourani |
| Environment | Mac / Python 3.9.6 / Playwright 1.60.0 |
| Site Tested | Noon.com UAE (noon.com/uae-en) |
| Total Scripts | 1 |
| Total Assertions | 3 |
| Overall Status | Pass |

## Test Flow
| Step | Action | Verification |
|---|---|---|
| 1 | Open Noon UAE homepage | Page loads |
| 2 | Search for "iPhone" | Autocomplete suggestions appear |
| 3 | Click iPhone suggestion | Search results load |
| 4 | Verify first product visible | Product list is not empty |
| 5 | Click first product | Product page opens |
| 6 | Verify product title | Title is visible |
| 7 | Verify product price | Current price is displayed |

## Challenges Solved
- **Flaky test** — search suggestions disappeared before Playwright could click them. Fixed using wait_for() to wait for suggestions to appear first
- **Bot detection** — Noon blocked cart functionality for automated browsers. Worked around by focusing test on verifiable page elements
- **Hardcoded price** — initial version used a specific price that would break if price changed. Fixed by targeting the price element using data-qa attribute instead

## Tools Used
- Python 3.9.6
- Playwright 1.60.0
- pytest 8.4.2
- VS Code

## How to Run
1. Install Playwright: pip3 install pytest-playwright
2. Install browsers: playwright install
3. Run test: pytest test_noon.py -v

## Files
- `conftest.py` — pytest fixture for browser setup
- `test_noon.py` — full Playwright test script
