# EazyBuy API

## Overview

EazyBuy API is a simple Django REST Framework API that works with my Django EazyBuy E-commerce website to retrieve product informations like

- Category
- Graphics details
- Operating system
- Memory limitations
- Processor speed
- Hard drive space
- Processor technology
- Power supply
- Battery capacity

## Documentation

**Request Parameters**
You can search for products with any combinations of the following criteria

- Category: Eg. Find Laptops
- Title: Eg. Find Lenovo Laptops
- Limit: Eg. Find 10 Lenovo Laptops

**Response Codes**
The API appends a "response_code" to each API call to help tell developers what the API is doing or has done.

- **Code 0**: Success.
Returned all or available results successfully

- **Code 1**: No Results
Could not return results (Eg. Asking for a title that doesn't exist in a category)

- **Code 2**: Invalid Parameter
Arguments passed in are not valid (Eg. limit=Three)

## Demo
